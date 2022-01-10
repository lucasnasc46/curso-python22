#Faça um Programa que pergunte em que turno você estuda. Peça para
#digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
#"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso


#Solicitando ao user a sigla de qual turno ele estuda e salavando na variavel turno
print("Qual o turno vc estuda?")
turno = input("Digite M para matutino, V para vesperino ou N para noturno ")

#Verficando qual foi a sigla, maiscula ou minuscula, escolhido pelo o user e retornando a saldação certa
if turno in ("m") or  turno  in ("M"):
    print("Bom dia!")

elif turno in ("V") or turno in ("v"):
    print("Boa tarde!")

elif turno in ("n") or turno in ("N"):
    print("Boa noite!")

else:
    print("Valor invalido")    