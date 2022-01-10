#Crie um programa que tenha uma lista de 5 frutas, e depois adicione uma nova fruta no final da lista. Depois remova o primeiro elemento da lista e por fim, altere o valor do item 2 pra "banana"

#Criando lista de frutas
fruta = ["uva", "melao", "manga", "maca", "abacaxi"]

#Adcionando kiwi no final da lista
fruta.append ("kiwi")
print(fruta)

#removendo o 1 item da lista
fruta.pop(0)
print(fruta)

#trocando o segundo elemento da lista para banana
fruta [1] = ("banana")
print(fruta)

#Fazendoi lista de lista de pessoas
pessoas = [["lucas", 27, "m", 1995], ["jana", 26, "f", 1996], ["debora", 25, "f", 1997], ["marcos", 73, "m", 1949]]
print(pessoas)