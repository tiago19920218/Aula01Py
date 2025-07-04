#Verificar se o número é impar ou par

numero = int(input('Digite um numero para verificar se é impar ou par:'))
par = numero%2

if (par == 0):
    print('É par')
else:
    print('É impar')