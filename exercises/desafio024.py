"""
Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com o nome "Santo".
"""

#Primeira forma
cidade = str(input('Qual sua cidade de nascimento? '))
print('Santo' in cidade)

#Segunda forma
cidade = str(input('Em que cidade você nasceu? '))
print(cidade[:5] == 'Santo')

#Terceira forma
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper == 'SANTO')