#Fazer um algoritmo que ao receber o salario atual de um funcionario, calcule o valor do novo salario, reajustando de acordo com a tabela no site
#Abaico de R$500.00 reajsute de 15%
#de R$500.00 até 1000.00 reajuste de 10%
#acima de R$1000.00 reajuste de 5%

#Solicitando ao use o seu salario e salvando na variavel salario
salario = float(input("Digite o seu salario "))

#Verificando a quantia para fazer os calculos de reajuste de acordo com a tabela
if salario < 500:
    reaj =  (salario*0.15) + salario  #pegando o valor e multiplicado pela a porcentegem e somando com o valor do salario para da o valor do novo salario
    print("seu salario agora é de:", reaj)

elif salario >= 500 and salario < 1000:
    reaj =  (salario*0.1) + salario
    print("Seu salário agora é:", reaj)

elif salario >= 1000:
    reaj =  (salario*0.05) + salario
    print("Seu salario agora é de:", reaj)

else:
    print("Salario sem reajsute")