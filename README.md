# Dados Públicos CNPJ 
Utilitário em Python para fazer download completo base de CNPJ [disponibilizada pela Brasil.io](https://brasil.io/dataset/documentos-brasil/documents/) (aprox. 2,5GB) 


## Configurações prévias
Para executar o script, é necessário que seu sistema contenha essas instalações:

## Python
Versão mais atual

` $ sudo apt upgrade python3`

## Gerenciador de Pacotes do Python (Pip)
A versão mais atual. Se estiver usando Python3:

`$ python3 -m pip install --upgrade pip`

## Instalar Pré-Requisitos:

`$ pip install -r requirements.txt`

Esse comando instalará as seguintes bibliotecas:

#### Pandas
A versão mais atual da biblioteca [Pandas](https://pandas.pydata.org) para Python. 

#### Selenium
A versão mais atual da biblioteca [Selenium](https://selenium-python.readthedocs.io/#)
Obs: Nesse script foi usado o (Webdriver.Chrome), caso não seja o seu navegador e obte por outro,
no proprio site da biblioteca citado acima tem links para download de Webdrives compatives com
os navegadores mais usuais.

#### Time
A versão mais recente da biblioteca.

## Antes de executar
Atente para o fato de que o arquivo de dados disponibilizado é grande. São aprox. (2.5 GB) de arquivo texto descomprimido.

## Como executar 
 Verificado que o arquivo "desafio.py" encontra-se no diretório:

`$ python3 desafio.py`

Ao final do da execução do script, é informado no terminal a seguinte mensagem:
"Aguarde o download! Caso queira encerrar o programa, pressione qualquer tecla: "
aguarde o termino do download para encerrar o script.
