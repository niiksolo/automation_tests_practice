import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

LEFT_CLICK_LOCATOR = ('xpath', "//button[@id='leftClick']")
DOUBLE_CLICK_LOCATOR = ('xpath', "//button[@id='doubleClick']")
RIGHT_CLICK_LOCATOR = ('xpath', "//button[@id='rightClick']")
HOVER_BUTTON_LOCATOR = ('xpath',"//button[@id='colorChangeOnHover']")

#driver.get('https://testkru.com/Elements/Buttons')

#LEFT_BUTTON = driver.find_element(*LEFT_CLICK_LOCATOR)      #просто клик левой кнопкой
#action.click(LEFT_BUTTON).perform()

#double_button = driver.find_element(*DOUBLE_CLICK_LOCATOR)
#action.double_click(double_button).perform()                # даблклик по кнопке

#right_button = driver.find_element(*RIGHT_CLICK_LOCATOR)    # правой кнопкой мыши клик
#action.context_click(right_button).perform()

#hover_button = driver.find_element(*HOVER_BUTTON_LOCATOR)

#action.move_to_element(hover_button)                   # наведение на элимент
#time.sleep(2)

# action.click(LEFT_BUTTON).pause(2).double_click(double_button).pause(2).context_click(right_button).perform()  #цепочка действий pause -делаем паузы капитан


# навидение на несколько элиментов подряд
driver.get('https://demoqa.com/menu')
main_item = driver.find_element('xpath', "//a[text()='Main Item 2']")
sub_list = driver.find_element('xpath', "//a[text()='SUB SUB LIST »']")
time.sleep(2)
action.move_to_element(main_item)\
    .pause(2)\
    .move_to_element(sub_list)\
    .pause(2)\
    .perform()
time.sleep(3)

