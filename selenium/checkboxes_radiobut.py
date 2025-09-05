import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# 1 метод получения статуса чекбокса проверяем атрибут checked
#driver.get('https://the-internet.herokuapp.com/checkboxes')
#checkboxes_1 = ('xpath', "(//input[@type='checkbox'][1])")
#print(driver.find_element(*checkboxes_1).get_attribute('checked')) # когда ставим галочку в доме появляется атрибут checked щас смотрим есть ли он ( ответ NONE)
#driver.find_element(*checkboxes_1).click()
#print(driver.find_element(*checkboxes_1).get_attribute('checked')) # щас появился cheked бо мы нажали чекбокс и появится запись TRUE

# 2 метод is.selected
#print(driver.find_element(*checkboxes_1).is_selected())     #  приходит FALSE
#driver.find_element(*checkboxes_1).click()
#print(driver.find_element(*checkboxes_1).is_selected())     #  приходит  TRUE

# как обойти когда не можешь кликнуть на чекбокс
#checkbox_home_status = ('xpath', "//input[@id='tree-node-home']")   # этот элимент чемто перекрыт (у него появляется невидимый статус checked)
#checkbox_home_action = ('xpath', "//span[@class='rct-checkbox']")   # этот видимый через него мы нажимаем на чекбокс а статус смотрим в checkbox_home_status
#driver.get('https://demoqa.com/checkbox')
#print(driver.find_element(*checkbox_home_status).is_selected())   # Приходит False
#driver.find_element(*checkbox_home_action).click()
#print(driver.find_element(*checkbox_home_status).is_selected())   # True


#ELEMENT_ONE = ('xpath', '//li[text()="Cras justo odio"]')
#driver.get('https://demoqa.com/selectable')
#before = driver.find_element(*ELEMENT_ONE).get_attribute('class')
#click = (wait.until(EC.element_to_be_clickable(ELEMENT_ONE)))
#driver.execute_script("arguments[0].scrollIntoView(true);", click)
#click.click()
#after = driver.find_element(*ELEMENT_ONE).get_attribute('class')
#assert 'active' in after  #assert - подтверди
# проанализировал что при нажитии чекбокса появляется active в атрибуте и проверил что он появляется чтобі знать что мі на чекбокс точно нажали


# радиокнопка все также как и с чекбокссами часто встречается вариант когда один элимент для статуса один для взаимодествия как в чекбоксах
driver.get('https://demoqa.com/radio-button')
YES = ('xpath', "//label[@class='custom-control-label']")
NOT = ('xpath', "//label[@class='custom-control-label disabled']")
driver.find_element(*YES).click()
print(driver.find_element(*YES).is_enabled()) # используется для проверки, доступен ли элемент для взаимодействия