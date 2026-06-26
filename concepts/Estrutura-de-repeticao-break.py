"""
Estrutura de repetição - INTERROMPENDO repetições while - break

O comando break em Python serve para interromper e sair imediatamente de um laço de repetição (while ou for), mesmo que a condição desse laço ainda seja verdadeira.

Imagine que ele funciona como um "botão de emergência" ou uma "saída de segurança". Quando o Python encontra a palavra break, ele quebra a engrenagem do loop na mesma hora e pula para a primeira linha de código que estiver logo após o laço.


Ex1: while true:
        if chão:
            passo
        if buraco:
            passo
        if moeda:
            pega
        if troféu:
            pula
            break         
     pega

     
Ex2:
while True:
    nome = str(input('Digite um nome (ou "sair" para parar): '))
    if nome == 'sair':
        break # O programa para na hora e sai do loop
    print(f'Olá, {nome}!')

print('Programa encerrado!')

Obs: No exemplo acima, o while True criaria um loop infinito, mas o break garante que o programa tenha uma saída assim que o usuário digitar "sair". É uma ferramenta essencial para controlar fluxos onde não sabe-se exatamente quantas vezes a repetição vai precisar rodar.

"""

#Exemplos:
# Mostrando o uso do break.
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
