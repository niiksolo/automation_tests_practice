import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
#driver = webdriver.Chrome(options=options)


#driver.get("https://demo.guru99.com/test/login.html")
#time.sleep(2)
#email_field = driver.find_element(By.NAME, "email")
#email_field.send_keys("test@example.com")

#password_field = driver.find_element(By.NAME, "passwd")
#password_field.send_keys("123456")

#sign_in_button = driver.find_element(By.ID, "SubmitLogin")
#sign_in_button.click()
#time.sleep(2)

#driver.switch_to.new_window('window')   # открываем новое окно и внем тоже будем залогинеными если ввели коректные даные по логину и паролю
#driver.get("https://demo.guru99.com/test/login.html")
#time.sleep(2)



#если хочу поработать с двумя вкладками но не под одним логином и паролем шо делаем :
user1 = webdriver.Chrome(options=options)

user1.get("https://demo.guru99.com/test/login.html")
time.sleep(2)
email_field = user1.find_element(By.NAME, "email")
email_field.send_keys("test@example.com")

password_field = user1.find_element(By.NAME, "passwd")
password_field.send_keys("123456")

sign_in_button = user1.find_element(By.ID, "SubmitLogin")
sign_in_button.click()
time.sleep(2)

user2 = webdriver.Chrome(options=options)
user2.get("https://demo.guru99.com/test/login.html")
time.sleep(3)