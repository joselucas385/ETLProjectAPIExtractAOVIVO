import requests

url = 'https://jsonplaceholder.typicode.com/posts/1#'
resposta = requests.get(url)
dados = resposta.json()

print(dados)
#Mesma informação que quando acessamos a url pelo navegador, mas agora em formato de dicionário.










