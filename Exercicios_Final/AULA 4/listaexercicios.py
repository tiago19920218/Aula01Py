
#1
print("EXERCICIO 1")
palavra = input("Digite uma palavra: ")

for letra in palavra:
    print(letra)


print("=="*15)
#2
print("EXERCICIO 2")
numero = int(input('Digite um número: '))

for i in range(1, numero):
    print(i)


print("=="*15)
#3
print("EXERCICIO 3")
cidades = ['São Paulo', 'Osasco', 'Rio de Janeiro', 'Maceió']

for nome in cidades:
    print(f"{nome} é uma cidade brasileira")

print("=="*15)
#4
print("EXERCICIO 4")
numero = int(input('Digite um número: '))

print(f"Números entre 1 e {numero} que são divisíveis por 7:")

for i in range(1, numero + 1):
    if i % 7 == 0:
        print(i)


print("=="*15)
#5
print("EXERCICIO 5")
contador = 0  # contador para números pares

print("Números pares de 0 a 20:")

for i in range(0, 21):
    if i % 2 == 0:
        print(i)
        contador += 1  # incrementa o contador

print(f"\nTotal de números pares exibidos: {contador}")


print("=="*15)
#6
print("EXERCICIO 6")
palavras = []  # lista para armazenar as palavras

palavra = input("Digite uma palavra (ou 'fim' para encerrar): ")

while palavra.lower() != "fim":
    palavras.append(palavra)  # adiciona à lista
    palavra = input("Digite outra palavra (ou 'fim' para encerrar): ")

print("\nPalavras digitadas:")
for p in palavras:
    print(p)


print("=="*15)
#7
print("EXERCICIO 7")
contador = 1
soma = 0

while contador <= 50:
    soma += contador
    contador += 1

print(f"A soma de todos os números de 1 até 50 é: {soma}")


print("=="*15)
#8
print("EXERCICIO 8")
senha = input('Digite a sua senha: ')
while senha != "liberar123":
    print('Senha errada')
    senha = input('Tente Novamente: ')
print('Bem-vindo!')

print("=="*15)
#9
print("EXERCICIO 9")
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

print(f"\nContando de {inicio} até {fim}, de 2 em 2:")

while inicio <= fim:
    print(inicio)
    inicio += 2

print("=="*15)
#10
print("EXERCICIO 10")
contador = 0

while True:
    fruta = input("Digite o nome de uma fruta: ")
    
    if len(fruta) > 10:
        print("\nFruta com mais de 10 letras! Encerrando...")
        break
    
    contador += 1

print(f"\nTotal de frutas inseridas: {contador}")
