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
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
