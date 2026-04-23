#Escreva um programa que leia um valor em metros e o exiba
#convertido em centímetros e milímetros.

#Primeira forma, usando várias variáveis
valor=float(input('Digite um valor em metros:'))
centimetros=valor*100
milimetros=valor*1000
print('O valor em metros é:{}m, o valor em centímetros é:{}cm, o valor em milímetros é:{}mm'.format(valor,centimetros,milimetros))

#Segunda forma, usando apenas uma variável, e com os cm e mm sem casas decimais
valor=float(input('Digite um valor em metros:'))
print('O valor em metros é:{}m, o valor em centímetros é:{:.0f}cm, o valor em milímetros é:{:.0f}mm'.format(valor,(valor*100),(valor*1000)))
