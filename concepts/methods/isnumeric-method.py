#O método isnumeric() retorna True se todos os caracteres 
#forem numéricos (0-9), caso contrário, retorna False.
#Expoentes, como ² e ¾, também são considerados valores numéricos.
#-1 e 1.5 NÃO são considerados valores numéricos, porque todos os 
#caracteres na string devem ser numéricos, e o hífen (-) e o ponto (.) não são.
n = input('Digite algo: ')
print(n.isnumeric())
