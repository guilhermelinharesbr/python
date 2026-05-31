"""
Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
"""

#Primeira forma
maior_peso = 0
menor_peso = 0
for pessoa in range (1, 6):
    peso = float(input('Qual o peso da {} pessoa ? '.format(pessoa)))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O Peso é {peso}')
print(f'O Maior peso é {maior_peso}')
print(f'O Menor peso é {menor_peso}')

#Segunda forma
