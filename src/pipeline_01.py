#Inserir ROBO PARA RODAR DE TANTOS EM TANTOS SEGUNDOS EM UM LOOP

#Extrair dados da API do Bitcoin
from pprint import pprint
import requests
from tinydb import TinyDB
from datetime import datetime
import time

# Função para extrair dados da API do Bitcoin
def extrair_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    data = response.json() #Pega somente os dados que importam em JSON
    return data

#Agora vamos transformar esses dados que o código extraiu.
def transformar_dados_bitcoin(data):
    #Vamos pegar cada valor da API e chamar de outro nome, para que seja mais fácil de entender.
    valor = data['data']['amount']
    cripto = data['data']['base']
    moeda = data['data']['currency']
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    #Salva tudo isso dentro de uma chave de dicionário.
    dados_transformados = {
        'Valor': valor,
        'Cripto': cripto,
        'Moeda': moeda,
        'Data/Hora':timestamp
    }

    return dados_transformados

#Função para salvar os dados transformados no banco NOSQL no TinyDB
def salvar_dados_tinydb(dados, db_name="bitcoin.json"): #cria um arquivo localmente chamado bitcoin.json
    db = TinyDB(db_name)
    db.insert(dados)
    print(f"Dados salvos com sucesso no banco de dados {db_name}")

#print(extrair_dados_bitcoin()['data']) #Parseia os dados para pegar o valor do Bitcoin em USD
# Usaria print para exibir os dados em uma única linha, o que pode ser menos legível para estruturas complexas.

#pprint(extrair_dados_bitcoin()['data'])
# Usamos pprint para exibir os dados de forma mais legível, com formatação que inclui quebras de linha e indentação.
# Isso é especialmente útil para visualizar estruturas de dados complexas.

#Esse if name main só roda as linhas abaixo se o código acima for rodado diretamente.
if __name__ == "__main__":
    #Loop infinito para rodar o código a cada 15 segundos
    while True:
        dados_bitcoin = extrair_dados_bitcoin()
        dados_transformados = transformar_dados_bitcoin(dados_bitcoin)
        salvar_dados_tinydb(dados_transformados)
        time.sleep(15)


