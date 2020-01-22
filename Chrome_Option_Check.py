#options = webdriver.ChromeOptions()
#options.binary_location = '/usr/bin/chromium-browser'
#All the arguments added for chromium to work on selenium
#options.add_argument("--no-sandbox") #This make Chromium reachable
#options.add_argument("--no-default-browser-check") #Overrides default choices
#options.add_argument("--no-first-run")
#options.add_argument("--disable-default-apps")
#driver = webdriver.Chrome('/home/travis/virtualenv/python2.7.9/chromedriver',chrome_options=options)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path_Chrome=r"chromedriver.exe"
browser = webdriver.Chrome(path_Chrome)

browser.get("http://www.123formbuilder.com/form-3291802/formula-rio-de-registro-de-novo-cliente")

browser.find_element_by_xpath(".//*[contains(text(), 'Não')]").click()

browser.find_element_by_xpath(".//*[contains(text(), 'Nós gentilmente te pedimos')]").click()
