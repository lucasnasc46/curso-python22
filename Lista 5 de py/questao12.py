# Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo:

# definindo a função media e passando como parementro a nota tipo float
def media(nota: float):

#fazendo a verificação das notas e retornando o conceito
    if nota >= 9 and nota <= 10:
        return("Seu conceito é A")

    elif nota >= 7 and nota <= 8.9:
        return("Seu conceito é B")

    elif nota >= 5 and nota <= 6.5:
        return("Seu conceito é C")

    elif nota >= 0 and nota <= 4.9:
        return("Seu conceito é D")

#Solicitando ao user a meida final 
media_final = float(input("Digite a media final do aluno: "))

#chamando a função 
print(media(media_final))