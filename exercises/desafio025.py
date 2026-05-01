"""
Crie um programa que leia o nome de uma pessoa e 
diga se ela tem "Silva" no nome.
"""

#Primeira forma
nome = str(input('Digite seu nome completo: ')).strip()
print('SILVA' in nome.upper())

#Segunda forma
nome = str(input('Qual é seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
