import os
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://the-internet.herokuapp.com/upload')
time.sleep(3)
file_input = (driver.find_element('xpath', "//input[@type='file']").send_keys(f'{os.getcwd()}/downloads/8b52cfa6-72ee-4133-ac9c-545c28fa87be.tmp'))
time.sleep(3)
