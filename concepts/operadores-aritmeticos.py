# Operadores Aritméticos:
# + Adição -> Ex: 5+2==7
# - Subtração -> Ex: 5-2==3
# * Multiplicação -> Ex: 5*2==10
# / Divisão -> Ex: 5/2==2.5
# ** Potência -> Ex: 5**2==25
# // Divisão Inteira -> Ex: 5//2==2
# % Resto da Divisão -> Ex: 5%2==1
# == Igual
# = Atribuição ou também conhecido com Recebe.

#Ordem de Precedência dos Operadores Aritméticos:
# 1º são os parênteses -> ()
# 2º são as potências -> **
# 3º são a multiplicação '*', divisão '/', divisão inteira '//', resto da divisão '%' -> 
# 4º Soma e Subtração -> + e -

#####################

#Concatena as str Oi e Olá.
print('Oi'+'Olá')
#Imprime a str oi 3 vezes.
print('Oi'*3)
#Imprime o símbolo do = 15 vezes.
print('='*15)



#####################
nome=input('Qual é seu? ')
#Saída normal do nome digitado:
print('Prazer em te conhecer {}!'.format(nome))

#Mostra o nome digitado em 20 caracteres. Na Prática se digitar 
#'Guilherme' vai aparecer assim: 'Guilherme           !', ou seja Guilherme mais 
#11 espaços em branco e depois a exclamação:
print('Prazer em te conhecer {:20}!'.format(nome))

#Mostra o nome digitado em 20 caracteres, Alinhado a Direita, o símbolo '>' 
#indica que deverá ser alinhado a Direita. Na Prática se digitar 'Guilherme' 
#vai aparecer assim: '           Guilherme!', ou seja Guilherme! alinhado a direita:
print('Prazer em te conhecer {:>20}!'.format(nome))

#Mostra o nome digitado em 20 caracteres, Alinhado a Esquerda, o símbolo '<' 
#indica que deverá ser alinhado a Esquerda. Na Prática se digitar 'Guilherme' 
#vai aparecer assim: 'Guilherme           !', ou seja Guilherme! alinhado a esquerda, 
#basicamente é padrão já vir alinhado a esquerda:
print('Prazer em te conhecer {:<20}!'.format(nome))

#Mostra o nome digitado em 20 caracteres, de maneira Centralizada, o símbolo '^' 
#indica que deverá ser Centralizado. Na Prática se digitar 'Guilherme' 
#vai aparecer assim: '      Guilherme      !':
print('Prazer em te conhecer {:^20}!'.format(nome))

#Mostra o nome digitado em 20 caracteres, de maneira Centralizada, o símbolo '^' 
#indica que deverá ser Centralizado, porém com o detalhe que foi colocado 
#o símbolo '=' antes do '^' para que preenchesse os espaços vazios com o 
#símbolo '='. Na Prática se digitar 'Guilherme' vai aparecer assim: '=====Guilherme======!':
print('Prazer em te conhecer {:=^20}!'.format(nome))


#####################

n1=int(input('Um valor:'))
n2 = int(input('Outro valor:'))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao=n1 / n2
divisaoInteira = n1 // n2
exponeciacao = n1 ** n2
#O {:.3f} indica que só deverá mostra as 3 primeiras casas decimais.
#Por exemplo em uma divisão de '4 / 3 ==1.333' ao invés de '1.3333333333333333'
#\n é usado para quebra de linha.
#Este end='' é usado para não quebrar a linha entre uma função print() e a outra()
# Poderia ser end='>>>', com isso iria adicionar >>> no final da linha, mas 
#sem dar uma quebra de linha:
print('A soma é:{}, \n a subratação é:{}, a divisão é:{:.3f} '.format(soma,subtracao,divisao), end='')
print('A divisão inteira é:{}'.format(divisaoInteira),end='>>>')
print('e a potência é:{}'.format(exponeciacao))


