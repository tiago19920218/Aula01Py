
#Soma de número

def soma (numero1, numero2):
    soma = numero1+numero2
    print(soma)

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))
soma(numero1, numero2)

#Soma com o return

def soma (numero3, numero4):
    return numero3+numero4

numero3 = float(input("Digite um numero: "))
numero4 = float(input("Digite um numero: "))
resultado = soma(numero3, numero4)
print(resultado)
