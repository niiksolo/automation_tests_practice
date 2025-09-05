import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pickle

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://www.freeconferencecall.com/ru/ua/login')

# print (driver.get_cookie('country_code')) - конкретную куку получить

# print(driver.get_cookies())   #- все куки получить

#driver.add_cookie({    #добавить куки
  #  'name': 'Example',
 #   'value': 'BGG'
#})print(driver.get_cookie('Example'))

#before = driver.get_cookie('split')  #получаю куку
#print(before)
#driver.delete_cookie('split')  # удаляю
#driver.add_cookie({               # добовляю
#    'name': 'split',
#    'value': 'QWERTY'
#})
#after = driver.get_cookie('split')  # получаю свою новую для проверки
#print(after)

# сохраняю куки в файл
#email_input = wait.until(EC.presence_of_element_located((By.ID, "login_email")))
#email_input.send_keys("your_email@example.com")
#password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
#password_input.send_keys("your_password")
#login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginform-submit")))
#login_button.click()
#pickle.dump(driver.get_cookies(), open(os.getcwd()+"/various/cookies/cookies.pkl", 'wb'))


#подгрузка куков из файла ( авторизация через куки )
#driver.delete_all_cookies()
#cookies = pickle.load(open(os.getcwd()+"/various/cookies/cookies.pkl", 'rb'))
#for cookies in cookies:
#    driver.add_cookie(cookies)
#driver.refresh()
#cookies = pickle.load(open(os.getcwd()+"/various/cookies/cookies.pkl", 'rb'))