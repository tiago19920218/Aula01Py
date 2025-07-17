#1
print("EXERCICIO 1")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = numero1+numero2
print(f'O resultado da soma de {numero1} + {numero2} = {resultado}')

print("=="*15)

#2
print("EXERCICIO 2")
valor = float(input('Digite o valor do produto:'))
desconto = valor *0.10
resultado = valor - desconto
print(valor-desconto)

print("=="*15)

print("EXERCICIO 3")
numero1 = float(input('Digite um número:'))
numero2 = float(input('Digite um número:'))
resultado = numero1/numero2
restodivisao = numero1%numero2
print(numero1/numero2)

print("=="*15)

print("EXERCICIO 4")

numero = int(input('Digite um numero:'))
expoente = int(input('Digite o expoente:'))
potencia = numero**expoente
print(potencia)

print("=="*15)

print("EXERCICIO 5")
temperatura = float(input('Digite a temperatura em graus Celsius:'))
fahrenheit = temperatura * 9 / 5 + 32
print(fahrenheit)

print("=="*15)

print("EXERCICIO 6")
idade = int(input('Digite a sua idade:'))
if (idade>18):
    print('Você é de maior')
else:
    print('Você é de menor')

print("=="*15)

print("EXERCICIO 7")
numero1 = float(input('Digite a sua senha:'))
if (numero1 == 18052007):
    print('Login efetuado com sucesso')
else:
    print('A senha está incorreta')

print("=="*15)

print("EXERCICIO 8")
numero = int(input('Digite um numero para verificar se é impar ou par:'))
par = numero%2

if (par == 0):
    print('É par')
else:
    print('É impar')

print("=="*15)

print("EXERCICIO 9")
idade = int(input('Digite a sua idade:'))
if (16<= idade <=65):
    print('Você pode entrar no evento')
else:
    print('Você não pode entrar no evento')

print("=="*15)

print("EXERCICIO 10")
idade = float(input('Digite a sua idade:'))
if (idade <= 12):
    print('O seu ingresso é gratuito')
else:
    print('O seu ingresso não é gratuito')

print("=="*15)

print("EXERCICIO 11")
nome = input('Digite o seu nome:')
voto = int(input('Digite o número da sua votação:'))
if (voto == 1):
    print(f'{nome} você votou em BRANCO')
elif (voto == 2):
    print(f'{nome} você votou em VERDE')
elif (voto == 3):
    print(f'{nome} você votou em VERMELHO')
else:
    print('Votou Errado')
print('Obrigado pelo o seu voto!')

print("=="*15)

print("EXERCICIO 12")
nome = input('Digite o seu nome:')
idade = int(input('Digite a sua idade:'))
if (idade >= 18):
    print(f'{nome} você pode tirar a CNH')
else:
    print(f'{nome}, você ainda não tem idade minima permitida')

print("=="*15)

print("EXERCICIO 13")
nota = float(input('Digite sua nota:'))
if(nota>=7):
    print("Aprovado")
elif(nota>=5 and nota<=6.9):
    print("Recuperação")
else:
    print("Reprovado")

print("=="*15)

print("EXERCICIO 14")
numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))
if(numero1> numero2):
    print(f"O maior numero é {numero1}")
elif(numero1 == 0 and numero2 ==0):
    print("Você digitou dois numeros 0")
else:
    print(f"O maior numero é {numero2}")

print("=="*15)

print("EXERCICIO 15")
peso = float(input("Digite o seu peso em Kg:"))
altura = float(input("Digite a sua altura:"))
imc = peso/ (altura**2)
if(imc<18):
    print("Está abaixo do peso")
elif (imc>18.5 and imc == 24.9):
    print("Você está no peso ideal")
elif(imc ==25):
    print("Você está sobre o peso")
else:
    print("Você está obeso")