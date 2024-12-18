import requests
import json
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

url = "https://api.openai.com/v1/chat/completions"

# Obtém a API key das variáveis de ambiente
openai_api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual é a capital da França?"}]
}

try:
    # Faz a requisição para a API
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Para debug - mostra a resposta completa
    print("Resposta completa:", response.text)
    
    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        response_data = response.json()
        print(response_data["choices"][0]["message"]["content"])
    else:
        print(f"Erro: {response.status_code}")
        print(f"Mensagem: {response.text}")
        
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")