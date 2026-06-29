"""
Faça um programa que jogue par ou ímpar com
o computador. O jogo só será interrompido 
quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou
no final do jogo.
"""

#Primeira forma
from random import randint
rodadas = vitorias = 0

print(f'-' * 10, 'Jogo PAR ou ÍMPAR', '-' * 10)

while True:
    jogador = str(input('Você quer PAR ou ÍMPAR(P/I): ')).strip().upper()[0]
    if jogador == 'P':
        print(f'Jogador escolheu PAR e Máquina Ímpar.')
    if jogador == 'I':
        print(f'Jogador escolheu ÍMPAR e Máquina Par.')
    num_jogador = int(input('Digite um número de 1 a 10: '))
    computador = randint(0,10)
    rodadas += 1
    print(f'PROCESSANDO...')
    print(f'O jogador escolheu {num_jogador} e a máquina escolheu {computador}.')
    if (num_jogador + computador) % 2 == 1:
        print(f'O resultado foi ÍMPAR.')
        if jogador == 'I':
            vitorias += 1
        if jogador == 'P':
            break 
    elif (num_jogador + computador) % 2 == 0:
        print(f'O resultado foi PAR.')
        if jogador == 'P':
            vitorias += 1
        if jogador == 'I':
            break
    print(f'-' * 3, 'próxima rodada', '-' * 3)
print(f'Fim do programa. Foram executadas {rodadas} rodada(s). O jogador venceu {vitorias} veze(s).')


#################

#Segunda forma
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
