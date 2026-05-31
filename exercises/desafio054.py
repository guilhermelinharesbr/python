"""
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.

Obs: considerando a maior idade sendo 21 anos.
"""

#Primeira forma

for c in range (0, 7, 1):
    idade = int(input('Em que ano a {} ª pessoa nasceu? ').format(c))
print('Ao foram {} pessoas'.format(c)) 


#Segunda forma
