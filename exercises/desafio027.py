"""
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.

Ex:Ana Maria de Souza
primeiro:Ana
último:Souza
"""

#Primeira forma
nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
nome_dividido = nome.split()
print('Seu primeiro nome é {}'.format(nome_dividido[0]))
#Para pegar o último item de uma lista é utilizando o índice negativo [-1]. 
#Essa sintaxe funciona sem precisar saber o tamanho total da lista:
print('Seu último nome é {}'.format(nome_dividido[-1]))

#Segunda forma
n = str(input('Digote seu nome completo:')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu primeiro nome é {}'.format(nome[len(nome)-1]))
