import json
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

option = Options()
option.headless = True
driver = webdriver.Firefox()

url = "https://www.espn.com.br/futebol/time/elenco/_/id/6273/gremio"

driver.get(url)



# INFO
#
#
# Coletando as informações do site
elements = driver.find_elements_by_tag_name("table")
elementG = elements[0]
elementL = elements[1]

html_contentG = elementG.get_attribute('outerHTML')
html_contentL = elementL.get_attribute('outerHTML')




# HTML
# 
#
# Configurando o HTML a partir do BeautifulSoup
soupG = BeautifulSoup(html_contentG, 'html.parser')
tableG = soupG.find(name='table')
soupL = BeautifulSoup(html_contentL, 'html.parser')
tableL = soupL.find(name='table')




# TABELAS
#
#
# Criando tabela a partir do Pandas
df_fullG = pd.read_html(str(tableG))[0]
dfG = df_fullG[['Nome', 'POS', 'Idade', 'Alt', 'P', 'NAC']]
dfG.columns = ['Nome', 'Posição', 'Idade', 'Altura', 'Peso', 'Nacionalidade']
df_fullL = pd.read_html(str(tableL))[0]
dfL = df_fullL[['Nome', 'POS', 'Idade', 'Alt', 'P', 'NAC']]
dfL.columns = ['Nome', 'Posição', 'Idade', 'Altura', 'Peso', 'Nacionalidade']



# DICIONÁRIO
#
#
# Criando váriaveis para dicionário
info_goleiros = {}
info_goleiros['info'] = dfG.to_dict('records')
info_linha = {}
info_linha['info'] = dfL.to_dict('records')
info_jogadores = {}
info_jogadores['Jogadores'] = dfG.to_dict('records') + dfL.to_dict('records')



# Fechando o driver
driver.quit()




# JSON
#
#
# Criando o arquivo .json
js = json.dumps(info_jogadores)
fp = open('infoJogadores.json', 'w', encoding='UTF-8')
fp.write(js)
fp.close()
