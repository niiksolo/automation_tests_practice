from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://sneakers-kross.com.ua/ru/muzhskaya-obuv')
login_button = driver.find_element(By.XPATH, "//span[@class='userbar__button-text']").click()
email_field = driver.find_element(By.XPATH, "//input[@type='email' and @tabindex='1']")
email_field.send_keys('login@gmail.com') # заполнили поле
# print(email_field.get_attribute('value'))
time.sleep(3)
email_field.clear()   # очистили поле
email_field.send_keys('sdfsdfsdfsd')  # ввели новый текст

