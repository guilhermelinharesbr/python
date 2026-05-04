"""
Desenvolva um programa que pergunte a distância 
de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km 
e R$0,45 para viagens mais longas.
"""

#Primeira forma
distancia = float(input('Qual a distância da viagem em Km? '))
if distancia <= 200:
    preco = distancia * 0.50
    print('O valor da passagem é R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O valor da passagem é R${:.2f}'.format(preco))

#Segunda forma
distancia = float(input('Qual a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O valor da passagem é R${:.2f}'.format(preco))

#Terceira forma
distancia = float(input('Qual a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da passagem é R${:.2f}'.format(preco))
