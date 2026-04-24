#Tipos Primitivos
#int   -> integer -> Ex: 7, -4, 0, 9578
#float -> float   -> Ex: 7.0, 4.5, 0.076, -15.223
#bool  -> boolean -> Ex: True, False. Obs: Sempre que for usar True e False, colocar a primeira letra maiúscula.
#str   -> string  -> Ex: 'Olá', '7.5', '' Obs: o último exemplo é de uma string vazia. 
#Métodos de String -> .format(), .isnumeric()


### Testando a tipagem das variáveis:
#No caso do tipo int, se digitar uma letra ele dará um erro no código.
a = int(input('Digite um valor para A: '))
print(a)
#No caso do tipo float, se digitar uma letra ele dará um erro no código.
b = float(input('Digite um valor para B: '))
print(b)
#No caso do tipo bool, se digitar algo ele retornará True,
#se não digitar nada retornará False. 
c = bool(input('Digite um valor para C: '))
print(c)
d = str(input('Digite um valor para D: '))
print(d)
