"""
Variáveis Compostas - TUPLAS

Tuplas são estruturas de dados utilizadas para armazenar
uma coleção ordenada de elementos. Elas são muito parecidas 
com as Listas, mas com uma diferença crucial: elas são imutáveis.

Para entender o conceito de forma simples, pense nelas através 
destas três características principais:

Imutáveis: Uma vez criada uma tupla, não pode alterar, adicionar, 
remover ou substituir nenhum elemento dela até o fim do programa.
Ou seja, enquanto o programa está parada pode-se mexer na tupla, 
porém ela estando em execução não pode-se editar ela.

Sintaxe: Enquanto as listas usam colchetes [ ], as tuplas 
são definidas utilizando parênteses ( ).

Uso ideal: São perfeitas para guardar dados que nunca devem mudar, 
como os dias da semana, os meses do ano, ou as coordenadas geográficas 
(Latitude, Longitude) de um mapa.

Em resumo: se precisa de uma lista de coisas que pode mudar, use Lista. Se precisa de uma lista de coisas que deve ficar protegida contra alterações, use Tupla.

Os índices das TUPLAS começam do 0.

"""


''' Exemplo 1:
Criando uma tupla, com 5 elementos, começando do 0 ao 4. Atenção que a tupla usa () e não [], apesar que no python mais modernos não precisa mais nem usar os (): '''
dias_da_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')

# Você consegue acessar os dados normalmente:
print(dias_da_semana[0])  # Vai mostrar: Segunda
print('--')
print(dias_da_semana[3])  # Vai mostrar: Quinta
print('--')
print(dias_da_semana)  # Vai mostrar: Todos os elementos da Tupla
print('--')
print(dias_da_semana[0:2])  # Vai mostrar: Segunda e Terça, porque o último elemento é ignorado, ou seja só mostra os elementos [0] e [1] e não mostra o [2]
print('--')
print(dias_da_semana[1:])  # Vai mostrar: o conteúdo a partir do elemento [1] da tupla até o final dela, ou seja, de Terça até Sexta.
print('--')
print(dias_da_semana[-1]) # Vai mostrar: Sexta. Porque é o último elemento menos 1.
print('--')
print(dias_da_semana[-3]) # Vai mostrar: Quarta. Porque é o último elemento menos 3.
print('--')
print(dias_da_semana[-4]) # Vai mostrar: Terça. Porque é o último elemento menos 4.
print('--')
print (len(dias_da_semana))  # Mostra o total de elementos da Tupla, no caso 5.
# Mas se você tentar alterar, o Python dará um erro:
#dias_da_semana[0] = 'Domingo'    # Erro! TypeError: 'tuple' object does not support item assignment

#Imprime os elementos da Tupla:
for c in dias_da_semana:
    print(f'{c}, ' , end='')

print('--')
print('--')

''' Exemplo 2:
Variáveis compostas usando lanches: '''
lanche = 'Hambúguer', 'Suco', 'Pizza', 'Pudim'
# É possível notar que os elementos da tupla aparecem entre () no print:
print(lanche)
print('--')
print(lanche[1])
print('--')
print(lanche[3])
print('--')
print(lanche[-1])
print('--')
print(lanche[-2])
print('--')
print(lanche[1:3])
print('--')
print(lanche[-2:])
print('--')
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('--')

#Imprime um item da tupla por linha:
for cont in range(0, len(lanche)):
    print(lanche[cont])

print('--')

for comida in lanche:
    print(f'Eu vou comer {comida} ')

print('--')

#Imprime um item da tupla por linha e diz a posição - primeira forma:
for cont in range(0, len(lanche)):
    print(f' Eu vou comer {lanche[cont]} na posição {cont}')

print('--')

#Imprime um item da tupla por linha e diz a posição - segunda forma:
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

print('--')

#Imprime em ordem alfabética:
print(sorted(lanche))

print('--')

''' Exemplo 3:
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print(a)
print('--')
print(b)
print('--')
print(c)
print('--')
print(d)
print('--')
print(len(d))
print('--')
# Conta quantas vezes está aparecendo o número 5 dentro de 'd'.
print('O número 5 apareceu', d.count(5), 'vezes')
print('O número 9 apareceu', d.count(9), 'vezes')
print(d)
print('--')
print('O index do número 8 na tupla d é', d.index(8))
# O index() pega o primeiro 5 da tupla.
print('O index do número 2 na tupla d é', d.index(2))
print('O index do número 2 na tupla d limitado para começar do índice 4 é', d.index(2,4))
print('--')

''' Tuplas em Python são similares aos vetores em Java, mas com o detalhe que
as tuplas em Python permitem o uso de tipos diferentes, já os vetores não.
Exemplo 4: 
A tupla 'pessoa' tem o nome 'Maria' do tipo string, a idade '31' do tipo int
o sexo 'F' do tipo string e o peso '76.50' do tipo int.
'''
pessoa = ('Maria', 31, 'F', 76.50)
print(pessoa)

''' Deleta a tupla 'pessoa', excluir ela inteira, e não é possível
excluir um item da tupla, ou deleta ela inteira ou não deleta. 
Após deletar a tupla não é possível usar mais nenhum conteúdo 
dela, ou seja não é possível usar nem um 'print()' após deletar 
a tupla, pois se não dará o erro "NameError: name 'pessoa' is not defined" 
e se tentar deletar apenas um item da tupla dará o erro 
"TypeError: 'tuple' object doesn't support item deletion": '''
del(pessoa)
