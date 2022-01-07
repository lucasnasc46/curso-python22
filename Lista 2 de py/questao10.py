#Faça um programa que lê três números e retorne eles de forma decrescente

#Solicitando 3 numeros ao user e salvando nas respectivas variaveis
n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digete o segundo número "))
n3 = int(input("Digite o terceiro número "))

#Verificando os tamanhos dos números salvos nas variaveis e ordenando de forma descrecente 
if n1 < n2 and n2 < n3:
    print("a ordem descrecente e:", n3, n2, n1)

elif n2 < n1 and n1 < n3:
    print("a ordem descrecente e:", n3, n1, n2)

elif n1 < n2 and n3 < n2 and n3 < n1:
    print("a ordem descrecente e:", n2, n1, n3)

elif n1 < n2 and n3 < n2 and n1 < n3:
    print("a ordem descrecente e:", n2, n3, n1)   

elif n2 < n1 and n3 < n1 and n3 < n2:
    print("a ordem descrecente e:", n1, n2, n3) 

elif n2 < n1 and n3 < n1 and n2 < n3:
    print("a ordem descrecente e:", n1, n3, n2)        
