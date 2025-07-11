
#Resultado para saber se o numero é par ou impar

def imparPar (numero):
    resultado = numero%2
    if (resultado == 0):
        print("O numero é par")

    else:
        print("O numero é impar")

numero = int(input("Digite um numero: "))
imparPar(numero)

print("=="*15)

#Calcular a media de 3 notas

def media (numero1, numero2, numero3):
    resultado = (numero1+numero2+numero3)/3
    print(resultado)

numero1 = float(input("Digite uma nota: "))
numero2 = float(input("Digite outra nota: "))
numero3 = float(input("Digite outra nota: "))
media(numero1, numero2, numero3)
