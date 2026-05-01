"""
Faça um programa que leia um número de 0 a 9.999 e mostre na 
tela cada um dos dígitos separados.

Ex: Digite um número:1834

Unidade:4
Dezena:3
Centena:8
Milhar:1
"""

#Primeira forma
numero = str(input('Digite um número de 0 a 9.999:'))
numero.split()
print('Unidade {}'.format(numero[3]))
print('Dezena {}'.format(numero[2]))
print('Centena {}'.format(numero[1]))
print('Milhar {}'.format(numero[0]))

#Segunda forma
numero = int(input('Informe um número de 0 a 9.999:'))
numero_em_string = str(numero)
print('Analisando o número {}'.format(numero))
print('Unidade {}'.format(numero_em_string[3]))
print('Dezena {}'.format(numero_em_string[2]))
print('Centena {}'.format(numero_em_string[1]))
print('Milhar {}'.format(numero_em_string[0]))

#Terceira forma
numero = int(input('Informe um número de 0 a 9.999:'))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o seu número {}'.format(numero))
print('Unidade {}'.format(unidade))
print('Dezena {}'.format(dezena))
print('Centena {}'.format(centena))
print('Milhar {}'.format(milhar))
