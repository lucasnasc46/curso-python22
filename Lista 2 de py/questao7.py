#Faça um programa que leia 3 números retorne o maior deles

#Solicitando três números o user e salvando nas respectivas variaveis 
n1 = int(input("Digite o primeiro numero "))
n2 = int(input("Digite o segundo numero "))
n3 = int(input("Digite o terceito numero "))

#Faendo a verificação de qual variavel tem o valor maior
if n1 > n2 and n1 > n3:
    print("O maior número é:", n1)

elif n2 > n1 and n2> n3:
    print("O maio número é:", n2)    

else:
    print("O maior número é:", n3)
