#Arquivo main (pricinpal)

#importando o modulo de calculo de area
import area

#Solicitando ao user qual figura quer calcular a area
opcao= int(input("escolha uma opção: 1. circulo, 2. quadrado: "))

#verificando a opçao escolhida
if opcao == 1:
    circ= float(input("Qual o valor do raio? "))
    print("a area do circulo é:", area.circulo(circ))     #chamando a funcao de circulo que esta dentro do modulo 

elif opcao == 2:
    quad= float(input("Digite o valor do lado do quadrado: "))
    print("a area do quadrado é:", area.quadrado(quad))   #chamando a funcao do quadrado que esta dentro do modulo 

else:
    print("escolha invalida")