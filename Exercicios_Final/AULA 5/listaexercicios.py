
#1
print("EXERCICIO 1")
frutas = ['Abacaxi', 'Banana', 'Morango', 'Pêra', 'Uva']
frutas.append('Kiwi')
print(frutas)

print("=="*15)
#2
print("EXERCICIO 2")
numero = []
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
numero = numero1, numero2, numero3
print(numero)
media = sum(numero) / len(numero)
print("Média:", media)

print("=="*15)
#3
print("EXERCICIO 3")
semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
primeiro = semana[0]
ultimo = semana[-1]

print("Primeiro dia da semana:", primeiro)
print("Último dia da semana:", ultimo)

print("=="*15)
#4
print("EXERCICIO 4")
# Leitura dos números
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
numero4 = int(input('Digite o quarto número: '))

# Armazenar os números em uma tupla
numeros = (numero1, numero2, numero3, numero4)

# Encontrar os pares
pares = tuple(n for n in numeros if n % 2 == 0)

# Verificar se há o número 10
tem_dez = 10 in numeros

# Exibir os resultados
print("Números pares:", pares)
print("Contém o número 10?", "Sim" if tem_dez else "Não")


print("=="*15)
#5
print("EXERCICIO 5")
vogais = {'a', 'e', 'i', 'o', 'u'}
palavra = input("Digite uma palavra: ").lower()

# Verificar as vogais presentes na palavra
vogais_encontradas = {letra for letra in palavra if letra in vogais}

print("Vogais encontradas na palavra:", vogais_encontradas)


print("=="*15)
#6
print("EXERCICIO 6")
# Criando um conjunto vazio
numeros = set()

# Lendo 5 números do usuário e adicionando ao conjunto
numeros.add(float(input('Digite o primeiro número: ')))
numeros.add(float(input('Digite o segundo número: ')))
numeros.add(float(input('Digite o terceiro número: ')))
numeros.add(float(input('Digite o quarto número: ')))
numeros.add(float(input('Digite o quinto número: ')))

# Exibindo os números únicos e a quantidade
print("Números únicos:", numeros)
print("Quantidade de valores únicos:", len(numeros))


print("=="*15)
#7
print("EXERCICIO 7")
usuario = [{
    "Nome": "Tiago","Idade": 20,"Cidade": "São Paulo"
}]
for i in usuario:
    frase = f"{i['Nome']} tem {i['Idade']} anos e mora em {i['Cidade']}."
    print(frase)


print("=="*15)
#8
print("EXERCICIO 8")
# Criando o dicionário com nomes e notas
alunos = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carla": 7.2,
    "Diego": 5.5,
    "Eduarda": 9.0
}

# Mostrando o dicionário completo
print("Dicionário completo de alunos e notas:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")

# Mostrando apenas alunos com nota maior ou igual a 7
print("\nAlunos com nota maior ou igual a 7:")
for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome}: {nota}")


