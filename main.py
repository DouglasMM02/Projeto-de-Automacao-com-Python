import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3

# abrir o navegador e acessar o link
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

# fazer login 
pyautogui.press('tab')
pyautogui.write('DevPython@gmail.com')
pyautogui.press('tab')
pyautogui.write('12345678')
pyautogui.press('enter')

# base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=653, y=294) # caso a posição do clicl não funcione, terá de mudar os eixos X e Y
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
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
    pyautogui.press("enter")
    # dar scroll de tudo pra cima e recomeçar de novo
    pyautogui.scroll(5000)