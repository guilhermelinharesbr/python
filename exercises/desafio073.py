"""
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.

B) Os últimos 4 colocados da tabela.

C) Uma lista com os times em ordem alfabética.

D) Em que posição na tabela está o time da Chapecoense.
"""

#Primeira forma
brasileirao_2021 = ('Atlético MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
                     'Bragantino','Fluminense', 'América MG', 'Atlético GO', 'Santos', 
                     'Ceará', 'Internacional', 'São Paulo', 'Athletico PR', 'Cuiabá',
                     'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Os 5 primeiros colocados do Brasileirão 2021 foram: {brasileirao_2021[0:5]}')
print(f'Os 4 últimos colocados do Brasileirão 2021 foram: {brasileirao_2021[16:20]}')
print(f'As equipes do Brasileirão 2021 em ordem alfabética são: {sorted(brasileirao_2021)}')
print(f'A equipe da Chapecoense ficou em {brasileirao_2021.index("Chapecoense")+1}º do Brasileirão 2021.')


#################


#Segunda forma
times = ('Atlético MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
                     'Bragantino','Fluminense', 'América MG', 'Atlético GO', 'Santos', 
                     'Ceará', 'Internacional', 'São Paulo', 'Athletico PR', 'Cuiabá',
                     'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão de 2021: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')
