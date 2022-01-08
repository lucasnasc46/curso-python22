#Escrever um programa em linguagem Python que lê um valor i, inteiro e positivo e 3 valores a, b e c. Se o valor de i é par então calcular e imprimir na tela a média aritmética de a, b e c. Caso contrário, se i>10 então calcular e imprimir na tela a média aritmética e ponderada de a, b e c. Os pesos dos valores são respectivamente 2, 3 e 4.

#importando a função sys para usar para finalizar o programa caso o user coloque o valor negativo
import sys;

#Solicitando ao user o valor de i
i = float(input("Digite o valor de i "))

#Verificando se o valor de i é maior que 0, ou seja, positivo
#Se for negativo, a função sys irá finalizar o programa
if i <= 0:
    print("Coloque um valor positivo e inteiro")
    sys.exit();

#Se o valor for positivo, será solicitado os valores de a,b e c
if i > 0:
    a = int(input("Digite o valor de a "))
    b = int(input("Digite o valor de b "))
    c = int(input("Digite o valor de c "))

#Dentro o if de verificação se o valor de i é maior q zero, verifico se o i é par e se o i é maior que 10
#Após a verificar faz os calculos de acordo com o valor de i
    if i % 2 == 0:
        med_ari = (a+b+c)/3
        print("A média aritimetrica é:", med_ari)

    if i>10:
        med_pond = (2*a + 3*b + 4*c)/9
        print("A média ponderada é:", med_pond)    

    
