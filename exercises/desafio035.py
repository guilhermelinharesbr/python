"""
Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não forma um triângulo.
"""

#Primeira forma
print('-=-' * 20)
print('Verificador de Triângulos')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos PODEM formar um triângulo.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')


#Segunda forma
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')
