"""
Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o 
jogador vai tentar adivinhar até acertar, mostrando no 
final quantos palpites foram necessários para vencer. 
"""

#Primeira forma


#Segunda forma



"""
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
"""    