"""
Refaça o desafio 035 dos triânculos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais

- Isósceles: dois lados iguais

- Escaleno: todos os lados diferentes
"""

#Primeira forma
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a and a == b and a == c:
    print('Os segmentos acima PODEM formar um triângulo. Este é um triângulo EQUILÁTERO.')
elif a + b > c and a + c > b and b + c > a and a == b and a != c or a != b and a == c:
        print('Os segmentos acima PODEM formar um triângulo. Este é um triângulo ISÓSCELES.')
elif a + b > c and a + c > b and b + c > a and a != b and a != c:
        print('Os segmentos acima PODEM formar um triângulo. Este é um triângulo ESCALENO.')  
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')


#Segunda forma
print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    #Esse end='' significa que não é para ter nada no final da linha, 
    #nem mesmo uma quebra de linha:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
         print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
         print('ESCALENO!')
    else:
         print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')
