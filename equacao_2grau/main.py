import baskara
import math


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = math.pow(b,2) - 4*a*c

if delta >=0:
    x1 = baskara.baskx1(a,b,delta)
    x2 = baskara.baskx2(a,b,delta)
    print(f"{a}xˆ2 + {b}x + {c} = 0\nx1: {x1}\nx2: {x2}")

else:
    print("Esse problema não tem raízes reais, visto que delta é menor que zero!")