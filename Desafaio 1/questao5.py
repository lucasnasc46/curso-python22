#Crie um codigo que peça o nome do user por meio da função input ()
#Se o nome for "optimus prime", imprima "bem vindo, vc é um guerreiro de Cybertron"
#Caso contrario, imprima "bom dia, nome" - substitua o nome pelo o nome do user

#Pedindo oa user o seu nome
nome = input("Qual o seu nome: ")

#Verificando se o nome é optimus ou nao e mostando a mensagem de acordo como o nome
if nome == "Optimus Prime" or "optimus prime":
    print("Bem vindo, você é um guerriro de Cybertron")

else:
    print("Bom dia", nome)    