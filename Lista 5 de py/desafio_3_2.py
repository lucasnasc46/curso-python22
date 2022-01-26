"""Escreva um procedimento que recebes 3 valores reais X, Y e Z e que
verifique se esses valores podem ser os comprimentos dos lados de um
triângulo e, neste caso, retornar qual o tipo de triângulo formado. Para que X,
Y e Z formem um triângulo é necessário que a seguinte propriedade seja
satisfeita: o comprimento de cada lado de um triângulo é menor do que a
soma do comprimento dos outros dois lados. O procedimento deve identificar
o tipo de triângulo formado observando as seguintes definições:
Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
Triângulo Isósceles: os comprimentos de 2 lados são iguais.
Triângulo Escaleno: os comprimentos dos 3 lados são diferentes."""


#Definindo uma função para verifcar se é um trinagulo
def tri (x, y, z):

#Fazendo a soma de cada dois lado 
   verifcax = y + z
   verifcay = z + x
   verifcaz = x + y

#fazendo a verificação se a soma dos lados é menor que cada comprimento (x, y e z)
#se satisfazer a condição o retorno é true, verdade, se nao o retorno é falso
   if x < verifcax and  y < verifcay and  z < verifcaz:
       return True
  
   else:
       return False


#definindo uma função para verificar o tipo do triangulo
def tipo_tri(x, y, z):

#Verificando o tipo de acordo com os comprimentos (x, y e z)
    if x == y and x== z:
        return ("Triangulo equilatero")

    elif x == y or x == z: 
        return ("Triangulo isoceles")
    
    else:
        return("triangulo escaleno")

#Solicitando ao user as 3 medidas do comprimento do triangulo
x1 = float(input("Digite o 1 lado: "))
y1 = float(input("Digite o 2 lado: "))
z1 = float(input("Digite o 3 lado: "))

#verificando se os valores formam um triangulo, chamando a função feita para isso
#se ela retorna verdadeiro, chama a função que verificar o tipo
if tri(x1,y1,z1) == True:
    print(tipo_tri(x1,y1,z1))

#se a chamada da função retornar falso, printa mensagem de erro
else:
    print("Essas medidas nao formam um trinagulo!")