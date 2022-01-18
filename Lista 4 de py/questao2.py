# Faça um programa que receba um usuário e senha. Se a senha de entrada
#for igual ao usuário, deverá ser apresentada a mensagem “Senha Inválida”, e
#pedir pro usuário inserir a senha novamente. Quando forem diferentes
#imprimir a mensagem “Senha aceita” e sair do laço while. DICA (Use while
#True e break). Use while.

while True:

    user = input("Digite o usuario: ")
    senha = input("Digite a senha: ")

    if senha == user:
        print("senha ivalida, insira novamente")

    else: 
        print("Senha aceita")
        break