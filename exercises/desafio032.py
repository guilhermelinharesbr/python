"""
Faça um programa que leia um ano qualquer
e mostre se ele é BISSEXTO.
"""

# Primeira forma
ano = int(input('Digite um ano para analisar se ele é Bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é um ano Bissexto.'.format(ano))
else:
    print('O ano {} NÃO é um ano Bissexto.'.format(ano))

# Segunda forma
from datetime import date
ano = int(input('Que ano você quer analisar se é Bissexto ou não ?' \
' Coloque 0 para analisar o ano atual: '))
# Da data de hoje pega apenas o ano. Só se o usuário digitar 0.
ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é um ano Bissexto.'.format(ano))
else:
    print('O ano {} NÃO é um ano Bissexto.'.format(ano))
