# 1 = branco
# 2 = verde
# 3 = vermelho

print('Vamos votar num time (1-Branco), (2-Verde) e (3-Vermelho)')
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