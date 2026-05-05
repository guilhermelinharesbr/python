"""
Escreva um programa que pergunte o salário de um funcionário 
e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.
"""

#Primeira forma
salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    aumento = ((salario * 10) / 100) + salario 
    print('Seu salário inicial era R${:.2f} e com o aumento passará para R${:.2f}'.format(salario,aumento))
if salario <= 1250:
    aumento = ((salario * 15) / 100) + salario 
    print('Seu salário inicial era R${:.2f} e com o aumento passará para R${:.2f}'.format(salario,aumento))

#Segunda forma
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100) 
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario,novo))
