import json
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.espn.com.br/futebol/time/elenco/_/id/6273/gremio"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)

# COLETANDO INFO DOS JOGADORES
driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[2]/div[5]/div/div/section/div/section/div[4]/div[1]/div[2]/div/div[2]/table')
elementG = driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[2]/div[5]/div/div/section/div/section/div[4]/div[1]/div[2]/div/div[2]/table')
html_contentG = elementG.get_attribute('outerHTML')

driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[2]/div[5]/div/div/section/div/section/div[4]/div[2]/div[2]/div/div[2]/table')
elementL = driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[2]/div[5]/div/div/section/div/section/div[4]/div[2]/div[2]/div/div[2]/table')
html_contentL = elementL.get_attribute('outerHTML')

# HTML JOGADORES
soupG = BeautifulSoup(html_contentG, 'html.parser')
tableG = soupG.find(name='table')

soupL = BeautifulSoup(html_contentL, 'html.parser')
tableL = soupL.find(name='table')

# TABELAS INFORMAÇÃO DOS JOGADORES
dfG_full = pd.read_html(str(tableG))[0]
dfG = dfG_full[['Nome', 'POS', 'Idade', 'Alt', 'P', 'NAC']]
dfG.columns = ['Nome', 'Posição', 'Idade', 'Altura', 'Peso', 'Nacionalidade']

dfL_full = pd.read_html(str(tableL))[0]
dfL = dfL_full[['Nome', 'POS', 'Idade', 'Alt', 'P', 'NAC']]
dfL.columns = ['Nome', 'Posicao', 'Idade', 'Altura', 'Peso', 'Nacionalidade']

#VARIÁVEIS DICIONÁRIO
info_jogadoresGol = {}
info_jogadoresGol['info'] = dfG.to_dict('records')

info_jogadoresLinha = {}
info_jogadoresLinha['info'] = dfL.to_dict('records')

info_jogadores = {}
info_jogadores['Jogadores'] = dfG.to_dict('records') + dfL.to_dict('records')

driver.quit()

# CRIAÇÃO DO JSON
js = json.dumps(info_jogadores)
fp = open('infoJogadores.json', 'w', encoding='UTF-8')
fp.write(js)
fp.close()
