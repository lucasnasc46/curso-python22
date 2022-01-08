#Faça um programa que o user informe o salario recebido e o total
#gasto com despesas. Deverá ser exebido na tela "gastos dentro do orçamento"
#caso o valor gasto não ultrapasse o valor do salario e 
#"orçamento estourado" se o valor gasto ultrapasar o valor do salario

#Pedindo ao user os valores do salario e gastos e salvando na suas variaveis respectivas
recebido = float(input("Digite o seu salario recebido do mês"))
gasto = float(input("Digite o total gasto no mês"))

#Verificando se os gastos foram maior que o recebedido e virse e versa e mostrando na tela para o user
if recebido > gasto:
    print("Gastos denro do orçamento")

else:
    print("Orçamento estourado")    