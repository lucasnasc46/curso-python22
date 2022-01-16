# 2 - Faça um programa que crie uma matriz NxN, insira os valores e 
# imprima em formato de matriz.
n = 3
matriz = [[0 for x in range(n)] for i in range(n)]

for i in range(n):
    for x in range(n):
        matriz[i][x] = float(input(f"Informe o valor do elemento [{i + 1}][{x + 1}]: "))
print("\nMatriz:")
for i in range(n):
    print(matriz[i])