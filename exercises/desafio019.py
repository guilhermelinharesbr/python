"""Um professor que sortear um dos seus quatro alunos para 
apagar o quadro. Faça um programa que ajude ele, lendo o nome 
deles e escrevendo o nome do escolhido."""

#Primeira forma
import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
#No Python uma lista fica entre colchetes
lista = [aluno1,aluno2,aluno3,aluno4]
""""O método choice da classe random, escolhe de maneira 
aleatórica um dos itens da lista, no caso um dos alunos."""
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

#Segunda forma
from random import choice
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
#No Python uma lista fica entre colchetes
lista = [aluno1,aluno2,aluno3,aluno4]
""""O método choice da classe random, escolhe de maneira 
aleatórica um dos itens da lista, no caso um dos alunos."""
escolhido = choice(lista)
print('O aluno que foi escolhido: {}.'.format(escolhido))
