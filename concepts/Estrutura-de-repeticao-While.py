"""
Estrutura de repetição While

Quando NÃO souber a quantidade de vezes que a estrutura
precisará ser executada usa-se o While, se souber usa-se For.

O While é considerado uma estrutura de repetição com Teste lógico.
O For é considerado uma estrutura de repetição com Laço de Controle.

Ex1: while not maçã:
        passo
     pega

Ex2: while not maçã:
        if chão:
            passo
        if buraco:
            passo
        if moeda:
            pega     
     pega

"""

#Exemplos:
#Comparando uma mesma estrtura de repetição For com uma While
#For:
for c in range(1, 10):
    print(c)
print('Fim')

#While:
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')


#While, para quando n form diferente de zero.
#Ou, seja a condição de parada ou também conhecida como
#flag, será o número 0.
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')


#flag, será 'S'.
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')


#While, para quando n form diferente de zero,
#além disso, diz se o número digitado foi ímpar ou par.
#Outra coisa interessante é que aqui será mostrado como duas variáveis
#podem receber o mesmo valor em apenas uma linha, no caso as variáveis
# de nomes par e impar receberam o varlor 0.
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
