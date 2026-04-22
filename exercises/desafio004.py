#Faça um programa que leia algo pelo teclado
#e mostre na tela o seu tipo primitivo e todas as 
#informações possíveis sobre ele.
valor = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(valor))
print('É um espaco?',valor.isspace())
print('É um número?',valor.isnumeric())
print('É alfabético?',valor.isalpha())
print('É alfanumérico?',valor.isalnum())
print('É maiúsculo?',valor.isupper())
print('É minúsculo?',valor.islower())
print('É capitalizada?',valor.istitle())
