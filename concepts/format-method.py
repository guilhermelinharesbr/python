#O método format() formata o(s) valor(es) especificado(s) 
#e os insere no espaço reservado da string.
#O espaço reservado é definido usando chaves: {}.
#O método format() retorna a string formatada.

numero1=int(input('Digite o primeiro número:'))
numero2=int(input('Digite o segundo número:'))
soma=numero1+numero2
print('A soma entre {} e {} é {}'.format(numero1,numero2,soma))
