# Faça um programa que peça as 4 notas bimestrais e mostre a média

#vamos separa 4 variaveis para salvar as notas solicitadas ao usuário
#vamos definir que os inputs seram do tipo float pois como são notas, precisamos trabalhar com casas decimais
nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))
nota3 = float(input("Digite a terceira nota "))
nota4 = float(input("Digite a quarta nota "))

media = (nota1+nota2+nota3+nota4)/4  #vamos epgar os valores das notas somar, entre em parenteses por conta da notação e dividir por 4 para da a media 

print("A média do aluno e:", media) #printando na tela o resultado
