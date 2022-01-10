#faça um programa para encontrar a mediana de três valores inseridos pelo o usuário

#Solicitando ao user os tren numeros e salvando as respectivas variaveis
n1 = float(input("Digite o primeiro número "))
n2 = float(input("Digite o segundo número "))
n3 = float(input("Digite o terceiro número "))

#Verificando qual o valor do meio da sequencia dos numeoros e monstrando na tela o resultado
if n1 < n2 and n2 < n3:
    print("a mediana é:", n2)

elif n2 < n1 and n1 <n3:
    print("a media é:", n1)

else:
    print("a media é:", n3)        

