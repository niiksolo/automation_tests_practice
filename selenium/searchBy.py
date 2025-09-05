from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()
browser.get("https://www.qa-practice.com/elements/button/simple")
click_button4 = browser.find_element(By.XPATH,'//input[@class="btn btn-primary"]')
click_button4.click()
# поиск по XPATH

# поиск по css selector
# click_button3 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
# click_button3.click()
# sleep(3)

# поиск по link text
#link = browser.find_element(By.LINK_TEXT, "Contact")
#browser.execute_script("arguments[0].click();", link) -  #не сработал click, говоришь: «Найди ссылку с надписью "Contact", и  JavaScript нажми на неё
#sleep(3)

# поиск по class name
#click_button = browser.find_element(By.CLASS_NAME, "btn-primary")
#click_button.click()
#sleep(4)


# поиск по ID
# click_button2 = browser.find_element(By.ID, "submit-id-submit")
# click_button2.click()
#sleep(4)

