

def verificaIdade (idade):
    if(idade>=18):
        return("Você é maior de idade")
    else:
        return("Você é menor de idade")
    

print(verificaIdade(20)) #Quando usar o return precisa tem o print no final para retornar um resultado

verificaIdade(15) #Sem o print não retorna nada

print(verificaIdade(15))
