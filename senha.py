# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


while True:

    nome = input("Digite a o seu nome: ")
    senha = input("Digite a sua senha: ")

    if nome != senha:
        print("login efetuado")
        break
    else:
        print("ERRO!! Nome e senha iguais tente novamente")
