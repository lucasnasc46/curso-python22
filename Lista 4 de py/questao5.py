# Faça um programa que lê um número inteiro n. E verifique se n é um número par, se não for pedir para inserir outro número até que seja par. Use while.

#usando um laço infinito para o programa continuar executando
while True:

    n = int(input("Digite um número: "))  #para While com true, usar o print dentro do laço

    if n % 2 != 0:                        #Se o numero digitado seja impar o programa continua executando (True)
        print("Digite um numero par")

    else:                                 #se o número for par entra o break e o programa para a execução
        break
