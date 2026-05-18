"""
Faça um programa que mostre na tela uma contagem 
regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

#Primeira forma
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOM! BOOM! POW!')


#Separação
print('-=-' * 10)


#Segunda forma
from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(0.5)
print('BUM! BUM! POW!')
