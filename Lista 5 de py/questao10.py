#.Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

#importando a biblioteca datetime para fazer as operações com datas de forma mais facil 
import datetime

#Definindo uma função com 3 parametros para ano, meses e dias 
def dias (a, m, d):
    data_nas = datetime.datetime(a, m, d)     #transformando os parametros em data com a função datetime
    data_atual = datetime.datetime.now()      #salvando a data atual em um variavel 

    dia = data_atual - data_nas               #fazendo a subtração da data atual com a data de aniversario 
    
    return dia                                #retornando o valor da subtraçao em dias

#solicitando ao user a data de aniversario 
a = int(input("digite o ano que vc nasceu: "))
m = int(input("digite o numero do mes que vc nasceu: "))
d = int(input("Digite o dia qu vc nasceu: "))

#Chamando a função e passando a data de aniversario do usuario como argumento
print(dias(a, m, d))


