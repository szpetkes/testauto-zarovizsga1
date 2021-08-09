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

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")
time.sleep(1)

try:
    # elements
    cities = driver.find_element_by_id('cites')
    missing = driver.find_element_by_id('missingCity')
    checking = driver.find_element_by_id('submit')
    result_message = driver.find_element_by_id('result')

    #cities in the world
    cities_in_the_world = []
    world_cities = driver.find_elements_by_id('cites')
    for city in world_cities:
        cities_in_the_world.append(city.text)
    print(cities_in_the_world)

    #random cities list
    random_cities = []
    random_city = driver.find_elements_by_xpath('//ul/li')
    for city in random_city:
        random_cities.append(city.text)
    print(random_cities)

    #compare two list
    def compare(cities_in_the_world, random_cities):
        for i in range(len(cities_in_the_world)):
            if cities_in_the_world[i] not in random_cities:
                print("missing", cities_in_the_world[i])
        for j in range(len(random_cities)):
            if random_cities[j] not in cities_in_the_world:
                print("added", random_cities[j])

    #send missing city to validate
    def data_input(missing_city):
        missing.clear()
        missing.send_keys(city)
        checking.click()
        time.sleep(1)

    assert result_message == missing.text

finally:
    driver.close()
