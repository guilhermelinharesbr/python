"""
ANSI - escape sequence

 O código ANSI começa com um contra barra ' \ ' e
depois vem o código.
 Existe uma faixa dos códigos ANSI para cores, mas 
um que trabalha bem com o Python é 033, por exemplo:
     style ; text ; background 
\033[                          m
          
 Acima é possível ver que a estrtura começa com o \033
e além disso tem o style, text, background e fechando com
a letra m. Abaixo será mostrado um exemplo completo:
\033[0;33;44m   
 No exemplo acima é visto que o '0' é referente ao style,
o 33 é referente ao text e o 44 é referente ao background.

 Os códigos que funcionam melhor no Terminal para o Python:
style -> 0, 1, 4, 7.
         0 -> none
         1 -> bold
         4 -> underline
         7 -> negative   #Inverte as cores, o que for background 
                         #vira texto e o que texto vira background. 
text -> 30, 31, 32, 33, 34, 35, 36, 37
        30 -> white
        31 -> red
        32 -> green
        33 -> yellow
        34 -> blue
        35 -> purple
        36 -> light blue
        37 -> gray
background -> 40, 41, 42, 43, 44, 45, 46, 47
              40 -> white
              41 -> red
              42 -> green
              43 -> yellow
              44 -> blue
              45 -> purple
              46 -> light blue
              47 -> gray

"""

#Para o texto sem formatação, de cor branca e back vermelho:
#Resp.: \033[0;30;41m

#Para o texto com underline, de cor amarela e back azul claro:
#Resp.: \033[4;34;46m

#Para o texto em negrito, de cor roxa e back amarelo:
#Resp.: \033[1;35;43m

#Para o sem formatação, de cor branca e back verde:
#Resp.: \033[30:42m
#Obs: Foi omitido de propósito o número referente ao style,
      #apenas para mostrar que pode-se omitir ele, pois é o padrão.

#Para o texto sem formatação, de cor cinza e back preto:
#Resp.: \033[m  ou \033[0m
#Obs: Esse é padrão do Terminal.

#Para o texto sem formatação, de cor preta e back branco:
#Resp.: \033[7;30m  
#Obs: Usa o código 7 para inverter a cor do texto, e 30 para
# dizer que o fundo é branco. 

#Obs: O módulo colorsys trabalha com conversão entre sistemas de cores.

#Observação final: a prática desse estudo está no arquivo cores-no-terminal.ipynb.
