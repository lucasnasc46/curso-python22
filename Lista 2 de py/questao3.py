#Faça um programa pra calcular o IMC e informar qual categoria pertence o IMC da pessoa

#Solicitando o peso e altura ao user e salvando nas respectivas variaveis
peso = float(input("Digite seu peso em kg "))
altura = float(input("Digite sua altura em metros "))

imc = peso/(altura ** 2)   #Fazendo o calculo o IMC

#Verificando as condições para dá o status do peso do user, de acordo com os calulos do Min. da Saúde
if imc < 18.5:
    print("Você está abaixo do peso")

elif imc >= 18.5 and imc <=25: #usando o and para dizer ao py que se o imc estiver entre os valores 18.5 e 25 ele retornar que está com o peso ideal, assim como nos elif abaixo
    print("Você está com o peso ideal")

elif imc > 24 and imc <= 30:
    print("Você está com sobrepeso") 

elif imc > 30 and imc <= 40:
    print("Você está obeso")

else:
    print("Você está com obesidade mórbida ")               