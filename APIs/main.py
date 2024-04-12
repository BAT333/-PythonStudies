import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
#vc pode colocar oq seu site vai retornar se é get, post, etc
response = requests.get(url)

print(response)
# se retonar 200 sua url esta ok
# se retorna outro numero tem algum erro na sua url ou no site

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

print(dados_restaurante['McDonald’s'])


#status_code PARA PEGAR OS STATUS PARA VER QUE DEU TUDO CERTO
#dados_json = response.json() = para pegar infos do json


for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)
