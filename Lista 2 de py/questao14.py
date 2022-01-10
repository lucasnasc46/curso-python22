#.Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

#Solicitando ao user um num equivalente ao dia da semana e salvando na variavel dia
dia = int(input("Digite um número de 1 a 7 equivalente ao dia da semana "))

#Verificando qual numero foi digitado e correspondendo ao dia da semana equivalente
if dia == 1:
    print("O dia da semana é Domingo")

elif dia == 2:
    print("O dia da semana é Segunda") 

elif dia == 3:
    print("O dia da semana é Terça") 

elif dia == 4:
    print("O dia da semana é Quarta") 

elif dia == 5:
    print("O dia da semana é Quinta")

elif dia == 6:
    print("O dia da semana é Sexta")

elif dia == 7:
    print("O dia da semana é Sabado")

else:
    print("numero invalido")     




