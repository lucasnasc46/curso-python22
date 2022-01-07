#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#Solcitando ao user o valor de cada produto
prod1 = float(input("Digite o preço do produto 1 "))
prod2 = float(input("Digite o preço do produto 2 "))
prod3 = float(input("Digite o preço do produto 3 "))

#Fazendo a verificação de qual tem o menor preço e retornando qual deve comprar
if prod1 < prod2 and prod1 < prod3:
    print ("Você deve comprar o produto 1")

elif prod2 < prod1 and prod2 < prod3:
    print ("Você deve comprar o produto 2")

else:
    print ("Você deve comprar o produto 3")       