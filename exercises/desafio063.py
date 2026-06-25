"""
Escreva um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma Sequência de Fibonaci.

Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

#Primeira forma
primeiro_termo = 0
segundo_termo = 1
cont = 0

print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
quantidade_termos = int(input('Quantos termos você quer mostrar ? '))
print('~' * 22)
print(f'{primeiro_termo} -> {segundo_termo} -> ', end='')

while cont < (quantidade_termos - 2):
    prox_termo = primeiro_termo + segundo_termo
    print(f'{prox_termo} -> ', end='')
    primeiro_termo = segundo_termo
    segundo_termo = prox_termo
    cont += 1
print(f'FIM!')


#Segunda forma
print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
n = int(input('Quantos termos você quer mostrar ? '))
t1 = 0
t2 = 1
print('~' * 22)
print('{} -> {} '.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' -> FIM')
