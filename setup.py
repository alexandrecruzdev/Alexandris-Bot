import getpass
import os

# Solicita a chave de API de forma oculta
api_key_pinecone = getpass.getpass("Digite sua chave de API PICONE: ")
api_key_groq = getpass.getpass("Digite sua chave de API GROQ: ")

variaveis = f"""
    GROQ_API_KEY={api_key_groq}
    PINECONE_API_KEY={api_key_pinecone}
    """

with open(".env", "w") as arquivo:
    arquivo.write(variaveis)
    print(".env criado com sucesso!")
