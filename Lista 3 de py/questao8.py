# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.(Use range de intervalos (range(x, y)))

#solicitando dois numeros ao user e salvando nas respectivos variaveis 
n1 = int(input("Digeite um número: "))
n2 = int(input("Digite outro número: "))

#usando a funcao range para printar todos os numeros no intervelo
for i in range(n1,n2+1):
    print(i)