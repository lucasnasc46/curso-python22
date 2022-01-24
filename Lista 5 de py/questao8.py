#Escreva um função que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra for A a função calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada também deve retornar por parâmetro.

#definindo a função com 3 parametros do tipo float e um do tipo string
def media (x, y, z : float, a : str):
    
    if a == "a" or "A":                    #Caso o argumento do paramentro do tipo string seja a ou A calcula a media aritmetica e retorna seu valor
        arit = (x + y + z)/3
        return arit

    elif a == "b" or "B":
        pond = ((x * 5)+(y * 3)+(z*2))/3   #Caso o argumento do paramentro do tipo string seja b ou B calcula a media ponderada e retorna seu valor
        return pond

    elif a == "h" or "H":                  #Caso o argumento do paramentro do tipo string seja h ou H calcula a media harmonica e retorna seu valor
        harm = 3/(( 1/x ) + (1/y) + (1/z))
        return harm

    else:                                  # se o valor nao for nenhum das ooções acima, retorna erro 
        print("op errada!")                 

#solicintando ao user as 3 notas e salvando nas respectivas variaiveis 
x = float(input("Digite a 1 nota: "))
y = float(input("Digite a 2 nota: "))
z = float(input("Digite a 3 nota: "))

#solicitando ao user qual o tipo de media ele deseja 
a = input("Escolha uma opção de media (a - aritmetrica b - ponderada h - harmonica: ")

#chamando a função e passando os argumentos dos paramentros 
print(media(x, y, z, a))