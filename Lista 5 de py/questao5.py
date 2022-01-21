#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado

#Definindo a função e passando um parametro do tipo inteiro
def quant (x : int):
    convert = str(x)    #Convertendo o tipo int para str (string)
    return len(convert) #retornando o tamanho da string, ou seja, a quantidade de digitos com a função len()

#testando a função
print(quant(12))