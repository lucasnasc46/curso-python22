#calculadora usando função

def soma (n1, n2):
    return n1 + n2

def sub (n1,n2):
    return n1 - n2

def mult (n1,n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2

op = input("escolha a operação, +, -, * ou /")

n1 = float(input("Digite um numero"))
n2 = float(input("Digite outro numero"))

if op == "+":
    valor = soma(n1,n2)
    print(f"a soma de {n1} + {n2} e:", valor)

if op == "-":
    valor = sub(n1,n2)
    print(f"a soma de {n1} - {n2} e:", valor)

if op == "*" :
    valor = mult(n1,n2)
    print(f"a soma de {n1} * {n2} e:", valor)

if op == "/" :
    valor = div(n1,n2)
    print(f"a soma de {n1} / {n2} e:", valor)