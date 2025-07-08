#Adicionando Kiwi dentro de uma tupla
frutas = ("Banana", "Maça", "Kiwi")
listfrutas = list(frutas)
listfrutas.append("laranja")
listfrutas.insert(0 , "Kiwi")
frutas = tuple(listfrutas)
print(frutas)

#Adicionado o numero 4 na posição 1
tuplaNumero = (0, 1, 2, 3)
listaNumero = list(tuplaNumero)
listaNumero.append(5) #adicionar um numero
listaNumero.insert(1, 4) #inserir um numero numa determinada posição
listaNumero.pop(2) #remover um numero
tuplaNumero = tuple(listaNumero)
print(tuplaNumero)


