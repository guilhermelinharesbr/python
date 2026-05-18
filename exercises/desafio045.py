"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

#Primeira forma
from time import sleep
from random import randint
print('-=-' * 5, 'JO-KEN-PO', ('-=-' * 5))
num_jogador = int(input("""
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? """))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
num_maquina = randint(0,2)
print('-=-' * 10)

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_jogador = opcoes[num_jogador]
escolha_maquina = opcoes[num_maquina]

print('O Jogador escolheu {}'.format(escolha_jogador))
print('A Máquina escolheu {}'.format(escolha_maquina))

if num_jogador == num_maquina:
    print('EMPATE')
elif (num_jogador == 0 and num_maquina == 2) or \
    (num_jogador == 1 and num_maquina == 0) or \
    (num_jogador == 2 and num_maquina == 1):
    print('O JOGADOR VENCEU, pois {} vence {}.'.format(escolha_jogador,escolha_maquina))
else:
    print('A MÁQUINA VENCEU, pois {} vence {}.'.format(escolha_maquina,escolha_jogador))    

print('-=-' * 20)


#Segunda forma - "Versão do Dante"
from time import sleep
from random import randint
print('-=-' * 5, 'JO-KEN-PO', ('-=-' * 5))
num_jogador = int(input("""
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? """))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
num_maquina = randint(0,2)
print('-=-' * 10)

escolha = str('')
escolha_maquina = str('')

if num_jogador == 0:
    escolha = 'PEDRA'
if num_jogador == 1:
    escolha = 'PAPEL'
if num_jogador == 2:
    escolha = 'TESOURA'
print('O Jogador escolheu {}'.format(escolha))
if num_maquina == 0:
    escolha = 'PEDRA'
if num_maquina == 1:
    escolha = 'PAPEL'
if num_maquina == 2:
    escolha = 'TESOURA'
print('A Máquina escolheu {}'.format(escolha))

if num_jogador == num_maquina:
    print('EMPATE')
elif num_jogador == 0:
    if num_maquina == 1:
        print('A MÁQUINA VENCEU, pois o Jogador escolheu Pedra e a Máquina Papel.') 
    else:
        print('O JOGADOR VENCEU, pois o Jogador escolheu Pedra e a Máquina Tesoura.')
elif num_jogador == 1:
        if num_maquina == 0:
            print('O JOGADOR VENCEU, pois o Jogador ecolheu Papel e a Máquina Pedra.') 
        else:
            print('A MÁQUINA VENCEU, pois o Jogador ecolheu Papel e a Máquina Tesoura.')
elif num_jogador == 2:
    if num_maquina == 0:
        print('A MÁQUINA VENCEU, pois o Jogador ecolheu Tesoura e a Máquina Pedra.') 
    else:
        print('O JOGADOR VENCEU, pois o Jogador ecolheu Tesoura e a Máquina Papel.')

print('-=-' * 20)


#Terceira forma
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Opção inválida!')
elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
        else:
            print('Opção inválida!')
elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('Opção inválida!')
