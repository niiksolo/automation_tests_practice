import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#KEYBORD = ('xpath', "//input[@id='target']")
#driver.get('https://the-internet.herokuapp.com/key_presses?')
#time.sleep(2)
#driver.find_element(*KEYBORD).send_keys('dsfgsdfgdfgds')     # ввел текст
#river.find_element(*KEYBORD).send_keys(Keys.CONTROL + 'A')  # выделяем текст
#driver.find_element(*KEYBORD).send_keys(Keys.BACKSPACE)      # удаляем текст
#time.sleep(2)

#SELECT = ('xpath', "//input[@id='react-select-3-input']")
driver.get('https://demoqa.com/select-menu')
#time.sleep(2)
#driver.find_element(*SELECT).send_keys('Ms.')       # находим из списка Ms
#driver.find_element(*SELECT).send_keys(Keys.ENTER)  # нажимаем ENTER и выбиреем ее
#time.sleep(3)


# как решить можно проблему когда скрытые элименты в дереве и они проподают
# в Devtools в Console пишем  setTimeout(function() { debugger; }, 5000); - через 5 сек останавливает на сайте все
#SELECT1 = ('xpath', "//div[@id='selectOne']")
#Prof = ('xpath', "//div[text()='Prof.']")

#driver.find_element(*SELECT1).click()
#time.sleep(2)
#driver.find_element(*Prof).click()
#time.sleep(2)


# работа с мультиселектом (можно вібрать сразу несколько вариантов)
MULTISELECT_LOCATOR = ('xpath', "//input[@id='react-select-4-input']")
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Green')
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Black')
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)