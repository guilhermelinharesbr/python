"""
Crie um programa que leia a idade e o sexo
de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer 
ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.

B) Quantos homens foram cadastrados.

C) Quantas mulheres tem menos de 20 anos.
"""

#Primeira forma
total_pessoas = maiores_18 = masculino = feminino = mulheres_jovens = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo?[M/F] ')).strip().upper()[0]
    if idade > 18:
        maiores_18 += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F':
        feminino += 1
    if sexo == 'F' and idade < 20:
        mulheres_jovens += 1
    continuar = ' '    
    continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if continuar == 'S':
        total += 1
    if continuar == 'N':
        total += 1
        break
print(f'''Fim do programa.
Foram cadastradas {total} pessoas.
Desse total temos {maiores_18} maiores de 18 anos.
Além disso, temos pessoa(s) {masculino} do sexo masculino {feminino} do sexo feminino.
Dessas pessoa(s) do sexo femino {mulheres_jovens} tem menos de 20 anos.''')


#################


#Segunda forma
# Inicializando as variáveis com nomes bem claros
total_pessoas = maiores_18 = total_homens = mulheres_sub20 = 0

print('-' * 25)
print('   CADASTRO DE PESSOAS   ')
print('-' * 25)

while True:
    idade = int(input('Idade: '))
    
    # 1. Validação do Sexo (Não sai do loop enquanto não digitar M ou F)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    
    # Contagem geral de pessoas cadastradas
    total_pessoas += 1
    
    # A) Quantas pessoas tem mais de 18 anos
    if idade > 18:
        maiores_18 += 1
        
    # B) Quantos homens foram cadastrados
    if sexo == 'M':
        total_homens += 1
        
    # C) Quantas mulheres tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_sub20 += 1
        
    # 2. Validação do Continuar (Não sai do loop enquanto não digitar S ou N)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    print('-' * 25)
    
    # Se o usuário escolher Não, o loop principal é interrompido
    if continuar == 'N':
        break

# Print final encostado na esquerda para não desalinhar no terminal
print(f'''
================ RESULTADO ===============
Foram cadastradas um total de {total_pessoas} pessoas.
A) Maiores de 18 anos: {maiores_18} pessoa(s).
B) Homens cadastrados: {total_homens} no total.
C) Mulheres com menos de 20 anos: {mulheres_sub20} mulher(es).
==========================================''')


#################


#Terceira forma
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
