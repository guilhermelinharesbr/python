"""
Refaça o DESAFIO 009, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for.
"""

#Primeira forma
valor = int(input('Digite um número para ver sua tabuada: '))
cont = 0
print('-'*12)
for c in range(1, 11):
    cont = cont + 1
    print(valor, ' x ', (cont), ' = ', (valor * cont))

print('=' * 20) 
###############################

#Segunda forma
num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for c in range(1, 11):
    print('{}  x  {:2} = {}'.format(num, c, num * c))
