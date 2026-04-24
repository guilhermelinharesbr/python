#Faça um programa que leia um número qualquer e mostre 
#na tela a sua tabuada.

#Primeira forma
valor=int(input('Digite um número para ver sua tabuada:'))
print('-'*12)
print(valor,' x ',('1'), ' = ',(valor*1))
print(valor,' x ',('2'), ' = ',(valor*2))
print(valor,' x ',('3'), ' = ',(valor*3))
print(valor,' x ',('4'), ' = ',(valor*4))
print(valor,' x ',('5'), ' = ',(valor*5))
print(valor,' x ',('6'), ' = ',(valor*6))
print(valor,' x ',('7'), ' = ',(valor*7))
print(valor,' x ',('8'), ' = ',(valor*8))
print(valor,' x ',('9'), ' = ',(valor*9))
print(valor,' x',('10'), ' = ',(valor*10))
print('-'*12)

#Segunda forma
valor=int(input('Digite um número para ver sua tabuada:'))
print('-'*12)
print('{} x {:2} = {}'.format(valor, 1, valor*1))
print('{} x {:2} = {}'.format(valor, 2, valor*2))
print('{} x {:2} = {}'.format(valor, 3, valor*3))
print('{} x {:2} = {}'.format(valor, 4, valor*4))
print('{} x {:2} = {}'.format(valor, 5, valor*5))
print('{} x {:2} = {}'.format(valor, 6, valor*6))
print('{} x {:2} = {}'.format(valor, 7, valor*7))
print('{} x {:2} = {}'.format(valor, 8, valor*8))
print('{} x {:2} = {}'.format(valor, 9, valor*9))
print('{} x {:2} = {}'.format(valor, 10, valor*10))
print('-'*12)
