#faça um programa que peça dois números e imprima o maior deles

#Solcitando ao user dois numeros e salvando nas variaveis num1 e num2
num1 = int(input("Digite um número "))
num2 = int(input("Digite outro número "))

#Fazendo a condição para verficicar se o 1 num é maior que o 2
if num1 > num2:
    print("o número", num1, "é maior que o", num2)

#Fazendo a condição para verficar se o 2 num é maior que o 1
else:
    print("o número", num2, "é maoir que", num1)

