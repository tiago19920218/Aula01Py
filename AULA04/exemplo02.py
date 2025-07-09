cliente = {"nome": "Pascoal", "numero_telefone": 11945652325, "idade": 25, "cpf": 12345678933, "endereço": "Avenida Paulista, 1236"}
print(cliente)
print(len(cliente)) #exibir a quantidade de dados dentro do dicionário
print(cliente["endereço"]) #exibir o endereço
del cliente["nome"] #deleter uma informação do dicionário
print(cliente)
print(len(cliente))
cliente["nome"] = "Tiago"
print(cliente)
print(len(cliente))