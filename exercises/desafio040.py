"""
Crie um programa que leia duas notas de um aluno e 
calcule sua média, mostrando uma mensagem no final, 
de acordo com a média atingida:

- Média abaixo de 5.0:
REPROVADO

- Média entre 5.0 e 6.9:
RECUPERAÇÃO

- Média 7.0 ou superior:
APROVADO
"""

#Primeira forma
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Sua média foi {} e por isso você foi REPROVADO.'.format(m))
elif m >= 7 :
    print('Sua média foi {} e por isso você foi APROVADO.'.format(m))
else:
    print('Sua média foi {} e por isso você ficou de RECUPERAÇÃO.'.format(m))

#Segunda forma
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2,media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está APROVADO.')
