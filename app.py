import streamlit as st
from dotenv import load_dotenv
import os
from chatbot import Chatbot  # Importe o chatbot adaptativo
from pinecone_handler import PineconeHandler
# Inicializar chatbot
load_dotenv()
chatbot = Chatbot()
api_key_pinecone = os.getenv('PINECONE_API_KEY')

pch = PineconeHandler(
        api_key=api_key_pinecone,
        index_name="quickstart",
        dimension=1024,
        metric="cosine",
        cloud="aws",
        region="us-east-1"
    )

# Cria o índice
pch.create_index()

# Verifica o último ID
last_id = pch.get_last_id()


# Configuração da interface
st.set_page_config(page_title="Alexandris Robot", layout="centered")
st.title("Alexandris Robot")

# Estado de conversa
if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

# Campo de entrada do usuário
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Digite sua pergunta:")
    afirmacoes =  [
    "valido", "certifico", "ratifico", "reconheço", "comprovo", "autentico",
    "asseguro", "declaro", "estabeleço", "reforço", "corroboro","digo que sim", "dou certeza", "torno oficial", "declaro verdadeiro","afirmo","confirmo"]
    for palavra in afirmacoes:
        if palavra in user_input:
            pch.upsert_data([{"text":user_input}])
    submit_button = st.form_submit_button("Enviar")

# Processar entrada e exibir conversa
if submit_button and user_input:
    # Obter resposta do chatbot
    contexto = pch.query(user_input,3)
    print(contexto)
    question = f"{user_input} responda com o auxilio do historico da nossa conversa:{st.session_state["conversation"]} e do nosso contexto:{contexto} mas não mencione-os na conversa."
    response = chatbot.get_response(question)
    
    # Atualizar histórico da conversa
    st.session_state["conversation"].append({"role": "user", "content": user_input})
    st.session_state["conversation"].append({"role": "bot", "content": response})

# Exibir conversa
for msg in st.session_state["conversation"]:
    if msg["role"] == "user":
        st.write(f"**Você:** {msg['content']}")
    else:
        st.write(f"**Chatbot:** {msg['content']}")
