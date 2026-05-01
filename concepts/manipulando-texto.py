"""
Manipulando texto


Fatiamento de String

Ex:
frase='Curso em Vídeo Python'

A frase acima ocupa 21 microespaços, começa a contar do 0 e acaba no 20, os espaços em branco também contam um micro espaço.

frase[9]
Pega apenas a letra 'V', pois ela ocupa o microespaço número 9. No Python quando se está em parênteses significa que é uma lista.
frase[9:13]
Pegas as letras que ocupam dos índices 9 ao 13, mas tem um detalhe no Python ele exclui o último, no caso ficando 'Víde'.
Se quisesse pegar a palavra 'Vídeo' completa seria frase[9:14].

Uma forma de fatiar também seria frase[9:21], pegaria 'Vídeo Python'.

Outra forma frase[9:21:2], seria imprimir do índice 9 ao 21, lembrando que diminui 1, então ficando do índice 9 ao 20, e esse 2 no final significa que será pulando de 2 em 2 índices, ficando 'VdoPto' 

Mais uma forma de fatiar, agora frase[:5], essa é forma reduzida de escrever frase[0:5], que mostraria 'Curso'

Outra forma de fatiar, agora frase[15:], pega do índice 15 até o final, mostrando 'Python'.

Essa forma de fatiar, frase[9::3], indica que vai pegar do índice 9 até o final e pulando de 3 em 3 índices, mostrando 'VePh'.

----

Analisando uma String:

Ex:
frase='Curso em Vídeo Python'

len(frase)  -> len vem de length que significa comprimento, ou seja esse método len() mostra que a String frase tem 21 caracteres.

frase.count('o')
O método count() acima conta quantas vezes a letra 'o' minúscula aparece na lista de nome frase, no caso a resposta foi 3.

frase.count('o',0,13)
Conta quantas vezes a letra 'o' minúscula aparece na lista de nome frase, no caso do índice 0 até 13, menos 1 ou seja até o 12, e o resultado é 1.

frase.find('deo')
O método find(), procura na lista frase a sequência 'deo' e retorno a posição do índice do primeiro caractere procurado no caso o 'd' e a resposta é 11.

frase.find('Android')
será retornado o valor -1, pois ele tenta procura na lista de nome frase a palavra 'Android' e como ele não encontrou ele retorna -1.

'Curso' in frase
Usando o operador 'in', para procurar a String 'Curso' dentro da lista de nome frase, e retorna True, pois existe essa String dentro desta lista.

----

Transformação de String:

Ex1:
frase='Curso em Vídeo Python'

frase.replace('Python,'Android')
o método replace() serve para procurar na lista de nome frase a String 'Python' e ao encontrar substituir ela por 'Android', e ficaria assim 'Curso em Vídeo Android'.

frase.upper()
o método upper() serve para deixar todos caracteres da lista de nome frase com letras maiúsculas.

frase.lower()
o método lower() serve para deixar todos caracteres da lista de nome frase com letras minúsculas.

frase.capitalize()
o método capitalize() serve para deixar todos caracteres da lista de nome frase com letras minúsculas e somente o primeiro caractere em maiúsculo, ficando 'Curso em vídeo python'.

frase.title()
o método title() serve para deixar todos caracteres da lista de nome frase com letras minúsculas e depois ele pega palavra por palavra que estiver separada por um espaço em branco e colocando o primeiro caractére em maiúsculo, ficando 'Curso Em Vídeo Python'.


Ex2:
frase='   Aprenda Python  '
A lista acima é composta do índice 0 até o 18, sendo que do 0 a 2 são espaços em branco e do 17 ao 18 também.

frase.strip()
O método strip() serve para remover os espaços em branco que estirem antes do primeiro caractere e os que estiverem depois do último, muito útil para reduzir erros de digitação, o resultado será 'Aprenda Python' o 'A' que era o caractere de índice 3 passará ser o de índice 0, o 'p' que era o caractere de índice 4 passará a ser o 1 e assim por diante.

frase.rstrip()
O método rstrip() esse r vem de right ou seja direita e ele serve para remover os espaços em branco que estiverem a direita do último caractere, o resultado será '   Aprenda Python', reduzindo assim o tamanho da lista de 19 índices para 17.

frase.lstrip()
O método lstrip() esse l vem de left ou seja esquerda e ele serve para remover os espaços em branco que estiverem a esquerda do primeiro caractere, o resultado será 'Aprenda Python  ', reduzindo assim o tamanho da lista de 19 índices para 16.

----

Divisão de String:

Ex:
frase='Curso em Vídeo Python'

frase.split()
o método split() serve para fazer uma divisão das palavras da lista de nome frase, ficando 'Curso' 'em' 'Vídeo' 'Python', com o detalhe que antes era uma lista que ia do índice 0 ao 18, e agora o 'Curso' vai de 0 ao 4, o 'em' vai do 0 ao 1, o 'Vídeo' vai do 0 ao 4, o 'Python' vai do 0 ao 5. 

----

Junção de String:

Ex:
frase='Curso' 'em' 'Vídeo' 'Python'

'-'.join(frase)
O método join() serve para juntar os elemntos da lista de nome frase, com o detalhe que serão juntos com o separador '-', ficando 'Curso-em-Vídeo-Python'

Observação no Python tudo é um objeto.
"""

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[0])
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
#Esse print acima primeiro converte os caracteres para maiúsculo para só depois contar as letra 'O' maiúsculas.
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase)
frase = print(frase.replace('Python', 'Android'))
#Uma String imutável, a menos que seja utilizado um método de substituição e depois seja feita uma atribuição.
print('Curso' in frase )
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

