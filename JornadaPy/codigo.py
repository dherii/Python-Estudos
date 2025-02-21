import pyautogui
import time

pyautogui.PAUSE= 1


pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=496, y=369)
pyautogui.write("Dheriiteste@hashtag.com")
pyautogui.press("tab")
pyautogui.write("teste321")

pyautogui.click(x=663, y=536)
time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    #codigo
    codigo = tabela.loc[linha,"codigo"]    
    pyautogui.click(x=417, y=254)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #1
    pyautogui.press("tab")
    #PU
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    #enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(2000)
