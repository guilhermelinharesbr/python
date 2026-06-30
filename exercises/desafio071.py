"""
Crie um programa que simule o funcionamento de
um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado(número inteiro)
e o programa vai informar quantas cédulas de cada
valor serão entregues.

Obs: Considere que o caixa possui cédulas de R$50,
R$20, R$10 e R$1.
"""

#Primeira forma
print('-' * 25)
print('   Caixa Eletrônico   ')
print('-' * 25)

cedula_atual = 50
total_cedulas = 0

valor = int(input('Qual valor a ser sacado? R$'))    
while True:
    if valor >= cedula_atual:
        valor -= cedula_atual
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} de cédulas de R${cedula_atual}.')
        
        if cedula_atual == 50:
            cedula_atual = 20
        elif  cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1

        total_cedulas = 0

        if valor == 0:
            break
print('-' * 25)
print(f'Volte sempre. Sessão Encerrada.')


#################


#Segunda forma
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV!')
