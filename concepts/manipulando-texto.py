"""
Manipulando Texto


Fatiamento de String

Ex:
frase='Curso em Vídeo Python'
       0123456789...     <- mricoespaços

A frase acima ocupa 21 microespaços, começa a contar do 0 e acaba no 20, os espaços em branco também contam um micro espaço.

frase[9]
Pega apenas a letra 'V', pois ela ocupa o microespaço número 9. No Python quando se está em parênteses significa que é uma lista.
frase[9:13]
Pegas as letras que ocupam dos índices 9 ao 13, mas tem um detalhe no Python ele exclui o último, no caso ficando 'Víde'.
Se quisesse pegar a palavra 'Vídeo' completa seria frase[9:14].

Uma forma de fatiar também seria frase[9:21], pegaria 'Vídeo Python'.

Outra forma de fatiar a lista frase[9:21:2], seria imprimir do índice 9 ao 21, lembrando que diminui 1, então ficando do índice 9 ao 20, e esse 2 no final significa que será pulando de 2 em 2 índices, ficando 'VdoPto'. 

Mais uma forma de fatiar, agora frase[:5], essa é forma reduzida de escrever frase[0:5], que mostraria 'Curso'.

Outra forma de fatiar, agora frase[15:], pega do índice 15 até o final, mostrando 'Python'.

Essa forma de fatiar, frase[9::3], indica que vai pegar do índice 9 até o final e pulando de 3 em 3 índices, mostrando 'VePh'.

----

Analisando uma String:

Ex:
frase='Curso em Vídeo Python'
       0123456789...     <- mricoespaços

len(frase)
O len vem de length que significa comprimento, ou seja esse método len() mostra que a String frase tem 21 caracteres.

frase.count('o')
O método count() acima conta quantas vezes a letra 'o' minúscula aparece na lista de nome frase, no caso a resposta foi 3.

frase.count('o',0,13)
Conta quantas vezes a letra 'o' minúscula aparece na lista de nome frase, no caso do índice 0 até 13, menos 1 ou seja até o 12, e o resultado é 1.

frase.find('deo')
O método find(), procura na lista frase a sequência 'deo' e retorno a posição do índice do primeiro caractere procurado no caso o 'd' e a resposta é 11.

frase.find('Android')
Será retornado o valor -1, pois ele tenta procurar na lista de nome frase a palavra 'Android' e como ele não encontrou ele retorna -1.

'Curso' in frase
Usando o operador 'in', para procurar a String 'Curso' dentro da lista de nome frase, e retorna True, pois existe essa String dentro desta lista.

----

Transformação de String:

Ex1:
frase='Curso em Vídeo Python'
       0123456789...     <- mricoespaços

frase.replace('Python,'Android')
O método replace() serve para procurar na lista de nome frase a String 'Python' e ao encontrar substituir ela por 'Android', e ficaria assim 'Curso em Vídeo Android'. Essa aletração é momentânea, para que ela seja definitiva é preciso atribuir a lista de nome frase como pode ser visto em:
frase = print(frase.replace('Python', 'Android')).

frase.upper()
O método upper() serve para deixar todos caracteres da lista de nome frase com letras maiúsculas.

frase.lower()
O método lower() serve para deixar todos caracteres da lista de nome frase com letras minúsculas.

frase.capitalize()
O método capitalize() serve para deixar todos caracteres da lista de nome frase com letras minúsculas e somente o primeiro caractere da primeira palavra em maiúsculo, ficando 'Curso em vídeo python'.

frase.title()
O método title() serve para deixar todos caracteres da lista de nome frase com letras minúsculas e depois ele pega palavra por palavra que estiver separada por um espaço em branco e colocando o primeiro caractére em maiúsculo, ficando 'Curso Em Vídeo Python'.


Ex2:
frase='   Aprenda Python  '
       0123456789...     <- mricoespaços
A lista acima é composta do índice 0 até o 18, sendo que do 0 a 2 são espaços em branco e do 17 ao 18 também.

frase.strip()
O método strip() serve para remover os espaços em branco que estirem antes do primeiro caractere e os que estiverem depois do último, muito útil para reduzir erros de digitação, o resultado será 'Aprenda Python' o 'A' que era o caractere de índice 3 passará ser o de índice 0, o 'p' que era o caractere de índice 4 passará a ser o 1 e assim por diante.

frase.rstrip()
No método rstrip() esse r vem de right ou seja direita e ele serve para remover os espaços em branco que estiverem a direita do último caractere, o resultado será '   Aprenda Python', reduzindo assim o tamanho da lista de 19 índices para 17.

frase.lstrip()
No método lstrip() esse l vem de left ou seja esquerda e ele serve para remover os espaços em branco que estiverem a esquerda do primeiro caractere, o resultado será 'Aprenda Python  ', reduzindo assim o tamanho da lista de 19 índices para 16.

----

Divisão de String:

Ex:
frase='Curso em Vídeo Python'
       0123456789...     <- mricoespaços

frase.split()
O método split() serve para fazer uma divisão das palavras da lista de nome frase, ficando 'Curso' 'em' 'Vídeo' 'Python', com o detalhe que antes era uma lista que ia do índice 0 ao 18, e agora o 'Curso' vai de 0 ao 4, o 'em' vai do 0 ao 1, o 'Vídeo' vai do 0 ao 4, o 'Python' vai do 0 ao 5. 

----

Junção de String:

Ex:
frase='Curso' 'em' 'Vídeo' 'Python'
       0123456789...     <- mricoespaços

'-'.join(frase)
O método join() serve para juntar os elementos da lista de nome frase, com o detalhe que serão juntos com o separador '-', ficando 'Curso-em-Vídeo-Python'

Obs: No Python tudo é um objeto.
"""

