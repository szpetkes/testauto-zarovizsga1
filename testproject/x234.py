"""""""""
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a téglalap kerülete app-ot az https://black-moss-0a0440e03.azurestaticapps.net/x234.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete appban:

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy assert 
összehasonlításokat használj! 

    
    TC01: Helyes kitöltés esete:
        a: 99
        b: 12
        Eredmény: 222

    TC02: Nem számokkal történő kitöltés:
        a: kiskutya
        b: 12
        Eredmény: NaN

    TC03: Üres kitöltés:
        a: <üres>
        b: <üres>

"""""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")
time.sleep(1)

try:
    # elements
    a_num = driver.find_element_by_id('a')
    b_num = driver.find_element_by_id('b')
    calc = driver.find_element_by_id('submit')


# datainput


    def calculation(a, b):
        a_num.clear()
        b_num.clear()
        a_num.send_keys(a)
        b_num.send_keys(b)
        calc.click()
        time.sleep(1)


# TC01
    calculation('10', '5')
    perimeter = driver.find_element_by_id('result')

    assert perimeter.text == '30'

# TC02
    calculation('number', 'also')
    perimeter = driver.find_element_by_id('result')

    assert perimeter.text == 'NaN'

# TC03
    calculation('', '')
    perimeter = driver.find_element_by_id('result')

    assert perimeter.text == 'NaN'

finally:
    driver.close()
