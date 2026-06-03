"""
Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o 
jogador vai tentar adivinhar até acertar, mostrando no 
final quantos palpites foram necessários para vencer. 
"""

#Primeira forma
from random import randint
from time import sleep
cont = 0
jogador = 11
computador = randint(0,10) 
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
cont += 1
print('PROCESSANDO...')
sleep(2)
while jogador != computador:
    jogador = int(input('Tente novamente: '))
    cont += 1
    print('PROCESSANDO...')
    sleep(2)
if jogador == computador:
    print(f'PARABÉNS! YOU WIN! Eu pensei no número {computador} e você levou {cont} palpites para acertar que eu pensei no número {jogador}.')


#Segunda forma
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites)) 
