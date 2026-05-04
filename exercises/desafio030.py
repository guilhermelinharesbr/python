"""
Crie um programa que leia um número inteiro e 
mostre na tela se ele é PAR ou ÍMPAR.
"""

#Primeira forma
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print ('O número {} é PAR.'.format(numero))
else:
    print ('O número {} é ÍMPAR.'.format(numero))

#Segunda forma
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR.'.format(numero))
else:    
    print('O número {} é ÍMPAR.'.format(numero))
