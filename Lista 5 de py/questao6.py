#Crie uma função que calcula o aumento do salário de um funcionário. A função deve receber a porcentagem de aumento e o salário atual e retornar o no salário. O usuário deve informar o salário atual e a porcentagem de aumento

#Definindo uma função e passando dois paramentros do tipo float, uma para o salaraio e outro para a porcentagem de aumento
def aumento (sal, porc : float):
    aument= sal * (porc/100)       #Calculando o valor do aumento de acordo com a porcentagem
    novo_sal = sal + aument        #somando o aumento com o salario antigo 
    return novo_sal                #retornando o salario com aumento 

#Solicitando ao user o salario e porcentagem de aumento e salvando nas respctivas variaveis
salar = float(input("Digite seu salario: "))
porcent = float(input("Digite a porcentagem e aumento: "))

#chamando a função para printar o novo valor, passando como argumneto as variaveis com os valores do salario e porcentagem armazendadas
print(f"Seu novo salario é {aumento(salar, porcent)}")