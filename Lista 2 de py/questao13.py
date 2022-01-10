#3.Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela contida na lista

#Solicantado as notas do aluno ao usario e as salvando nas variaveis correspondentes 
n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))

media = (n1+n2)/2  #Fazendo o calculo da media e salvando o resultado na variavel media


#Verificando se o valor da media pertece a qual conceito
if media >= 9 and media <= 10:
    print("Seu conceito é A")

elif media >= 7.5 and media < 9:
    print("Seu conceito é B")

elif media >= 6 and media < 7.5:
    print("Seu conceito é C")

elif media >= 4 and media  < 6:
    print("Seu conceito é D")

elif media >=0 and media < 4:
    print("Seu conceito é E")                