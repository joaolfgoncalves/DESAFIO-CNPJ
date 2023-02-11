import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC




def get_cnpj():

     # Abrindo e configurando o navegador onde a biblioteca selenium vai executar os comandos
    self = 'https://brasil.io/dataset/documentos-brasil/documents/'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    navegador = webdriver.Chrome(executable_path="chromedriver",options=options)
    navegador.set_window_size(1080,1080)
  

    navegador.get(f'{self}')

   
   #Etapa de navegação pela estrutura do site para encontrar os dados 
    time.sleep(20)
    elemento =  navegador.find_element(By.XPATH,'/html/body/nav/div/ul/li[2]/a').click()
    time.sleep(20)
    elemento =  navegador.find_element(By.XPATH,'//*[@id="desktop-data-dropdown"]/li[1]/a').click()
    time.sleep(20)
    elemento =  navegador.find_element(By.XPATH,'/html/body/main/div/div[2]/div[10]/div/div[1]/p').click()
    time.sleep(20)
    elemento = navegador.find_element(By.XPATH,'/html/body/main/div/div[2]/div[10]/div/div[2]/div/a[1]').click()
    time.sleep(20)
    elemento =  navegador.find_element(By.XPATH,'//*[@id="data"]/div[2]/div[1]/a').click()
    time.sleep(20)

    #Mudança de abas no navegador
    navegador.switch_to.window(navegador.window_handles[1])
    time.sleep(20)
    elemento =  navegador.find_element(By.XPATH,'/html/body/main/div/div/div/div[2]/table/tbody/tr[2]/td[1]/a').click()
    time.sleep(20)
    i = input("Aguarde o download! Caso queira encerrar o programa, pressione qualquer tecla: ")
    return self



var = get_cnpj()

