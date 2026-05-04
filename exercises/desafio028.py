"""
Escreva um programa que faça o computador "pensar" em um 
número inteiro entre 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

#Primeira forma
import random
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numero_pensado = random.randint(0,5)
numero_digitado = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if numero_pensado == numero_digitado:
    print('PERDI! Eu realmente pensei no número {}'.format(numero_pensado))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numero_pensado,numero_digitado))

#Segunda forma
from random import randint
from time import sleep
#Escolhe um número de maneira aleatória de 0 a 5:
computador = randint(0,5) 
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
#O método sleep do módulo time, faz o PC ficar parado por 3 segundos:   
sleep(3)  
if jogador == computador:
    print('PARABÉNS! YOU WIN!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
