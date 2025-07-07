#Verificação entrada no evento

idade = float(input('Digite a sua idade:'))
if (idade >= 18):
    print('Você pode entrar no evento')
elif (idade <= 65):
    print('Você pode entrar no evento')
else:
    print('Você não pode entrar no evento')