"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto

- À vista no cartão: 5% de desconto

- Em até 2x no cartão: preço normal

- 3x ou mais no cartão: 20 % de juros
"""

#Primeira forma
print('-=-' * 5, 'Loja Linhares', '-=-' * 5)
compras = float(input('Seu total em compras foi R$'))
print('[1] À vista dinheiro/cheque\n [2] À vista no cartão\n [3] 2x no cartão\n [4] 3x ou mais no cartão\n')
opcoes = int(input('Qual a opção? ')) 
if opcoes == 1:
    desconto = compras - ((compras * 10) / 100)
    print('Sua compra de R${:.2f} sairá por R${:.2f}'.format(compras,(desconto)))
elif opcoes == 2:
    desconto = compras - ((compras * 5) / 100)
    parcela = desconto / 2
    print('Sua compra de R${:.2f} sairá por R${:.2f} com duas parcelas de R${:.2f}'.format(compras,desconto, parcela))
elif opcoes == 3:
    print('Sua compra de R${:.2f} foi validada.'.format(compras))
elif opcoes == 4:
    valor_com_juros = compras + ((compras * 20) / 100)
    parcela = int(input('Digite o total de parcelas: '))
    valor_parcelado = valor_com_juros / parcela
    print('Sua compra de R${:.2f} sairá por R${:.2f} com {} parcelas de R${:.2f}'.format(compras,valor_com_juros,parcela,valor_parcelado))  
else:
    print('Opção inválida.')


#Segunda forma
print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1 :
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc,parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
