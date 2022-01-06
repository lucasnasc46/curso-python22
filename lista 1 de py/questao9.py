#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule o seu peso ideal, usando a seguinte fórmula
#(72.7*altura)-58

#definindo o input como float para trabalharmos com casas decimais e salvando na variavel h
h = float(input("Digite a sua altura: "))

peso = (72.7*h)-58 #calculo do peso ideal, resultao salva na variavel peso
 
print("Seu peso ideal é:", peso) #mostrando o resultado na tela
          
