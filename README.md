# WebScraping Grêmio
![120px-Gremio-Logo](https://user-images.githubusercontent.com/72706376/141303317-ca9fd191-3afd-411b-ac8e-25813c1f3841.png)

## SOBRE O PROJETO
O projeto tem como função utilizar o BeautifulSoup e o Selenium para buscar informações, 
no site da ESPN Brasil, sobre os jogadores da atual temporada do Grêmio.


## NECESSÁRIO PARA UTILIZAR
>>> Python 3

>>> requests

>>> selenium

>>> geckodriver

>>> Beautiful Soup

>>> pandas

>>> json


## FUNCIONAMENTO DO PROJETO
O programa busca, com  o webdriver, no site da ESPN Brasil o elenco inteiro do 
time do Grêmio e, coleta as informações de nome, idade, altura, posição e nacionalidade 
sobre os todos os jogadores. Após pegar essas informações o código usa o Pandas 
para criar uma tabela e um dicionário com as informações e, a partir disso cria um arquivo 
.json com todas as informações de cada jogador.
