"""
Crie um programa que leia vários números inteiros
pelo teclado. No final da execução, mostre a média 
entre todos os valores e qual foi o maior e o menor 
valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.  
"""

#Primeira forma
num = maior_valor = menor_valor = cont = soma = media = 0 
continuar = 'x'

while continuar != 'n':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]')).strip().lower()
    soma += num
    cont += 1
    if cont == 1:
        maior_valor = num
        menor_valor = num
    else:
        if num > maior_valor:
            maior_valor = num
        if num < menor_valor:
            menor_valor = num
media = soma / cont
print(f'Você digitou {cont} número(s) e a média foi {media:.2f}.')
print(f'O maior valor foi {maior_valor} e o menor foi {menor_valor}.')

#################

#Segunda forma
resp = 'S'
soma = quant = media = maior = menor = 0 
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]        
media = soma / quant
print('Você digitou {} número(s) e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
