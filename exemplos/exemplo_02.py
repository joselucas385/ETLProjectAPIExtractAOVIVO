import requests

url = 'https://jsonplaceholder.typicode.com/comments'
parametros = {'postid': 1} #obter o post com id 1
resposta = requests.get(url, params=parametros)
dados = resposta.json()

comentarios = resposta.json()
print(f'Total de comentários: {len(comentarios)}')
print(f"Erro: {resposta.status_code} - {resposta.text}")












