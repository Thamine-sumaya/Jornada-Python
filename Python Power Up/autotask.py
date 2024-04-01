import pyautogui 
#time é uma biblioteca nativa do python, não é necessário importar
import time
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("navegador opera GX")
pyautogui.press('enter')
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
time.sleep(3)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click (x=973, y=486)
pyautogui.write('emailgenérico@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press("enter")
time.sleep(3)
import pandas
tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
	pyautogui.click(x=853, y=338)
	#código do produto
	codigo = tabela.loc[linha, "codigo"]
	pyautogui.write(codigo)      
	pyautogui.press('tab')
	#marca 
	marca = tabela.loc[linha, "marca"]
	pyautogui.write(marca)
	pyautogui.press('tab')
	#tipo
	tipo = tabela.loc[linha, "tipo"]
	pyautogui.write(tipo)
	pyautogui.press('tab')
	#categoria
	categoria = str(tabela.loc[linha, "categoria"])
	pyautogui.write(categoria)
	pyautogui.press('tab')
	#preço
	preço = str(tabela.loc[linha, "preco_unitario"])
	pyautogui.write(preço)
	pyautogui.press('tab')
	#custo
	custo = str(tabela.loc[linha, "custo"])
	pyautogui.write(custo)
	pyautogui.press('tab')
	#obs
	obs = tabela.loc[linha, "obs"]
	if not pandas.isna(obs):
		pyautogui.write(obs)
	pyautogui.press('tab')
	#enviar 
	pyautogui.press("enter")
	pyautogui.scroll(5000)