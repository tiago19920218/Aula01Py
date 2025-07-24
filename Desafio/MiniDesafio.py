
#Cadastre usuários com nome e senha.
#Permita fazer login com nome e senha.
#Mostre uma mensagem de boas-vindas se o login for bem-sucedido. 
#Menu com opções: 1. Cadastrar, 2. Login, 3. Sair
#Verificar se o nome já existe ao cadastrar
#Verificar se a senha está correta ao fazer log

print("CADASTRO DE USUÁRIOS")

usuario = input("Digite o seu nome: ")
senha = input("Digite a sua senha: ")

while usuario != "Tiago" and senha != "18052027":
    print("Login incorreto")
    usuario = input("Tente novamente o usuário: ")
    senha = input("Tente novamente a sua senha: ")
    
print("Seja Bem-Vindo!")

