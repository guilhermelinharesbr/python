"""
Faça um programa que leia três números e mostre qual é 
o maior e qual é o menor.
"""

#Primeira forma
primeiro_num = int(input('Digite o primeiro número: '))
segundo_num = int(input('Digite o segundo número: '))
terceiro_num = int(input('Digite o terceiro número: '))
# 1º maior e 2º menor
if primeiro_num > segundo_num and primeiro_num > terceiro_num and segundo_num < primeiro_num and segundo_num < terceiro_num:
    print('O número {} é o maior dos três e o número {} é menor dos três'.format(primeiro_num,segundo_num))

# 1º maior e 3º menor
if primeiro_num > segundo_num and primeiro_num > terceiro_num and terceiro_num < primeiro_num and terceiro_num < segundo_num:
    print('O número {} é o maior dos três e o número {} é menor dos três'.format(primeiro_num,terceiro_num))

# 2º maior e 1º menor
if segundo_num > primeiro_num and segundo_num > terceiro_num and primeiro_num < segundo_num and primeiro_num < terceiro_num:
    print('O número {} é o maior dos três e o número {} é menor dos três'.format(segundo_num,primeiro_num))

# 2º maior e 3º menor
if segundo_num > primeiro_num and segundo_num > terceiro_num and terceiro_num < primeiro_num and terceiro_num < segundo_num:
    print('O número {} é o maior dos três e o número {} é menor dos três'.format(segundo_num,terceiro_num))

# 3º maior e 1º menor
if terceiro_num > primeiro_num and terceiro_num > segundo_num and primeiro_num < segundo_num and primeiro_num < terceiro_num:
    print('O número {} é o maior dos três e o número {} é menor dos três'.format(terceiro_num,primeiro_num))

# 3º maior e 2º menor
if terceiro_num > primeiro_num and terceiro_num > segundo_num and segundo_num < primeiro_num and segundo_num < terceiro_num:
    print('O número {} é o maior dos três e o número {} é menor dos três'.format(terceiro_num,primeiro_num))

# Números iguais
if primeiro_num == segundo_num == terceiro_num:
    print('Os três números são iguais.')

#########################################################################

#Segunda forma
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#Verificando quem é menor
menor = a
if b < c and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digutado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
