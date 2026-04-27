"""Faça um programa que leia um ângulo qualquer e mostre 
na tela o valor do seno, cosseno e tangente desse ângulo.

Obs: Para cosseno usar o método math.cos,
para seno usar o método math.sin,
para tangente usar o método math.tan e
para radianos usar o método math.radians.
Os métodos math.cos, math.sin e math.tan 
são indicadas em radianos."""

#Primeira forma
import math
angulo = float(input('Digite o valor do ângulo:'))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))

#Segunda forma
from math import radians, sin, cos, tan
angulo = float(input('Digite um valor para o ângulo:'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = sin(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))
