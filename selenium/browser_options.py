from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager' #   'normal' загружает страницу а 'eager' ждет только загрузки DOM
# chrome_options.add_argument('--headless')      # безголовый режим
# chrome_options.add_argument('--incognito')       # инкогнито режим
# chrome_options.add_argument('--ignore-certificate-errors')  # избегает ошибок с сертификатом
chrome_options.add_argument('--window-size=700,700')   # фиксирует размер окна
# chrome_options.add_argument('--disable-cache')  # кеш не будет записываться
driver = webdriver.Chrome(options=chrome_options)

# driver.maximize_window() окно экрана на весь экран
driver.get('https://chatgpt.com')
