# 1 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34... 
# Faça um programa capaz de gerar a série até o N−ésimo termo, 
# onde N é inserido pelo usuário.

n = int(input("Digite um numero  para sequência de Fibonacci: "))

ant = 1
prox = 1
suma = 1
fib =[]
fib.append(ant)
fib.append(prox)

for x in range(n):
    soma = prox + ant
    ant = prox
    prox = soma
    
    fib.append(soma)

print("A sequencia de fibonacci:", fib)