#Faça uma função que receba uma lista, percorra a lista e some os números pares dessa lista e retorne a soma. Imprimir a lista e o resultado da soma ao final do código.

#Fazendo função de somar
def soma_lis (lista : list): #definindo o argumento como lista
    cont = 0                 #inicializnando o contador para a contagem
    for i in lista:
        if i % 2 == 0:       #verificando se o indece da lista é par
            cont += 1        #se for para acrescenta 1 no contador

    return cont              #Retorna o valor total do contador 

l =  [1,2,3,2,1,2,3,4,5,6,5,4,3,2,1,8,10,12] #fazendo uma lista

result = soma_lis(l)          #chamando a função, passando a lista como argumento e salvando na variavel
print(l)
print ("a soma da quantidade de pares é: ", result)