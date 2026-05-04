"""
Escreva um programa que faça o computador "pensar" em um 
número inteiro entre 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""


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
"""

"""
import random

mac = "00:16:3e:%02x:%02x:%02x" % (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
)
print(mac)
"""

#Segunda forma




"""
a condicional Composta - Tirar média das notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim!')
"""



#Vou pensar em um número entre 0 e 5. Tente adivinhar...
#Em que número eu pensei? 3
#  PROCESSANDO...
#GANHEI! Eu pensei no número 0 e não no 3!

#Segunda forma
