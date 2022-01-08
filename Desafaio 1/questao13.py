#faça um programa para calcular a soma e a média de n numeros inteiros insetidos pelo o usuario

print ("insira os numeros. Digite zero para sair")

cont = 0
soma = 0.0
n = 1

while n != 0:
    n = int(input(""))
    soma = soma + n
    cont += 1

if cont == 0:
     print("Digite alguns numeros")

else:
     print("soma dos numeros:", soma)
     print ("a média dos números é:", soma/(cont-1))

