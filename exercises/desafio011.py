#Faça um programa que leia a largura e a altura de uma
#parede em metros, calcule a sua área e a quantidade de 
#tinta necessária para pintá-la, sabendo que cada litro 
#de tinta, pinta uma área de 2m².

#Primeira forma
largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(area/2))

#Segunda forma
largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
área = largura * altura
tinta = área / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura,altura,área))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tinta))
