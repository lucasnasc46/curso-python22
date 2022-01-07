#Faça um programa que leia 3 números retorne o maior e o menor deles

#Solicitando três números o user e salvando nas respectivas variaveis 
n1 = int(input("Digite o primeiro numero "))
n2 = int(input("Digite o segundo numero "))
n3 = int(input("Digite o terceito numero "))

#Faendo a verificação de qual variavel tem o valor maior e o menor
if n1 > n2 and n1 > n3 and n2 < n1 and n2 < n3:
    print("O maior número é:", n1)
    print("o menor número é:", n2)

if n1 > n2 and n1 > n3 and n3 < n1 and n3 < n1:
    print("O maior número é:", n1)
    print("o menor número é:", n3)    

elif n2 > n1 and n2> n3 and n1 < n2 and n1 < n3:
    print("O maior número é:", n2)    
    print("O menor número é:", n1)

elif n2 > n1 and n2> n3 and n3 < n1 and n3 < n2:
    print("O maior número é:", n2)    
    print("O menor número é:", n3)

elif n3 > n1 and n3 > n2 and n1 < n2 and n1< n3:
    print("O maior número é:", n3)
    print("O menor número é:", n1)

elif n3 > n1 and n3 > n2 and n2 < n1 and n2 < n3:
    print("O maior número é:", n3)
    print("O menor número é:", n2)
