#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

#solicitando ao user a quantidade de numeros do conjunto
n = int(input("Digite a quantidade de numeros do conjunto "))
conjunto=[]
#solicitando os numeros do conjunto e colocando em uma lista
for i in range(n):
    termo = int(input("numero: "))
    conjunto.append(termo)

#Ordenando a lista de forma crescente para pegar o menor e maior valor
conjunto.sort()
print("o menor numero é:", conjunto[0])     #pegando o primeiro e menor item
print("o maior numero é:", conjunto[-1])    #pegando o ultimo e maior numero
print("A soma dos numeros do conjunto é:", sum(conjunto)) #fazendo a soma de todos os itens do conjunto