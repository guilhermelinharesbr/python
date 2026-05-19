"""
Faça um programa que calcule a soma entre todos os números 
ímpares que são múltiplos de três e que se encontram no 
intervalo de 1 até 500.

"A soma de todos os 83 valores solicitados é 20667"
"""

#Primeira forma
soma_total = 0
quantidade = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        print(numero, end=', ')
        soma_total = soma_total + numero
        quantidade = quantidade + 1
print('FIM')
print('A soma de todos esses {} números é {}.'.format(quantidade, soma_total))
print('=' * 20)

#Segunda forma

#Acumulador:
soma = 0
#Contador:
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        #Poderia ser 'cont += 1':
        cont = cont + 1
        #Poderia ser 'soma += c': 
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
