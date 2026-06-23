"""
Melhore o DESAFIO 061, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.
"""

#Primeira forma
cont = 0
mais_termos = 10
total_termos = 0
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = primeiro_termo
while mais_termos != 0:
    total_termos = mais_termos + total_termos
    while cont < total_termos:    
        print(f'{pa}', end=' -> ')
        pa = pa + razao
        cont += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos a mais quer mostrar? '))
print(f'Fim! Foram exibidos {total_termos} termos.')


#Segunda forma
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos vocês quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
