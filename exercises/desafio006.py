#Crie um algoritmo que leia um número e mostre o seu
#dobro, triplo e raiz quadrada.

#Primeira forma, usando várias variáveis
numero = int(input('Digite um número:'))
dobro = numero*2
triplo = numero*3
raizquadrada = numero ** (1/2)
print('O número digitado foi {}, o seu dobro é {}, o seu triplo é {} e sua raiz quadrada é {}'.format(numero,dobro,triplo,raizquadrada))

##########

#Segunda forma, usando apenas uma variável
numero = int(input('Digite um número:'))
print('O número digitado foi {}\n O seu dobro é {}\n O seu triplo é {}\n A raiz quadrada é {:.2f}'.format(numero,(numero*2),(numero*3),(numero ** (1/2))))

#Terceira forma, usando a pow function
numero = int(input('Digite um número:'))
print('O número digitado foi {}\n O seu dobro é {}\n O seu triplo é {}\n A raiz quadrada é {:.2f}'.format(numero,(numero*2),(numero*3),(pow(numero,1/2))))
