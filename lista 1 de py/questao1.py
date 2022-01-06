#Faça um programa que peça dois números e imprima a soma

#n1 é a variavel onde vamos salvar o 1 numero, que estamos pedindo ao usuario para digitar, o n2 é a variavel para o segundo número
n1 = int(input("digite o primeiro número ")) #input é a função para que o usuario digite um valor, por padrão o input salva oq o user digitar como string 
n2 = int(input("digite o segundo número "))  #por isso precisamos colocar o tipo da variavel antes do input, por isso o int

soma = n1+n2  #soma é a variavel onde vamos salvar o resultado da soma dos numeros 

print("A soma dos dois números é:", soma) #função print para mostrar na tela o resultado 