#########

frase = 'Curso em Vídeo Python'
print('1º: ',frase)
print('2º: ',frase[0])
print('3º: ',frase[3])
print('4º: ',frase[3:13])
print('5º: ',frase[:13])
print('6º: ',frase[13:])
print('7º: ',frase[1:15:2])
print('8º: ',frase[1::2])
print('9º: ',frase[::2])
#Abaixo é possível ver como imprimir um texto enorme, no caso basta usar o método print() e dentro dele colocar o texto entre aspas triplas. 
print('10º: ',"""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")
print('11º: ',frase.count('o'))
print('12º: ',frase.count('O'))
#Abaixo pode-se ver que primeiro converte os caracteres para maiúsculo para só depois contar as letra 'O' maiúsculas.
print('13º: ',frase.upper().count('O'))
print('14º: ',len(frase))
print('15º: ',len(frase.strip()))

frase2 = '    Curso em Vídeo Python   '
print('16º: ',len(frase2))
print('17º: ',len(frase2.strip()))

#Abaixo é provado que o método replace não salva a mudança a menos que seja feita uma atribuição. Uma String é imutável, a menos que seja utilizado um método de substituição e depois seja feita uma atribuição.
print('18º: ',frase.replace('Python', 'Android'))
print('19º: ',frase)
frase = frase.replace('Python', 'Android')
print('20º: ',frase)

print('21º: ','Curso' in frase )
print('22º: ',frase.find('Curso'))
print('23º: ',frase.find('Vídeo'))
print('24º: ',frase.find('vídeo'))
print('25º: ',frase.lower().find('vídeo'))

print('26º: ',frase.split())
dividido = frase.split()
print('27º: ',dividido[0])
print('28º: ',dividido[1])
print('29º: ',dividido[2])
print('30º: ',dividido[3])
#Abaixo ele pega o elemento de índice 2 na lista de nome frase, que no caso é 'Vídeo' e imprime o caractere de índice 3 que no caso é 'e', lembrando que sempre começa do 0.
print('31º: ',dividido[2][3])
