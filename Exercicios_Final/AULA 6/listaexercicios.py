
#1
print("EXERCICIO 1")
# Criando o dicionário com nomes e notas
def minha_funcao ():
    print('Você Consegue!')
minha_funcao()

print("=="*15)
#2
print("EXERCICIO 2")
def simbolos ():
    print('='*15)
simbolos()

print("=="*15)
#3
print("EXERCICIO 3")
def tabuada_do_5():
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")

# Chamada da função
tabuada_do_5()


print("=="*15)
#4
print("EXERCICIO 4")
def animal_favorito():
    animal = input("Qual é o seu animal favorito? ")
    print(f"Eu também gosto de {animal}!")

# Chamada da função
animal_favorito()


print("=="*15)
#5
print("EXERCICIO 5")
def saudacao():
    hora = int(input("Digite a hora (0 a 23): "))
    if 5 <= hora <= 12:
        print("Bom dia!")
    elif 13 <= hora <= 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")

# Chamada da função
saudacao()


print("=="*15)
#6
print("EXERCICIO 6")
def mostrar_letras():
    palavra = input("Digite uma palavra: ")
    for letra in palavra:
        print(letra)

# Chamada da função
mostrar_letras()


print("=="*15)
#7
print("EXERCICIO 7")
def multiplicar(a, b):
    return a * b

# Chamada da função com entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = multiplicar(num1, num2)
print("Resultado da multiplicação:", resultado)


print("=="*15)
#8
print("EXERCICIO 8")
def maior_numero(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

# Exemplo de uso
numeros = [10, 25, 7, 98, 42]
print("Maior número da lista:", maior_numero(numeros))


print("=="*15)
#9
print("EXERCICIO 9")
def contar_letras(frase):
    contador = 0
    for letra in frase:
        if letra != " ":
            contador += 1
    return contador

# Exemplo de uso
frase = input("Digite uma frase: ")
print("Total de letras (sem espaços):", contar_letras(frase))


print("=="*15)
#10
print("EXERCICIO 10")
def eh_palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

# Exemplo de uso
texto = input("Digite uma palavra: ")
if eh_palindromo(texto):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")



print("=="*15)
#11
print("EXERCICIO 11")
def nome_completo(nome, sobrenome):
    return f"{nome} {sobrenome}"

# Exemplo de uso
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("Nome completo:", nome_completo(nome, sobrenome))


print("=="*15)
#12
print("EXERCICIO 12")
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Exemplo de uso
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = calcular_media(nota1, nota2, nota3)
print("Média:", media)


print("=="*15)
#13
print("EXERCICIO 13")
def celsius_para_fahrenheit(celsius):
    return (celsius * 1.8) + 32

# Exemplo de uso
c = float(input("Temperatura em Celsius: "))
f = celsius_para_fahrenheit(c)
print("Temperatura em Fahrenheit:", f)
