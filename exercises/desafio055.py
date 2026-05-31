"""
Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
"""
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
"""
#Segunda forma
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
