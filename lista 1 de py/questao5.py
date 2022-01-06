# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

#Solicitando o valor do lado para calcular a area, definindo input como float para trabalhar com valores decimais 
lado = float(input("digite o valor do lado do quadrado "))

area = lado**2 #fazendo a formula da area do quadrado, o ** é o operador para potencia no python

print("O dobro da area é:", area*2) #area é a variavel onde foi salva o resultao do calculo acima, onde multiplicamos por 2 e msotramos o resultado na tela
