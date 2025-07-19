
#1
print("EXERCICIO 1")
numero = float(input('Digite um número: '))

if numero > 0:
    print('Positivo')
elif numero == 0:
    print('O número é zero')
else:
    print('Negativo')


print("=="*15)
#2
print("EXERCICIO 2")
temperatura = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = temperatura * 9 / 5 + 32
print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
if temperatura < 0:
    print("Está congelando!")
elif 0 <= temperatura <= 25:
    print("Temperatura amena")
else:
    print("Está quente!")

print("=="*15)
#3
print("EXERCICIO 3")
letra = input("Digite uma letra: ").lower()

# Verifica se é uma letra do alfabeto
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, digite apenas uma letra do alfabeto.")
elif letra in 'aeiou':
    print("É uma vogal.")
else:
    print("É uma consoante.")


print("=="*15)
#4
print("EXERCICIO 4")
numero = int(input('Digite um número de 1 a 7:'))
if(numero == 1):
    print('Segunda-feira')
elif(numero == 2):
    print('Terça-feira')
elif(numero == 3):
    print('Quarta-feira')
elif(numero == 4):
    print('Quinta-feira')
elif(numero == 5):
    print('Sexta-feira')
elif(numero == 6):
    print('Sábado')
elif(numero == 7):
    print('Domingo')
else:
    print('Número inválido')
          

print("=="*15)
#5
print("EXERCICIO 5")
nota = float(input('Digite uma nota de 0 a 10: '))
if(nota<5):
    print('Reprovado')
elif(nota>= 5 and nota<=6.9):
    print('Recuperação')
else:
    print('Aprovado')

print("=="*15)
#6
print("EXERCICIO 6")
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"O maior número é {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"O maior número é {numero2}")
else:
    print(f"O maior número é {numero3}")


print("=="*15)
#7
print("EXERCICIO 7")
# Solicita os três lados do triângulo
a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

# Verifica se é um triângulo válido
if a + b > c and a + c > b and b + c > a:
    # Verifica o tipo de triângulo
    if a == b == c:
        print("Triângulo Equilátero: todos os lados são iguais.")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles: dois lados são iguais.")
    else:
        print("Triângulo Escaleno: todos os lados são diferentes.")
else:
    print("Os valores informados não formam um triângulo.")


print("=="*15)
#8
print("EXERCICIO 8")
numero = int(input("Digite um número de 1 a 12: "))
if(numero == 1):
    print("Janeiro")
elif(numero == 2):
    print('Fevereiro')
elif(numero == 3):
    print('Março')
elif(numero == 4):
    print('Abril')
elif(numero == 5):
    print('Maio')
elif(numero == 6):
    print('Junho')
elif(numero == 7):
    print('Julho')
elif(numero == 8):
    print('Agosto')
elif(numero == 9):
    print('Setembro')
elif(numero == 10):
    print('Outubro')
elif(numero == 11):
    print('Novembro')
elif(numero == 12):
    print('Dezembro')
else:
    print('Número inválido')


print("=="*15)
#9
print("EXERCICIO 9")
letra = input('Digite uma letra ou caracter especial: ')
if len(letra) == 1 and letra.isalpha():
    if letra.isupper():
        print("A letra é MAIÚSCULA.")
    elif letra.islower():
        print("A letra é minúscula.")
else:
    print("É um caracter especial")

print("=="*15)
#10
print("EXERCICIO 10")
horas_trabalhadas = float(input("Digite a suas horas trabalhadas: "))
valor_hora = float(input('Digite o valor das horas trabalhadas: '))
salario = horas_trabalhadas*valor_hora*30
if(salario == 1000):
    print('Salário baixo')
elif(salario>= 1001 and salario <= 3000):
    print('Salário Médio')
else:
    print('Salário Alto')