"""
Refaça o DESAFIO 051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
"""

#Primeira forma
c = 0
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = primeiro_termo
while c < 10:
    print(f'{pa}', end=' -> ')
    pa = pa + razao
    c += 1
print(f'Fim!')


#Segunda forma
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
