from dotenv import load_dotenv
import os
from groq import Groq
from pinecone_handler import Pinecone

class Chatbot:
    def __init__(self, api_key: str = None):
        # Carrega variáveis do .env se o api_key não for passado
        if api_key is None:
            load_dotenv()
            api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError("A API Key da Groq não foi fornecida ou carregada.")
        
        self.client = Groq(api_key=api_key)
    
    def get_response(self, question: str, model: str = "llama3-8b-8192") -> str:
        """Recebe uma pergunta e retorna uma resposta usando a API da Groq."""
        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": question}],
                model=model,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao obter resposta: {str(e)}"


