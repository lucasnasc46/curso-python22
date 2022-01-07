#Faça um programa que peça um número inteiro e determine se ele é par ou impar

#Solicitando ao user um numero do tipo inteiro e salvando na variavel num
num = int(input("Digite um número inteiro "))

#Verificando o resto da divisão com o operador %, se for igual a zero é pq é par
if num % 2 == 0:
    print("o numero é par")

else:
    print("o número é impar")    