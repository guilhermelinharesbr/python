#Faça um algoritmo que leia o salário de um funcionário e mostre
#seu novo salário, com 15% de aumento.

#Primeira forma
salario = float(input('Qual é o salário do Funcionário? R$'))
aumento = (salario*15)/100
novo_salario = (salario+aumento)
print('Um funcionário uqe ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,novo_salario))

#Segunda forma
salario = float(input('Qual é o salário do Funcionário? R$'))
novo_salario = salario+(salario*15)/100
print('Um funcionário uqe ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,novo_salario))
