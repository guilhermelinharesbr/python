"""
Faça um programa que leia o sexo de uma pessoa, mas
só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
"""

#Primeira forma
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print(f'Escolha [M/F]: \n')
print(f'O seu sexo é {sexo}.')

#Segunda forma
"""O [0] pega apenas a primeira letra digitada"""
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
