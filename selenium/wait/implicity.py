from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(1)   # глобально для всего файла использ
driver.get('https://demoqa.com/dynamic-properties')
Visible_after_button = ('xpath', "//button[@id='enableAfter']")
driver.find_element(*Visible_after_button).click()  #      * - распаковщик