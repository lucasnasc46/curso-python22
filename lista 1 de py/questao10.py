#tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas
#para homens: (72.7*h)-58
#para mulheres (62.1*h)-44.7

#definindo o input como float para trabalharmos com casas decimais e salvando na variavel h
h = float(input("Digite a sua altura: "))

pesoh = (72.7*h)-58 #calculo do peso ideal para homens, resultao salva na variavel pesoh
pesom = (62.1*h)-44.7 #calculo do peso ideal para homens, resultao salva na variavel pesom
print("Se for homem, o peso ideal é:", pesoh) #mostrando o resultado na tela para homens
print("Se for mulher, o peso ideal é:", pesom) #mostrando o resultado na tela para mulheres
