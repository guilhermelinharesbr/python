#Desenvolva um programa que leia as duas notas
#de um aluno, calcule e mostre a sua média.

#Primeira forma, usando várias variáveis
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = (nota1+nota2)/2
print('Sua média é:{}'.format(media))

#Segunda forma, usando apenas uma variável e nota com apenas
#uma casa decimal
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
print('Sua média é:{:.1f}'.format((nota1+nota2)/2))
