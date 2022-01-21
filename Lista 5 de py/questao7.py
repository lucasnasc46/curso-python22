 #Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (volume = (4/3)*pi*raio3)

#importando a biblioteca math para trabalhar com o valor de pi
import math 

#definindo uma função passando r como parametro do tipo float
def volume_esfera (r:float):
    vol = (4/3) * (math.pi * (r ** 3))  #Fazendo o calculo do volume de esfrea usando o valor de pi, chamando da biblioteca math
    return vol                          #Retornando o valor do volume

#Solicitando ao user o valor do raio
raio = float(input("Digite o valor do raio: "))

#printando o valor do volume, chamando a função e passando o valor do raio pedido como argumento
print(f"O volume da esfera é: {volume_esfera(raio)}")