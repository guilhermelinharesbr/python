"""
Descreva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 24.9: Peso ideal
- 25 até 29.9: Sobrepeso
- 30 até 34.9: Obesidade Grau I
- 35 até 39.9: Obesidade Grau II
- Acima de 40: Obesidade mórbida
"""

#Primeira forma
peso = float(input('Digite o seu peso em (Kg): '))
altura = float(input('Digite sua altura em (m): '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('O seu IMC é de {:.1f}\nVocê está ABAIXO DO PESO normal'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('O seu IMC é de {:.1f}\nVocê está com o PESO IDEAL.'.format(imc))
elif imc >= 25 and imc < 30:
    print('O seu IMC é de {:.1f}\nVocê está com SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 35:
    print('O seu IMC é de {:.1f}\nVocê está com OBESIDADE GRAU I.'.format(imc))
elif imc >= 35 and imc < 40:
    print('O seu IMC é de {:.1f}\nVocê está com OBESIDADE GRAU II.'.format(imc))
elif imc >= 40:
    print('O seu IMC é de {:.1f}\nVocê está com OBESIDADE MÓRBIDA.'.format(imc))
print('-=-' * 15)

#Segunda forma
peso = float(input('Qual o seu peso em (Kg): '))
altura = float(input('Qual sua altura em (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('Você está com o PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 35:
    print('Você está com OBESIDADE GRAU I.')
elif 35 <= imc < 40:
    print('Você está com OBESIDADE GRAU II.')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA.')
