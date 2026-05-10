"""
Escreva um programa para aprovar o empréstimo bancário para a compra
 de uma casa. O programa vai perguntar o valor da casa, o salário do 
 comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 
30% do salário ou então o empréstimo será negado.
"""

#Primeira forma
casa = float(input('Digite o valor da casa que você quer comprar em R$'))
salario = float(input('Digite o seu salário em R$'))
anos_de_pagamento = int(input('Em quantos anos você pretende pagar a casa? '))
prestacao = casa / (anos_de_pagamento * 12)
if prestacao > (salario * 30) / 100:
    print("Empréstimo NEGADO.")
else:
    print('Empréstimo APROVADO.')

#Segunda forma
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print("Empréstimo APROVADO.")
else:
    print('Empréstimo NEGADO.')
