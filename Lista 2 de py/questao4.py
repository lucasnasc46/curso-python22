#Faça um Programa que verifique se uma letra digitada é "F" ou "M".Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#Solcitando ao user q digite as siglas para seu sexo. Não precisa definir o tipo do input, pois por padrão é str
sexo = input("Digite M se for homem ou F se for mulher ")

#Verificando se a sigla digitada é maisculo ou minuscolo para retornar o sexo selecionado
if sexo == "M" or sexo =="m":
    print("Masculino")

elif sexo == "F" or sexo == "f":
    print("Feminino")

else:
    print("sexo invalido")        