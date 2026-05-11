"""
Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

#Primeira forma
numero = int(input('Digite um número inteiro: '))
opcoes = int(input('Escolha a base de conversão:\n [1] para converter para BINÁRIO\n'
'[2] para converter para OCTAL\n [3] para converter para HEXADECIMAL\n Sua opção: '))
if opcoes == 1:
    print('1')
elif opcoes == 2:
    print('2')
elif opcoes == 3:
    print('3')
else:
    print('Opção incorreta.')


#Segunda forma