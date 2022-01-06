#Faça um programa que pergunte quanto vc ganha por hora e o numero de horas trabalhadas no mês. Calcule e mostre o total do seu salario no referido mês

#Definindo os inputs como float, para podermos trabalhar com casas decimais 
valor = float(input("Qual o valor da sua hora de trabalho? ")) #Solicitando ao usuário o valor da sua hora de trabalho e salvando na vairiavel valor
horas = float(input("Quantas horas voce trabalhou nesse mês? ")) #Solicitando a quantidade horas trabalhadas e salva na variavel horas

salario = valor*horas #salvando o resultado no salario na vairavel salario

print("Seu salario deste mês é de R$",salario) #mostrando na tela o valor do seu salario
