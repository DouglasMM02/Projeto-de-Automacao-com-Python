# Projeto de Automacao com Python

Projeto feito em Python usando as bibliotecas Pyautogui e Pandas.
O objetivo do projeto é automatizar o cadastro e produtos em um site de vendas, usando uma base de dados com os produtos já organizado.
Código serve para qualquer automação do mesmo gênero.
Na linha 28 (pyautogui.click(x=653, y=294)) vale ressaltar que caso não funcione no seu PC, basta executar o seguinte código em outro arquivo:
import pyautogui
import time

time.sleep(5)
# Obter a posição atual do mouse, de run no código e troque rapidamente para a tela de login
x, y = pyautogui.position()
print(f"Posição do mouse: ({x}, {y})")

Também é necessário estar na exata tela na qual travou o sistema e com o ponteiro encima do campo inicial.

 
