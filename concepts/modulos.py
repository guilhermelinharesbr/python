#Módulos
#Bibliotecas
#Comando import
#import bebidas
#import doce -> importas todos os doces
#from doce import pudim -> importa apenas o pudim
#Biblioteca math
#import math -> já vem por padrão no python?
#Biblioteca math, funcionalidade ceil"arredonda um número para cima". Funcionalidade floor "arredonda pra baixo", funcionalidade trunc elimina as informações após a vírgula de um número. A funcionalidade pow é usada para a potência. A funcionalidade sqrt calcula a raiz quadrada.  A funcionalidade factorial faz cálculos de fatorial.
# Ao rodar:
#import math
#Está sendo importado por exemplo as funcionalidades ceil,floor,trunc,pow,sqrt,factorial.

#Ao rodar:
#from math import sqrt
#Importa apenas a funcionalidade sqrt da biblioteca math

#from math import sqrt,ceil
#Importa apenas as funcionalidades sqrt e ceil da biblioteca math


#Exercício de exemplo. Digitar 29 para entender a diferença nos resultados
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz ' \
'de {} é igual a {:.2f}'.format(num,raiz))


import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz ' \
'de {} é igual a {}'.format(num,math.ceil(raiz)))

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz ' \
'de {} é igual a {}'.format(num,math.floor(raiz)))


#Segundo exemplo
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz ' \
'de {} é igual a {}'.format(num,raiz))

#ANOTAR que estou estudando na versão 3.10.12 e desde dia 21/04/26

# Para consultar as bibliotecas é acessando o site python.org -> Documentation -> Docs -> Library Reference ->

#Biblioteca random
import random
#O método random da classe random gera um número float aleatório entre 0 e 1.
num =random.random()
print(num)
#O método randint gera um número aleatório entre 1 e 10
num2=random.randint(1,10)
print(num2)

#Se você digitar import e depois segurar CTrl + espaço, serão mostradas todas as bibliotecas que podem ser importadas. São mostradas inclusive as bibliotecas que são built-in, ou seja já vem com o python, no Pycharm mostra se é built-in ou não, já no VS Code não mostra.

#No site do Python ao clicar em PyPI é aberta a página do Python Packge Index, que é o índice de pacotes python. Neste local um programador pode criar a sua biblioteca e disponibilizar para que outros programados possam usar ela nos seus programas. 
#Ao buscar por internet, são visto os módulos que tem o nome internet? 
#Ao buscar por emoji, é vista abiblioteca emoji 2.15.0, com ela pode-se usar emojis nos códigos. Pode-se procurar por "Emoji Cheat Sheet" lá mostram os Emoji em inglês.

#Descobrir como instalar a biblioteca emoji no Pycharm e no VS Code.
#import emoji