import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://demoqa.com/alerts')
Button_1 = (By.XPATH, "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(Button_1)).click()
time.sleep(2)
alert = wait.until(EC.alert_is_present()) # ждем пока алер появится
driver.switch_to.alert  # переключаемся на него
print(alert.text)  # текст что в алерте был передает
alert.accept() # примимаем его или можно отменить  alert.desmiss()
   # если в алерте нужно чтото написать alert.send_keys('Hello')