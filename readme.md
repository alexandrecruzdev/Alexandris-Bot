 Chatbot Interativo com Armazenamento de Afirmações

Este projeto implementa um chatbot interativo que aprende e se adapta com base nas interações do usuário. Ele utiliza Groq LLM, Pinecone como banco vetorial para armazenar informações relevantes e Streamlit para a interface.

O chatbot é capaz de identificar afirmações feitas pelo usuário e armazená-las para que, futuramente, o chatbot possa utilizá-las para gerar respostas mais precisas e relevantes.

## Passos para Configuração

### 1. Configuração Inicial

Antes de rodar o sistema, você precisará gerar um arquivo de configuração `.env` onde serão armazenadas as chaves das APIs que o chatbot utiliza. Para fazer isso, execute o seguinte comando:

```bash
py setup.py
pip install -r requirements.txt
streamlit run app.py
```
Isso abrirá uma interface no seu navegador onde você poderá interagir com o chatbot.

### Como Funciona o Armazenamento de Informações
O chatbot identifica palavras-chave nas mensagens enviadas pelo usuário e armazena informações relevantes no banco de dados. Quando o usuário faz uma afirmação, ele usa palavras-chave que indicam que aquela informação é importante o suficiente para ser armazenada.

Palavras-chave para Armazenamento
Abaixo estão as palavras-chave que indicam que o usuário fez uma afirmação importante, que deve ser registrada no banco de dados:

afirmacoes = [
    "valido", "certifico", "ratifico", "reconheço", "comprovo", "autentico",
    "asseguro", "declaro", "estabeleço", "reforço", "corroboro", "digo que sim", 
    "dou certeza", "torno oficial", "declaro verdadeiro", "afirmo", "confirmo"
]
Essas palavras-chave são utilizadas pelo chatbot para identificar quando o usuário está fazendo uma afirmação que deve ser armazenada para futura referência.

### Exemplo de Funcionamento
Se o usuário escrever:
Eu **declaro verdadeiro** que meu nome é João e eu moro no Brasil.
O chatbot identificará a palavra-chave "declaro verdadeiro" e armazenará a informação “Meu nome é João e eu moro no Brasil.” no banco de dados para futuras interações.
https://alexandrisbot.streamlit.app/
