#Exemplos de uso da função print():

numero1=int(input('Digite o primeiro número:'))
numero2=int(input('Digite o segundo número:'))
soma=numero1+numero2
#Mostrando um exemplo com a máscara {} e o Método .format(soma)
print('A soma é igual a: {}'.format(soma))
#print(type('A variável soma é do tipo: ',(soma))
#print(type('A variável soma é do tipo: ',(numero1))
print(type(numero1))
print(type(soma))
#Primeira forma de fazer:
print('A soma entre',numero1,'e',numero2,'é',soma)
#Segunda forma de fazer:
print('A soma entre {} e {} é {}'.format(numero1,numero2,soma))
