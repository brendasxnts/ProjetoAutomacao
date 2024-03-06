import pyautogui

pyautogui.PAUSE = 1.5
pyautogui.press ("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("link que eu quero")
pyautogui.press("enter")

import time
time.sleep(3) #programa vai esperar 3 seg para carregar a pagina 
#fazer login
#criar novo arquivo "auxiliar.py"
#importar o pyautogui

pyautogui.click("x=, y=")
pyautogui.write("email")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click("x=, y=")
#ou pyautogui.press("tab")
time.sleep(4) #para carregar a pagina caso demore

#importar base de dados para preencher os formularios de um site 

import pandas
tabela = pandas.read_csv("produtos.csv") #(poderia ser read_xml ou read_html ou read_excel  ou pandas_sql)
print(tabela) #para ver 


#cadastrar 1 produto
#para cada linha

for linha in tabela.index:
 pyautogui.click("posição x e y")
 #para pegar o codigo
 codigo = tabela.loc[linha, "codigo"]
 pyautogui.write("codigo")
 pyautogui.press("tab")

marca = tabela.loc[linha, "marca"]
pyautogui.write(tabela.loc[linha, "marca"])
pyautogui.press("tab")

pyautogui.write(tabela.loc[linha, "tipo"])
pyautogui.press("tab")

str()
pyautogui.write(str(tabela.loc[linha, "categoria"]))
pyautogui.press("tab")

pyautogui.write(str(tabela.loc[linha, "preço_unitario"]))
pyautogui.press("tab")

pyautogui.write(str(tabela.loc[linha, "custo"]))
pyautogui.press("tab")

obs = tabela.loc[linha, "obs"]
if not pandas.isna(obs): #se n tiver vazia NAN(NOT A NUMBER) preenche
 pyautogui.write(tabela.loc[linha, "obs"])
pyautogui.press("tab")

#para enviar
pyautogui.press("enter")
pyautogui.scroll(5000) 
#scroll positivo para cima e negativo para baixo)
