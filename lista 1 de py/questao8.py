#Faça um programa que peça 2 numeros inteiros  um real. Calcule e mostre
# 1 - o produto do dobro do primeiro com metado do segundo
# 2 - soma do triplo do primeiro com o terceiro
# 3 - terceiro elevado ao cubo


num1 = int(input("Digite o primeiro número inteiro ")) #Solicitando o 1 numero do tipo int
num2 = int(input("Digite o segundo número inteiro ")) #Solicinando o 2 numero do tipo int
num3 = float(input("Digite o terceiro número real ")) #Solcitando o 3 numero do tipo float

a = (num1*2)*(num2/2) #salvando a 1 operaçao solicitada na variavel a
b = (num1*3)+ num3    #salvando a 2 operação soliciada na variavel b
c = num3**3           #salvando a 3 operação na variavel c, ** é o operador para potencia no Py

print("o produto do dobro do primeiro com metado do segundo. é: ", a) #mostrando o resultado da 1 operação 
print("soma do triplo do primeiro com o terceiro, é: ", b) #mostrando o resultaod da 2 operação
print("terceiro elevado ao cubo, é: ", c)  #mostrando o resultado da 3 operação
