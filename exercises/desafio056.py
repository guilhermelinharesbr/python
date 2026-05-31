"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

#Primeira forma
masculino = 0
feminino = 0
total_idade = 0
homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_jovens = 0
for pessoa in range(1,5):
    print(f'{"=" * 10} Pessoa {pessoa} {"=" * 10}')
    nome = str(input('Qual o seu nome? ')).strip()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo? (M/F): ')).strip().upper()
    total_idade += idade
    if sexo == 'M':
        masculino += 1
        if homem_mais_velho == 0 or idade > homem_mais_velho:
            homem_mais_velho = idade
            nome_homem_mais_velho = nome
    else:
        feminino += 1
        if idade < 20:
            mulheres_jovens += 1
media = (total_idade) / pessoa
print(f'{"=" * 15} RESULTADO FINAL {"=" * 15}')
print(f'A média de idade deste grupo de pessoas é de {media} nos.')
print(f'Tem {masculino} pessoa(s) do sexo Masculino e {feminino} pessoa(s) do sexo Feminino.')
print(f'O Homem mais velho tem {homem_mais_velho} anos e o nome dele é {nome_homem_mais_velho}.')
print(f'De um total de {feminino} Mulhere(s), {mulheres_jovens} tem menos de 20 anos.')


#Segunda forma
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:' )).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
