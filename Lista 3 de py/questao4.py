#Faça um Programa que peça o nome, a idade e a altura de N pessoas, armazene cada informação em uma lista e depois insira em uma lista maior chamada lista_pessoas. Por fim, imprima o nome e peso de cada pessoa, e
#diga se ela é maior ou menor de idade.

#Solicitando a quantidade de cadastros
quat = int(input("Digite a quantidade de pessoas que deseja cadastrar: "))

#definidno a lista maior para ser preenchida no for
lista_total = []

#Salvando os dados da quatidade de pessoas definida pelo o user
for x in range(quat):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    h = float(input("Digite a altura"))

#Salvando os dados em listas
    lista = [nome, idade, h]

#adicionando todas as listas da quantodade definida na llista maior
    lista_total.append(lista) 

#Fazendo a verificação se a pessoa é de maior
for i in lista_total:
    if i[1] >= 18:                            #Vericando se a 2 posição, da idade, é maior q 18
        print(lista_total, "você é de maior")

    else:
        print(lista_total, "você é de menor")

