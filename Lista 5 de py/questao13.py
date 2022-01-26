#Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma
#pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal
#usando a fórmula peso ideal = 72.7 x alt - 58 e, para mulheres, peso ideal =
#62.1 x alt - 44.7.

def peso_ideal (h : float, sexo : str):

    if sexo == "f" or sexo =="F":
        imc = (62.1 * h) - 44.7
        return(imc)

    elif sexo == "m" or sexo == "M":
        imc = ( 72.7 * h) - 58
        return (imc)

altura = float(input("Digite o sua altura: "))
sexo = input("Digite seu sexo - m para masculino e f para feminino: ")

print(f" seu peso idael é: {peso_ideal(altura, sexo)}")