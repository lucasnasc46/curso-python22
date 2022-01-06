# Faça um programa que converta metro em centímetros

#Solicitando ao usuario o valor em metros para a conversão e definindo o input como float pois precisamos trabalhar com casas decimais
metro = float(input("Digite quantos metros deseja converter para centimetros "))

cm = metro/0.01 #calculo da converção e salvando o resultao na variavel cm

print(metro,"m em centimetros é:", cm,"cm") #printando na tela, lembrando que o que está fora das "" são os valores salvos nas variaveis, oq estiver dentro será o texto mostrado na tela

