#Faça um programa que lê um número inteiro n. Escrever a soma de todos os números de 1 até n. Use while.

#Solicintando ao usuario um numero para somar 
n = int(input("Digite um número: "))

#definindo o contador valendo 1 enquanto ele for menor do que o numero que o usuário definio
#ele vai somar até o numero escolhido
i = 1
while i <= n:
    soma = n + i
    
    print(f"a soma de {i} + {n} é: {soma}")
    i += 1
  
