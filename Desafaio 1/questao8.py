#Escreva um programa para encontrar números entre 100 e 400 (ambos inclusos),
#onde cada digito de um número é um númeror par. os números obtidos devem ser impressos em sequência separada por virgulas

lista = []

for i in range(100, 401):
    s = str(i)

    if int(s[0]) %2 == 0 and int(s[1]) %2 == 0 and int(s[2]) %2 ==0:
        lista.append(s)

print(",".join(lista))        
