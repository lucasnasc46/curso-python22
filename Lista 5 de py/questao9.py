#Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro (True) caso o valor seja primo e Falso (False) em caso contrário.

#importando a biblioteca math para usar uma de suas funções 
import math

#Definindo a função primo, passando como argumento um tipo inteiro 
def primo(n : int):
    
    ind = 2                                 #declarando uma variavel e a iniciando com o valor 2 
    if n > 0:                               #Verificando se o numero digitado é positivo 
        while ind <= math.sqrt(n):          #Sendo positivo, enquanto o contador for menor ou igual a raiz quadarada do parametro (math.sqrt(n)) o laço continua 
            if n % ind < 1:                 #Se o resto da divisão do paramentro com o contador for menor q 1 retorna falso pois ele nao é primo
                return False
            ind += 1                        #acrescimo de 1 no contador para o laço 

        return n > 1

    else:                                   #caso o user digite um valor negativo, retorna uma msg de erro
        print("digite um número positivo")

#Solicitando ao user um numero
n = int(input("digite um numero para saber se ele é primo: "))

#Chamando a função de verificação de numeros primos
print (primo(n))