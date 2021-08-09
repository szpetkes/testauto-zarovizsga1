"""""""""""""""

3 Feladat: Összeadó

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a összeadó app-ot az https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a összeadó app tesztelését.

Az applikáció minden frissítésnél véletlenszerűen változik!

A feladatod, hogy a random számokkal működő matematikai applikációt ellenőrizd. A teszted ki kell, hogy olvassa a két 
operationt (számot) és az operátort (műveleti jelet). Ennek megfelelően kell elvégezned a kalkulációt Pythonban. 

A kalkuláció gombra kattintva mutatja meg az applikáció, hogy mi a művelet eredménye szerinte.

Hasonlítsd össze az applikáció által kínált megoldást és a Python által kalkulált eredményt. Ennek a kettőnek 
egyeznie kell. 

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

driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")
time.sleep(1)

try:
    # elements
    num1 = driver.find_element_by_id("num1")
    num2 = driver.find_element_by_id("num2")
    operation = driver.find_element_by_id("op")

    print(num1.text)
    print(operation.text)
    print(num2.text)

    # calculation by site
    calculation_button = driver.find_element_by_id("submit")
    calculation_button.click()

    result = driver.find_element_by_id("result")
    print('Eredmény az oldalon:', result.text)

    # calculation by me
    if operation.text == '+':
        my_calculation = int(num1.text) + int(num2.text)
    elif operation.text == '-':
        my_calculation = int(num1.text) - int(num2.text)
    else:
        my_calculation = int(num1.text) * int(num2.text)

    print('Számolt eredmény:', my_calculation)

    assert result.text == str(my_calculation)

finally:
    driver.close()
