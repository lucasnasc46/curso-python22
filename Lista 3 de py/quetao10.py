#.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada

#solicitando ao usuario qual numeor quer a tabuada
n = int(input("Digite um numero para verificar a tabuada: "))
print(f"Tabuada de {n}:")

#gerando a tabuada
for i in range(11):
    tab = n * i

    print(f"{n} X {i}: {tab}")