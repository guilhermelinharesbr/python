#Faça um programa que leia um número inteiro
#e mostre na tela o seu sucessor e seu antecessor.
numero = int(input('Digite um número:'))
sucessor=numero+1
antecessor=numero-1
print('O número digitado foi {}, o seu sucessor é {}, o seu antecessor é {}.'.format(numero,sucessor,antecessor))