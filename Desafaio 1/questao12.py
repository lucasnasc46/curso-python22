#Faça um programa para calcular o fatorial de qualquer número]

#definindo a varaivel fat como 1 e solicitando ao user um numeor para calculo e salvando na variavel n
fat = 1
n = int(input("Digite um numero para calcular o seu fatoria "))

#Verificando se o numero é negatio
if n < 0:
    print("Nao existe fatorial de numero negatico")

#Verificando se o numeor é zero
elif n == 0:
    print("O faltorial de 0 é 1")

#Se ele for um numero positivo é feito o calculo fatorial
else:

#fazendo um for para fazer a multiplicação dos numeros anterioes ao valor digitado 
    for i in range(1, n+1):
        fat = fat * i 

    print("o fatorial de", n, "é", fat)
