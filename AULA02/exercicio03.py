#Verificar se pode tirar a CNH.

print('PROGRAMA PARA SABER SE PODE TIRAR O CNH')
nome = input('Digite o seu nome:')
idade = int(input('Digite a sua idade:'))
if (idade >= 18):
    print(f'{nome} você pode tirar a CNH')
else:
    print(f'{nome}, você ainda não tem idade minima permitida')
   