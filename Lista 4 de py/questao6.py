#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

i = 1               #definindo o contador do laço como 1
par = 0             #definindo um contador para contar numeros pares
impar = 0           #definindo um contador para contar numeros impares

#laço para ler 10 numeros
while i <= 10:
    n = int(input(f"Digite o {i}º numero: "))

    if n % 2 == 0:  #se o numero for para ele incrementa 1 no contador par
        par +=1

    else:
        impar +=1   #se o numero for impar ele incrementa 1 no contador impar
    
    i += 1

#printando o valor total dos contadores de par e impar
print(f"{par} numeros pares e {impar} numeros impares")

   