"""
A Confederação Nacional de Natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""

#Primeira forma
from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('O atleta tem {} anos e deverá ser da categoria MIRIM.'.format(idade))
elif idade > 9 and idade <=14:
    print('O atleta tem {} anos e deverá ser da categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <=19:
    print('O atleta tem {} anos e deverá ser da categoria JUNIOR.'.format(idade))
elif idade > 19 and idade <=25:
    print('O atleta tem {} anos e deverá ser da categoria SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e deverá ser da categoria MASTER.'.format(idade))


#Segunda forma
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <=9:
    print('Classificação MIRIM')
elif idade <=14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <=25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
