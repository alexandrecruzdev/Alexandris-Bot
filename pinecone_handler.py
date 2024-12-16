import time
from pinecone import Pinecone, ServerlessSpec

class PineconeHandler:
    def __init__(self, api_key, index_name, dimension, metric, cloud, region):
        self.api_key = api_key
        self.index_name = index_name
        self.dimension = dimension
        self.metric = metric
        self.cloud = cloud
        self.region = region
        self.pc = Pinecone(api_key=self.api_key)
        self.index = None

    def create_index(self):
        if not self.pc.has_index(self.index_name):
            self.pc.create_index(
                name=self.index_name,
                dimension=self.dimension,
                metric=self.metric,
                spec=ServerlessSpec(
                    cloud=self.cloud,
                    region=self.region
                )
            )
            while not self.pc.describe_index(self.index_name).status['ready']:
                time.sleep(1)
        self.index = self.pc.Index(self.index_name)

    def get_last_id(self):
        # Lista os IDs no índice para encontrar o maior
        last_id = 0
        while True:
            current_id = f"vec{last_id + 1}"
            response = self.index.fetch(ids=[current_id], namespace=self.index_name)
            if not response['vectors']:
                break
            last_id += 1
        return last_id

    def upsert_data(self, data):
        # Obtém o último ID existente no índice
        last_id = self.get_last_id()
        embeddings = self.pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[d['text'] for d in data],
            parameters={"input_type": "passage", "truncate": "END"}
        )

        records = []
        for d, e in zip(data, embeddings):
            last_id += 1  # Incrementa o ID
            record_id = f"vec{last_id}"

            records.append({
                "id": record_id,
                "values": e['values'],
                "metadata": {'text': d['text']}
            })

        self.index.upsert(vectors=records, namespace=self.index_name)

    def query(self, query_text, top_k=3):
        # Converte a consulta em um vetor numérico
        query_embedding = self.pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[query_text],
            parameters={"input_type": "query"}
        )

        # Realiza a busca no índice
        results = self.index.query(
            namespace=self.index_name,
            vector=query_embedding[0].values,
            top_k=top_k,
            include_values=False,
            include_metadata=True
        )

        return results
