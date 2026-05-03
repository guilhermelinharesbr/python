"""
Estruturas condicionais

Os blocos do if e do else precisam ser identados usando a tecla TAB.

Ex:
if carro.esquerda():
    bloco True
else:
    bloco False

Ex2:
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--Fim--')

Ex3:
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--Fim--')

Obs: O Python não tem um operador ternário.
O operador ternário é uma forma concisa de escrever estruturas condicionais if-else em uma única linha, utilizando a sintaxe condição ? expressão1 : expressão2. Ele avalia a condição: se for verdadeira, retorna expr1; caso contrário, retorna expr2, sendo ideal para atribuições simples e melhor legibilidade.
Algumas linguagens possuem operador ternário, como Java, PHP, C.

Obs2: O Python trabalha com identação, com o TAB.

Obs3: Quando tem apenas o if é chamado estrtura condicional simples, quando tem o if e o else é chamado de estrutura condicional composta.

Obs4: O if e o else terminam com os dois pontos ':' .

"""

#Estrtura condicional Simples
nome = str(input('Qual é seu nome? '))
if nome == 'Guilherme':
    print('Você é meu chará.')
print('Bom dia, {}'.format(nome))

#Estrtura condicional Composta
sobrenome = str(input('Qual é seu sobrenome? '))
if sobrenome == 'Linhares':
    print('Você é meu parente.')
else:
    print('Você Não é meu parente.')
print('Bom dia, {}'.format(sobrenome))

#Estrtura condicional Composta - Tirar média das notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim!')

#Estrtura condicional Simplificada - Tirar média das notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns!' if m >= 6 else 'Estude mais!')
