#Fala um programa para verificar se uma letra do alfabeto é uma vogal ou uma consoante

#Solicitando ao user que digite uma vogal
letra = input("Digite uma letra ")

#Verificando se a letra digitada é uma vogal e mostrando na tela
if letra in ("a", "e", "i", "o","u"):
    print(letra, "é uma vogal")

else:
    print(letra, "é uma consoante")

        