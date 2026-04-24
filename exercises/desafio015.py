#Escreva um programa que pergunte a quantidade de Km
#percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

#Primeira forma
dias = int(input('Por quantos dias o carro foi alugado?'))
quilometros_rodados = float(input('Quantos Km rodados?'))
diaria_carro = float (60)
valor_por_km = float (0.15)
valor_a_pagar = float((diaria_carro * dias) + (quilometros_rodados * valor_por_km))
print('O total a pagar é de R${:.2f}'.format(valor_a_pagar))

#Segunda forma
dias = int(input('Por quantos dias o carro foi alugado?'))
quilometros_rodados = float(input('Quantos Km rodados?'))
valor_a_pagar = (dias * 60) + (quilometros_rodados * 0.15)
print('O total a pagar é de R${:.2f}'.format(valor_a_pagar))
