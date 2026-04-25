#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

#Primeira forma
import math
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (math.sqrt(pow(cateto_oposto,2)+pow(cateto_adjacente,2)))
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))

#Segunda forma
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('A hipotenusa medirá: {:.2f}'.format(hipotenusa))

#Terceira forma, usando o método hypot para calcular a hipotenusa
from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto,cateto_adjacente)
print('A hipotenusa terá a medida: {:.2f}'.format(hipotenusa))
