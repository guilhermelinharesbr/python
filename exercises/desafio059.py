"""
Crie um programa que leia dois valores e mostre 
um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada
em cada caso.
"""

#Primeira forma
opcao = 0

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

while opcao != 5:
    print(f""" --------
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    opcao = int(input(f'Qual é a sua opção? '))
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma de {valor1} e {valor2} é \033[32m{soma}\033[0m.')
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print(f'A multiplicação de {valor1} e {valor2} é \033[32m{multiplicacao}\033[0m.')
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print(f'Entre {valor1} e {valor2} o maior valor é \033[32m{maior}\033[0m.')
        elif valor1 < valor2:
            maior = valor2
            print(f'Entre {valor1} e {valor2} o maior valor é \033[32m{maior}\033[0m.')
        else:
            print(f'Entre {valor1} e {valor2} não existe maior valor, pois ambos são iguais.')
    elif opcao == 4:
        print(f'Informe os novos números: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print(f'\033[32mFinalizando...\033[0m')
    else:
        print('Opção inválida. Tente novamente.')
print(f'Fim do Programa.')


            





#Segunda forma
