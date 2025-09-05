import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PROXY = '8.211.42.167' #А ЕСЛИ НУЖНА АВТОРИЗАЦИЯ НА ПРОКСИ СЕРВЕРЕ ТО ДЕЛАЕМ ТАК 'username:password@8.211.42.167'

options = Options()
options.add_argument(f"--proxy-server={PROXY}")

driver = webdriver.Chrome(options=options)
driver.get('https://2ip.ua/ru') #188.163.14.189

time.sleep(3)