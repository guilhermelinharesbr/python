"""
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.

Obs: considerando a maior idade sendo 21 anos.
"""

#Primeira forma
from datetime import date
atual = date.today().year
maiores_de_idade = 0
menores_de_idade = 0
for c in range (1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nascimento
    if idade >= 21:
        maiores_de_idade += 1
    else:   
        menores_de_idade += 1
print(f'Ao todo foram {c} pessoas') 
print(f'Ao todo tiveram {maiores_de_idade} maiores de idade.')
print(f'Ao todo tiveram {menores_de_idade} menores de idade.')


#Segunda forma
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
