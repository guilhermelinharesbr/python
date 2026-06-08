"""
Faça um programa que leia um número qualquer 
e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120.
"""

#Primeira forma
acumulador = 1 #porque um fator de multiplicação limpa é 1, se fosse soma seria 0.
numero = int(input('Digite um número para que possa ser calculado o seu Fatorial: '))
print(f'O fatorial de {numero}! = ', end='')
while numero > 0:
    acumulador = numero * acumulador
    if numero > 1:
        print(f'{numero} x ', end='')
    if numero == 1:
        print(f'{numero}', end='' )
    numero = numero - 1
print(f' = {acumulador}')


#Segunda forma
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))


#Terceira forma
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f =1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))
