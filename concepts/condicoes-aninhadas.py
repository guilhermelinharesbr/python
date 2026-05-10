"""
Condições aninhadas: 
 Em Python permitem colocar estruturas if, 
elif ou else dentro de outros blocos condicionais para verificar 
múltiplas condições sequenciais. Elas exigem endentação correta 
para definir o escopo de cada verificação. Embora úteis, o uso 
excessivo pode prejudicar a legibilidade, sendo recomendado usar 
operadores lógicos (and, or) para simplificar, quando possível.

elif -> Em Python 'elif' é simplicação do nome da junção do else
        com o if. 

Obs: Sempre terá por um if e nunca poderá começar com um elif e 
     nem sempre terá o else. O elif e o else são opcionais,
     até mesmo quando usa o elif o else é opcional. 
Obs2: Dentro de um if você pode utilizar quantos elif você quiser,
      e dentro deste mesmo if o else pode ser utilizado apenas uma
      vez ou nenhuma.
      

Ex:
carro.siga()
if carro.esquerda():
    bloco1
elif carro.direita():
    bloc2
elif carro.ré():
    bloco3
else:
    bloco4
"""

#Prática

#Condição Simples
nome = str(input('Qual é o seu nome? '))
if nome == 'Guilherme':
    print('Você é meu chará.')
print('Tenha um bom dia, {}!'.format(nome))

#Condição Composta
nome = str(input('Qual é o seu nome? '))
if nome == 'Guilherme':
    print('Você é meu chará.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#Condição Aninhada
nome = str(input('Qual é o seu nome? '))
if nome == 'Guilherme':
    print('Você é meu chará.')
elif nome == 'Maria' or nome == 'João' or nome == 'José':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Emanuele':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#Condição Aninhada sem else
nome = str(input('Qual é o seu nome? '))
if nome == 'Guilherme':
    print('Você é meu chará.')
elif nome == 'Maria' or nome == 'João' or nome == 'José':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Emanuele':
    print('Belo nome feminino.')
print('Tenha um bom dia, {}!'.format(nome))
