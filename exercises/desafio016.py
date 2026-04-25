"""Crie um programa que leia um número Real
qualquer pelo teclado e msotre na tela a 
sua porção inteira.
Ex: Digite um número:6.127 
O número 6.127 tem a parte inteira 6."""

#Primeira forma
import math
valor=float(input('Digite um número Real:'))
print('A porção inteiro do número digoitado é {}'.format(math.trunc(valor)))

#Segunda forma
import math
valor=float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(valor,math.trunc(valor)))

#Terceira forma
from math import trunc
valor=float(input('Digite um valor:'))
print('O valor que você digitou foi {} e a sua porção inteira é {}'.format(valor,trunc(valor)))

#Quarta forma, usando a função int
valor=float(input('Digite um número:'))
print('O valor que você escreveu foi {} e a sua porção inteira é {}'.format(valor,int(valor)))
