import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pickle
from selenium.webdriver.chrome.options import Options

options = Options()
Options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://bt.rozetka.com.ua/ua/pyramida-4260674993626/p429500831')
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button--green')]"))).click()
pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies_site", "wb"))
time.sleep(3)
driver.delete_all_cookies()
driver.refresh()
time.sleep(3)
cookies = pickle.load(open(os.getcwd()+"/cookies_site", 'rb'))
time.sleep(3)
driver.refresh()
time.sleep(3)