#Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro

#Solicitando o número ao usuário e o salvando na variavel num
num = int(input("Digite um número inteiro "))

if num < 0:
     print("O número é negativo")

elif num == 0:
    print("O número é neutro")

else:
    print("O número é positivo")
