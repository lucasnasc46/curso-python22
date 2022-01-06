#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius

#Definindo o input como float para trabalhar casas decimais e solicitando ao usuario a temperatura
f = float(input("Digite graus Fahrenheit: "))

c = 5*((f-32)/9) #calculando a conversao e salvando na variavel c, os parenteses sao extremos importantes por conta da notação matematica 

print(f,"Fahrenheit é",c ,"Celsius") #mostrando na tela o resultado, lembrando que o que esta fora das "" é o resultaod salvo nas variaiveis 
