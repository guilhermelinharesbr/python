"""
Escreva um programa que leia dois números inteiros e 
compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.
"""

#Primeira forma
primeiro_num = int(input('Digite o primeiro número: '))
segundo_num = int(input('Digite o segundo número: '))
if primeiro_num > segundo_num:
    print('{} é maior que {}.'.format(primeiro_num,segundo_num))
if segundo_num > primeiro_num:
    print('{} é maior que {}.'.format(segundo_num, primeiro_num))
if segundo_num == primeiro_num:
    print('{} é igual a {}.'.format(primeiro_num,segundo_num))


#Segunda forma
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são IGUAIS.')    
