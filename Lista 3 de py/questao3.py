# Faça um Programa que leia N (peça pro usuário informar o valor de N) notas e insira em uma lista, depois percorra a lista e calcule a soma das notas, por fim calcule a média (soma dividido por N) e mostre na tela

#Solicitando ao usuário a quantidade de notas
n = int(input("Digite quantas notas vc quer calular a media: "))

#deifindo a lista fazia para que no for ela seja preenchida com as notas informadas
lista = []

# fazendo o laço para pegar a quantidade de notas informada pelo o user
for x in range (n):
    nota = float(input(f"Digete a nota {x + 1}:"))  #Solicitado a nota ao user  
    lista.append(nota)                              #Adcionando a nota informada na lista

#somando os valores da lista usadno a função sum
soma = sum(lista)
print("a media é:", soma/n)           # printando na tela a media das notas
