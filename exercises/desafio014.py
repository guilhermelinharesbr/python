#Escreva um programa que converta uma temperatura digitada
#em ºC e converta para ºF.

#Primeira forma
celsius = float(input('Informe a temperatura em ºC:'))
fahrenheit = float(((celsius * 9) / 5) + 32)
print('A temperatura de {}ºC corresponde a {}ºF!'.format(celsius,fahrenheit))

#Segunda forma
celsius=float(input('Informe a temperatura em ºC:'))
fahrenheit = celsius * 9 / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(celsius,fahrenheit))
