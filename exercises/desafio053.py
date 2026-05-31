"""
Crie um programa que leia uma frase qualquer e diga 
se ela é um palíndromo, desconsiderando os espaços.

Ex: APOS A SOPA.
    A SACADA DA CASA 
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA

Obs: Pode desconsiderar os acentos.    
"""

#Primeira forma
"""
frase = str(input('Digite uma frase: ')).strip()
print(frase)
"""


#Segunda forma
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')

#Terceira forma
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')
