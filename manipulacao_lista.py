# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista_num = [1, 3, 4, 2, 9]

lista_num.sort()

for i in lista_num:
    sum = lista_num[-1] + lista_num[0]

print("lista ordenada", lista_num)
print("maior numero", lista_num[0])
print("mennor numeor", lista_num[-1])
print("soma:", sum)
