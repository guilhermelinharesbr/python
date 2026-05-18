"""
Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50.
"""

#Primeira forma
for c in range(0, 51):
    if c % 2 == 0 and c != 0:
        print(c, end=', ')
print('FIM!')

#Segunda forma
for n in range(2, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou!')

#Terceira forma
#Essa é a melhor neste caso, porque o FOR é 
#executado metade das vezes.
for n in range(2, 51, 2):
        print(n, end=' ')
print('Acabou!')
