#Calculo IMC

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