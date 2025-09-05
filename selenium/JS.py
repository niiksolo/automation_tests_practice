import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get('https://seiyria.com/bootstrap-slider')
#driver.execute_script("alert('HELLO')")  # пример js

EX_2 = ('xpath', "//h3[text()='Example 2: '] ")  # тут нет JS а просто как доскролить до нужного элимента
EX = driver.find_element(*EX_2)

action.scroll_to_element(EX).perform()
time.sleep(3)