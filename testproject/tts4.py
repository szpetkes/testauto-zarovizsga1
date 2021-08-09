"""""""""
2 Feladat: Pénzfeldobás

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a pénzfeldobás app-ot az https://black-moss-0a0440e03.azurestaticapps.net/tts4.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a pénzfeldobás app tesztelését.

Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej. Ezt kell ellenőrizned.

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy assert 
összehasonlításokat használj! 

"""""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")
time.sleep(1)

try:

    # elements
    button = driver.find_element_by_id("submit")
    result = driver.find_element_by_id("lastResult")

    # heads count
    heads_number = 0
    for i in range(1, 101):
        button.click()
        if result.text == "fej":
            heads_number += 1

    # TC01:
    assert heads_number >= 30
    print('fej találatok:', heads_number, ',OK!')

finally:
    driver.close()
