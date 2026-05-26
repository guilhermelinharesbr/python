"""
Faça um programa que leia um número inteiro e 
diga se ele é ou não um número primo.
"""

#Primeira forma - 
num = int(input('Digite um número:'))
cont = 0
for c in range (1, num + 1):
    if num % c == 0:
        cont += 1
print(f'O número {num} foi divisível {cont} vezes.')   
if cont == 2:
    print(f'E por isso ele É PRIMO!')
else:
    print(f'E por isso ele NÃO É PRIMO!')


#Segunda forma
num = int(input('Digite um número: \033[32m'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m', end='')
        tot += 1
    else:
        print(f'\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')   
if tot == 2:
    print(f'E por isso ele É PRIMO!')
else:
    print(f'E por isso ele NÃO É PRIMO!')
