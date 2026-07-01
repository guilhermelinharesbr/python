"""
Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso de zero 
até vinte.
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
"""

#Primeira forma
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')

while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if numero >= 0 and numero <= 20:
            print(f'Você digitou o número {numeros[numero]}')
            break
        else:
            print(f'Tente novamente. Digite um número válido!')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break


#################


#Segunda forma
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
