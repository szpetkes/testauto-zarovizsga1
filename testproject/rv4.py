""""""""""
5 Feladat: Kakukktojás - városok

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Kakukktojás - városok app-ot az https://black-moss-0a0440e03.azurestaticapps.net/rv4.html 
oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel a Kakukktojás - városok app tesztelését.

Az applikáció minden frissítésnél véletlenszerűen változik!

Feladatod, hogy megtaláld a hiányzó városnevet, kitöltsd a form-ban a mezőt és ellnörizd le, hogy eltaláltad-e.

A feladatnak több helyes megoldása is van (találgatós/ismétlős, pythonban kalkulálós), mindegy, hogy hogyan oldod 
meg, csak találd meg az egy véletlen hiányzó város nevét 

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy assert 
összehasonlításokat használj! "" """

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")
time.sleep(1)

try:
    # elements
    cities = driver.find_elements_by_id('cites')
    random_cities = driver.find_elements_by_id('randomCities')
    lost_city = driver.find_element_by_id('missingCity')
    checking = driver.find_element_by_id('submit')
    result_message = driver.find_element_by_id('result')


    # datainput

    def data_input(city):
        lost_city.clear()
        lost_city.send_keys(city)
        checking.click()
        time.sleep(1)


# TC01:

finally:
    driver.close()
