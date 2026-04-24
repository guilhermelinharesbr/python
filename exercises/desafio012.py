#Faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço, com 5% de edesconto.

#Primeira forma
valor = float(input('Qual é o preço do produto? R$'))
desconto = float((valor*5)/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor,(valor-desconto)))

#Segunda forma
valor = float(input('Qual é o preço do produto? R$'))
valor_com_desconto = valor - ((valor*5)/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor,(valor_com_desconto)))
