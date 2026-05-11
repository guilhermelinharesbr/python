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
    print('O número {} em BINÁRIO é {}'.format(numero,bin(numero)))
elif opcoes == 2:
    print('O número {} em OCTAL é {}'.format(numero,oct(numero)))
elif opcoes == 3:
    print('O número {} em HEXADECIMAL é {}'.format(numero,hex(numero)))
else:
    print('Opção incorreta.')

#######

#Segunda forma
num = int(input('Digite um número inteiro: '))
#Quando usa-se as aspas simples triplas elas podem ser usadas para escrever
#textos grandes, sem a necessidades de usar o \n para quebra de linha.
print ('''Escolha um das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
#É preciso usar o [2:] para remover o código 0b que é referente ao binário no Python.
    print('{} convertido par BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
#É preciso usar o [2:] para remover o código 0o que é referente ao octal no Python.
    print('{} convertido par OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
#É preciso usar o [2:] para remover o código 0x que é referente ao hexadecimal no Python.
    print('{} convertido par HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
