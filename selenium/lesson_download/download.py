import os


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()

prefs = {                                                          #указываем нашу папку куда скачать иначе будет сохранять в базовую директорию
    'download.default_directory': f'{os.getcwd()}/downloads'       #
}
chrome_options.add_experimental_option('prefs', prefs)       #

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://the-internet.herokuapp.com/download')
driver.find_element(By.XPATH, "//a[2]").click()





