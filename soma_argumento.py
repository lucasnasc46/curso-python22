# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma_arg (arg1, arg2, arg3):
    return arg1 + arg2 + arg3

argumento1 = int(input("Digite primeiro argumento "))
argumento2 = int(input("Digite o segundo argumento "))
argumento3 = int(input("Digite o terceiro argumento "))

result = soma_arg (argumento1, argumento2, argumento3)
print(result)