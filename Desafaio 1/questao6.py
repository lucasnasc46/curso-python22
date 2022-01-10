#Escreva um programa para ler um número inteiro e informar se ele é divisivel por 5

#Pedindo ao user que coloque um númemro
num = int(input("Digite um  número inteiro "))

#Verificando se o numero digitado é divisel por 5 usando o operador % de resto
if num %5 == 0:
    print(num," é divisível por 5")

else:
    print(num, "não é divisível por 5")    