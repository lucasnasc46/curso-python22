#Faça um programa que leia números reais. Quando o número digitado for o número zero o programa deverá apresentar uma lista com todos os números que foram digitados e sair do laço while.Use while.

#definindo uma lista para guardar os numeros
lista = []

#fazendo um laço infinto para a condição
while True:
    num = float(input("Digite o numero: "))
    
    #enquanto o numero digitado seja diferente de zero ele salva o numero na lista
    if num != 0:
        lista.append(num)

    #quando o numero for o 0, ele printa a lista com todos o numeros digitados      
    else:
        print(lista)

    