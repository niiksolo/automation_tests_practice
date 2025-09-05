import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--window-size=700,700')
options.add_argument('--disable-blink-features=AutomationControlled') # обманывает браузер что не вебдрайвер заходит на сайт а человек
options.add_argument('--user-agent=Selenium')      # подставлять вместо Селениум какойто юзерагент с интернета чтобы боаузе не думал что мы робот и везде пропускал
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://chatgpt.com')
driver.save_screenshot('screen.png')  # сделать скриншот
