numeros = []

# Loop while para coletar os números
while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")
    if entrada.lower() == "sair":
        break
    if entrada.isdigit():
        numeros.append(int(entrada))
    else:
        print("Por favor, digite um número válido ou 'sair'.")

# Exibir apenas os números pares usando for
print("\nNúmeros pares digitados:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
