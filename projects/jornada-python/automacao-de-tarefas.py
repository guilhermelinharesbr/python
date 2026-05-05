# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time
from pathlib import Path

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.8

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
# Feito no monitor Positivo
#pyautogui.click(x=717, y=414)

# Feito no monitor Notebook Samsung
pyautogui.click(x=607, y=553)

# escrever o seu emailpythonimpressionador@gmail.com    
pyautogui.write("youremail@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("DtR48732##!@!213")
# Feito no monitor Positivo
#pyautogui.click(x=939, y=568) # clique no botao de login
# Feito no monitor Notebook Samsung
pyautogui.click(x=978, y=757) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
# pip install pandas
import pandas as pd

# Se os produtos.csv não estiverem no mesmo diretório do arquivo
# automacao-de-tarefas.py teria que passar o caminho completo.
pasta_script = Path(__file__).parent
tabela = pd.read_csv(pasta_script / "produtos-2unidades.csv") 

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    # Feito no monitor Positivo
    #pyautogui.click(x=679, y=292)
    # Feito no monitor Notebook Samsung
    pyautogui.click(x=659, y=414)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

    # nan == not a number
