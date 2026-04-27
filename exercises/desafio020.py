"""O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e 
mostre a orden sorteada."""

#Primeira forma
import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
""""O método shuffle da classe random embaralha os itens de uma
lista. Em português shuffle significa embaralhar."""
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

#Segunda forma
from random import shuffle
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
""""O método shuffle da classe random embaralha os itens de uma
lista. Em português shuffle significa embaralhar."""
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
