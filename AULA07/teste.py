
def unicos(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(lista)
    return nova_lista
print(unicos([1, 2, 2, 3, 4, 4]))


