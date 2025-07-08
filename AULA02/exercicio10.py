#Comparar valores ou se são iguais

numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))
if(numero1> numero2):
    print(f"O maior numero é {numero1}")
elif(numero1 == 0 and numero2 ==0):
    print("Você digitou dois numeros 0")
else:
    print(f"O maior numero é {numero2}")