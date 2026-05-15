"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

#Primeira forma
import time
from random import randint
print('-=-' * 5, 'JO-KEN-PO', ('-=-' * 5))
num_jogador = int(input("""
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? """))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
num_maquina = randint(0,2)
print('-=-' * 10)

escolha_jogador = str('')
escolha_maquina = str('')

if num_jogador == 0:
    escolha_jogador = 'PEDRA'
if num_jogador == 1:
    escolha_jogador = 'PAPEL'
if num_jogador == 2:
    escolha_jogador = 'TESOURA'
if num_maquina == 0:
    escolha_maquina = 'PEDRA'
if num_maquina == 1:
    escolha_maquina = 'PAPEL'
if num_maquina == 2:
    escolha_maquina = 'TESOURA'
print('O Jogador escolheu {}'.format(escolha_jogador))
print('A Máquina escolheu {}'.format(escolha_maquina))

if num_jogador == num_maquina:
    print('EMPATE')
elif num_jogador == 0 and num_maquina == 1:
    print('A MÁQUINA VENCEU, pois o Jogador ecolheu Pedra e a Máquina Papel.') 
    if num_jogador == 0 and num_maquina == 2:
        print('O JOGADOR VENCEU, pois o Jogador ecolheu Pedra e a Máquina Tesoura.')
elif num_jogador == 1 and num_maquina == 0:
    print('O JOGADOR VENCEU, pois o Jogador ecolheu Papel e a Máquina Pedra.')
    if num_jogador == 1 and num_maquina == 2:
        print('A MÁQUINA VENCEU, pois o Jogador ecolheu Papel e a Máquina Tesoura.')
elif num_jogador == 2 and num_maquina == 0:
    print('A MÁQUINA VENCEU, pois o Jogador ecolheu Tesoura e a Máquina Pedra.')
    if num_jogador == 2 and num_maquina == 1:
        print('O JOGADOR VENCEU, pois o Jogador ecolheu Tesoura e a Máquina Papel.')

print('-=-' * 20)

#Segunda forma - "Versão do Dante"
import time
from random import randint
print('-=-' * 5, 'JO-KEN-PO', ('-=-' * 5))
num_jogador = int(input("""
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? """))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
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
