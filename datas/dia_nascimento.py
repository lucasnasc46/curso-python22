#Crie um programa que receba o dia, mês e ano de nascimento de uma pessoa. Use a biblioteca datatime pra verificar o dia da semana que a pessoa nasceu. 


import datetime
from time import strftime

a = int(input("digite o ano que vc nasceu: "))
m = int(input("digite o numero do mes que vc nasceu: "))
d = int(input("Digite o dia qu vc nasceu: "))

data_nasc = datetime.datetime(a,m,d)

print(data_nasc.strftime("Seu dia de nascimento é: %A"))