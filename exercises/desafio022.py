"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

-> O nome com todas as letras maiúsculas

-> O nome com todas minúsculas

-> Quantas letras ao todo(sem considerar espaços)

-> Quantas letras tem o primeiro nome.
"""

#Primeira forma
nome = input('Digite seu nome completo:')
print('Seu nome em maiúsculas é' , nome.upper())
print('Seu nome em minúsculas é' , nome.lower())
nome_sem_espaco_em_branco = nome.split()
nome_sem_espaco_em_branco = '-'.join(nome_sem_espaco_em_branco)
print('Seu nome ao todo tem {} letras.'.format(len(nome_sem_espaco_em_branco.replace('-',''))))
primeiro_nome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(primeiro_nome[0],len(primeiro_nome[0])))

#Segunda forma
nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))

#Terceira forma
nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0],len(separa[0])))
