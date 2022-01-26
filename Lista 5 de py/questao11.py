#Faça um procedimento que recebe a idade de um nadador por parâmetro e retorna , também por parâmetro, a categoria desse nadador de acordo com a tabela abaixo:

#definindo a função passando idade coomo parametro do tipo inteiro
def modalidade (idade:int):

#fazendo a verificação da idade e retornao a categoria para cada faixa de indade 
    if idade < 5:
        return("idade invalida, 5+")
    elif idade >= 5 and idade <=7:
        return ("infatil A")

    elif idade >= 8 and idade <=10:
        return ("infatil B")

    elif idade >= 11 and idade <=13:
        return ("juvenil A")

    elif idade >= 14 and idade <=17:
        return ("juvenil B")

    else:
        return("adulto")

#Solicitando ao user a idade e salvando na vairiavel
idade_atleta = int(input("Digite a idade do atleta de natação: "))

#Chamando a função e printando a categoria na tela
print(f"A categoria é {modalidade(idade_atleta)}")