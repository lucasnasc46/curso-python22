#Faça um programa que peça um número e verifique se ele é positivo ou negativo 

#Solicitando ao user um valor + ou - 
valor = int(input("Digite um valor positivo ou negativo "))

#Verificando se o valor é maior que zero, logo sendo positivo
if valor > 0:
    print("O valor", valor, "é positivo")

#Verificando se valor nao for maior que zero, logo ele será negativo
else:
    print("o valor", valor, "é negativo")    