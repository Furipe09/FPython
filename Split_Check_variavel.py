#Ideia para quebrar sring em partes e utilizar o texto de cada quebra em alguma funçao, exemplo, pesquisar Checkbox com pesquisa de texto no Browser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

#Cria variave e separa por ","
palavra = "Não,Nós"
teste = palavra.split(",")

#path para navegar
path_Chrome=r"chromedriver.exe"
browser = webdriver.Chrome(path_Chrome)
#URL de teste
browser.get("http://www.123formbuilder.com/form-3291802/formula-rio-de-registro-de-novo-cliente")

#Função para percorrer a variavel

def percorreLista(tamanhoLista):
    for item in range(tamanhoLista):
        print(item, "-", teste[item])
        variavel = teste[item]
        print(variavel)
        #browser.find_element_by_xpath(".//*[contains(text(), variavel)]").click()
        browser.find_element_by_xpath(".//*[contains(text(), '" + variavel + "')]").click()

if re.search(',', palavra, re.IGNORECASE):
    print("Sim")
    tamanhoLista = len(teste)
    percorreLista(tamanhoLista)
else:
    print("não ", palavra)
    '" + VAR_TEXT + "'
    browser.find_element_by_xpath(".//*[contains(text(), '" + palavra + "')]").click()



