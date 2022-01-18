#Faça um programa para ler um número inteiro n. Escrever a soma de todos os números pares de 2 até n. Use while.

#Solicitando um numero ao usuario e salvando na variavel n
n = int(input("Digite um numero: "))

#Definindo um contador igual a 1 para o laço ir de 1 ate o numero escohido 
i = 1
while i <= n:
    if i % 2==0:    #Se o númeor for par, ele vai somar
        soma = i + n 
    i +=1 
 
print(f"a soma dos pares é: {soma})")




      