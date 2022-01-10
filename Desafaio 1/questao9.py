#Desenvolva um programa que recebe do usuário o placar de um jogo de futebol, os gols de cada time, e informe se o resultado foi um emparte, se a vitoria foi do primeiro ou segundo time

gol_timea = int(input("Digite quantos gols fez o time a: "))
gol_timeb = int(input("Digite quantos gols fez o time b: "))

if gol_timea == gol_timeb:
    print("O resultao do jogo foi empate")

elif gol_timea > gol_timeb:
    print("O resultado do jogo foi vitoria do tima A")

else:
    print("O resultado do jogo foi vitoria do time B")    