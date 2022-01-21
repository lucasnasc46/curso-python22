#Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.

#Definindo uma função com parametro x sendo inteiro
def posi_neg (x: int):
    if x > 0:
        return True     #caso o x seja positivo ele retorna o booleano true
    else:
        return False    #caso o x seja negativo ele retorna o booleano false

#Apenas testando a função
print(posi_neg(-9))
print(posi_neg(9))