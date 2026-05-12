"""
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.

- Se é a hora de se alistar.

- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou 
que passou do prazo.
"""

#Primeira forma
from datetime import datetime
ano_atual = datetime.now().year
idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Em {} você tem {} ano(s) e faltam {} ano(s) para você se alistar.'.format(ano_atual,idade,(18 - idade)))
elif idade > 18:
    print('Em {} você tem {} ano(s) e já se passaram {} ano(s) que você deveria ter se alistado.'.format(ano_atual,idade,(idade-18)))
else:
    print('Você precisa se alistar esse ano mesmo.')

#Segunda forma
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade ==18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
