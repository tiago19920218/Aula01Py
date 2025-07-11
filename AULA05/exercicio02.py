#Contagem do 0 ao 10
def contagem():
    for i in range(11):
        print(i)

contagem()

print("="*15) #separar os resultados

#1 ao 10 pulando de 2 em 2
def pulando():
    for contador in range(0, 11, 2):
        print(contador)

pulando() 

print("="*15) #separar os resultados

#Boa noite para uma lista de alunos
nomes = ["Paulo", "Tiago", "Lucas", "Rafael"]
def saudacao():
    for i in nomes:
        print(f"Boa noite {i}")

saudacao()