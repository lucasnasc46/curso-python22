#Faça um programa que auxilie os utilizadores ed reservatóios de agua a contralorem seu consumo
#obtenha as dimensões de um reservatorio, altura, largura e comprimento em cm
#e o consumo medio diario. Assuma que o reservatorio esteja cheio, tenha o formato cubico e informe
#a capacidade total do reservatorio em litro
#a automia do reservatorio em dias
#a classificação do consumo, de acordo com a quantidade de dias de autonomia
#consumo elevado se autonomia for menor q 2 dias
#consumo moderado ser a autonomia for entre 2 a 7 dias
#consumo reduzido se a autonomia for maior que 7 dias

#Solcintando ao use as dimensões do reservatorio e consumo e salvando nas respeectivas variaveis
h = float(input("Digite a altura do reservatorio em cm "))
l = float(input("Digite a largura em cm do reservatorio "))
c = float(input("Digite o comprimento em cm do reservatorio "))
cons = float(input("Digite o consumo medio diario em litros por dia "))

#Divindo por 1000 para converter de cm³ para litros
capacidade = (h*l*c)/1000

#Calculando a autonomia
auto = capacidade/cons

#mosntrando na tela a capacidade e autonomia do reservatorio
print("A capacidade do seu reservatorio é:", capacidade,"litros")
print("A autonomia do seu reservatorio é", auto, "dias")

#Verificando em qual tipo de consumo se encaixa
if auto < 2:
    print("Consumo elevado")

elif auto >= 2 and auto < 7:
    print("Consumo moderado")

else:
    print("Consumo reduzido")
