"""
Crie um programa que leia o nome e o preço
de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.

B) Quantos produtos custam mais de R$1.000,00.

C) Qual é o nome do produto mais barato.
"""

#Primeira forma
print('-' * 25)
print('   Loja LINHARES   ')
print('-' * 25)

total_compra = produtos_acima_1000 = menor_preco = cont = 0
nome_produto_menor_preco = ' '

while True:
    produto = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o valor? R$'))
    cont += 1
    total_compra += preco
    continuar = ' '
    if cont == 1:
        menor_preco = preco
        nome_produto_menor_preco = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_produto_menor_preco = produto
    if preco > 1000:
        produtos_acima_1000 += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break    
print(f'''O valor total da compra foi: R${total_compra:.2f}   
Com valor superior a R$1.000,00 tiveram: {produtos_acima_1000} produto(s).
O produto mais barato foi {nome_produto_menor_preco} que custou {menor_preco}.''')


#################

#Segunda forma
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
