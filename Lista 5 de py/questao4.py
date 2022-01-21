#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def p_n (x: int):
    if x > 0:
        return "P"     #caso o x seja positivo ele retorna o booleano true
    else:
        return "N"   #caso o x seja negativo ele retorna o booleano false

print(p_n(2))
print(p_n(0))
print(p_n(-3))