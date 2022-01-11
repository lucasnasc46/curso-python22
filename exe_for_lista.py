# Crie um programa para cadastrar N pessoas.
# Adicione em uma lista e imprima npo final.
n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    endereco = input("Digite o seu endereço: ")
    peso = float(input("Digite seu peso: "))
    nova_pessoa = [nome, idade, endereco, peso]
    lista_pessoas.append(nova_pessoa)

for pessoa in lista_pessoas:
    print(
        f"Bem-vin@ {pessoa[0]}, você tem {pessoa[1]} anos, pesa {pessoa[3]}kg, e mora em {pessoa[2]}")

    if pessoa[1] >= 18:
        print("Voce é maior de indade")
    else:
        print("voce é menor de idade")
