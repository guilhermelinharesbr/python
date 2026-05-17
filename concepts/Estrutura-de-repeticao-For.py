"""
Estrutura de repetição For

Laço de variável de controle
Estrtura de controle condicional

Ex1: for c in range(1,10):
        passo
     pega

Ex2: for c in range(0,3):
        passo
        pula
     passo
     pega

Ex3: for c in range(0,3):
        passo
        pula
     passo
     pega 

Ex4: for c in range(0,3):
        if moeda:
            pega
        passo
        pula
     passo
     pega 

"""

#Exemplos:

#Esse FOR imprime em tela 4 vezes a palavra
# 'Oi', pois no Python ele não executa a útlima vez
# e depois de imprimir as 4 vezes a palavra 'Oi' ele imprime 'FIM'
for c in range(1,5):
    print('Oi')
print('FIM')

#Esse FOR imprime em tela 6 vezes a palavra
# 'Oi', pois no Python ele não executa a útlima vez, e como comecei do 0 ele conta de 0 a 5 e depois no 6 ignora, depois de imprimir as 6 vezes a palavra 'Oi' ele imprime 'FIM'
for c in range(0,6):
    print('Oi')
print('FIM')

#Esse FOR imprime em tela os números de 1 a 6, depois de imprimir os números ele imprime 'FIM'
for c in range(1,7):
    print(c)
print('FIM')

#Esse FOR imprime em tela os números de 6 a 1 de maneira decrescente, depois de imprimir os números ele imprime 'FIM'. Vale ressaltar que o '-1' é para ir reduzindo menos do número 6 até chegar no 1, visto que o 0 será ignorado, por ser o último número da sequência.
for c in range(6,0, -1):
    print(c)
print('FIM')


#Esse FOR imprime em tela os números de 0 a 6, com o detalhe que o '2' indica que será de 2 em 2, então serão impressos 0,2,4,6, depois de imprimir os números ele imprime 'FIM'.
for c in range(0, 7, 2):
    print(c)
print('FIM')

#
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

#
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

# Para pedir para digitar o valor 3 vezes
for c in range(0,3):
    n = int(input('Digite um valor: '))
print('FIM')

# Para pedir para digitar o valor 3 vezes
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    # É o mesmo que 's = s + n':
    s += n
print('O somatório de todos os valores foi {}'.format(s))
