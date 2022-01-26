#- Faça uma função que verifique se um valor é perfeito ou não. Um valor é
#dito perfeito quando ele é igual a soma dos seus divisores excetuando ele
#próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve
#retornar um valor booleano. (Use for pra ir de 1 até N,range…)

#Definindo uma função com um numero inteiro como parementro
def perfeito (n : int):
    lista = []              #Criando uma lista vazia para salvar os divisores do numero

    for i in range(1, n):   #pecorrendo todos os numeros no intervalo de 1 ao numero digitado
     
        if n % i == 0:          
            lista.append(i) #se algum numero no intervalo for divisor do numero digitado ele vai ser salvo na lista
            soma = sum(lista) #Somando os numeros da lista
    if soma == n:           #caso a soma dos numeros da lista for igual ao numero digitado, ele sera um perfeito e o retono sera True
        return True
#Se a soma nao for igual ao numeoro digitado o retono é falso
    else:
        return False

#Solicitando ao user um numero
numero = int(input("Digite um numero para verificar se é perfeito: "))
#chamando a função e passando o numero digitado como argumento da função
print(perfeito(numero))
