"""
Faça um programa que mostre a tabuada de vários
números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando
o número for negativo.
"""

#Primeira forma
while True:
    num = int(input('Quer ver a tabuada de qual Nº?(dgite um Nº negativo para parar): '))
    if num < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{num}  x  {cont:2} = {num * cont}')
        cont += 1
print('-'*12 , 'Fim do programa' , '-'*12)


#################

#Segunda forma
while True:
    n = int(input('Quer ver a tabuada de qual Nº? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n}  x  {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
