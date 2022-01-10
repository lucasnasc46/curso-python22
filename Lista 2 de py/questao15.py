#.Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida

#Pedindo ao user q informe o número correspondente a sua bebida, usado o \n para quebrar linha 
op = int(input("Digite o número correspondente a a bebida que voce deseja \nMENU\n1. Água \n2.Refrigerante \n3.Suco \n"))

#Verificando qual o numero escolhido e associando a bebida escolhida
if op == 1:
    print("Você escolheu água")

elif op == 2:
    print("Você escolheu refrigerante")

elif op == 3:
    print("Voce escolheu suco")

else:
    print("Número de escolha invalido")        