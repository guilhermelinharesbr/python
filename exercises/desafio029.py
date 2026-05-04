"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo 
que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.
"""

#Primeira forma
velocidade = int (input('A que velocidade o carro passou no radar? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você estava a {}Km e a velocidade máxima da via é de 80Km. Sua multa é de R${},00'.format(velocidade,multa))
else:
    print('Velocidade condizente com a via.')

#Segunda forma
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
