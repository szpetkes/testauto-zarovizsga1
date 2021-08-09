"""""""""
4 Feladat: Email mező

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Email mező app-ot az https://black-moss-0a0440e03.azurestaticapps.net/mm43.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Email mező app tesztelését.

A cél az email validáció tesztelése:

    TC01: Helyes kitöltés esete:
        email: teszt@elek.hu
        Nincs validációs hibazüzenet

    TC02: Helytelen:
        email: teszt@
        Please enter a part following '@'. 'teszt@' is incomplete.

    TC03: Üres:
        email: <üres>
        b: <üres>
        Please fill out this field.

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

driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")
time.sleep(1)

try:
    # elements
    email_field = driver.find_element_by_id('email')
    submit = driver.find_element_by_id('submit')

    # testdata
    email1 = 'teszt@elek.hu'
    email2 = 'teszt@'
    email3 = ''


# datainput


    def data_input(email):
        email_field.clear()
        email_field.send_keys(email)
        submit.click()
        time.sleep(2)


# TC01:
    data_input(email1)
    error_text = driver.find_elements_by_class_name('validation-error')
    assert len(error_text) == 0

# TC02:
    data_input(email2)
    error_text = driver.find_element_by_class_name('validation-error')
    assert error_text.text == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'

# TC03:
    data_input(email3)
    error_text = driver.find_element_by_class_name('validation-error')
    assert error_text.text == 'Kérjük, töltse ki ezt a mezőt.'

finally:
    driver.close()
