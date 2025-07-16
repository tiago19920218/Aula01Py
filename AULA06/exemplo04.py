
# Importa a biblioteca para conectar com a internet
import requests
 
nome = input('Digite o seu nome:')

# Define o endereço da API com o nome "lucas"
url = (f"https://api.agify.io?name={nome}")
 
# Faz a requisição e guarda a resposta
resposta = requests.get(url)
 
 
# Converte a resposta para um dicionário
dados = resposta.json()
# Mostra o nome
print(f"Nome: {dados['name']}")
 
# Mostra a idade prevista
print(f"Idade estimada: {dados['age']}")

