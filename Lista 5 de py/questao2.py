# Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.

#definindo a função com paramentro x do tipo inteeiro
def par_impar (x : int):
    if x % 2 == 0:
        return True    #se o paramentro for par, retorna o booleano true
    else:
        return False   #se o paramentro fo impar ele retorna o booleano false

#testando a função
print(par_impar(2))
print(par_impar(3))