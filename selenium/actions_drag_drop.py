import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
action = ActionChains(driver)

#driver.get('https://the-internet.herokuapp.com/drag_and_drop')

#COLLUMN_A = ('xpath', "//div[@id='column-a']")
#COLLUMN_B = ('xpath', "//div[@id='column-b']")

# 1 способ
#A = driver.find_element(*COLLUMN_A)
#B = driver.find_element(*COLLUMN_B)
#time.sleep(2)
#action.drag_and_drop(A, B).perform()
#time.sleep(2)

#2способ    # если драг энд дроп исчезающий нужно остановить страницу и проинспектировать этот исчезающий драгэнддроп
            # setTimeout(function() { debugger; }, 5000);
driver.get('https://tympanus.net/Development/DragDropInteractions/sidebar.html')
GRID_ITEM = ('xpath', "//div[@class='grid__item'][3]")
SIDE_BAR = ('xpath', "//div[@class='drop-area__item'][3]")

GRID = driver.find_element(*GRID_ITEM)
DROP_AREA = driver.find_element(*SIDE_BAR)

action.click_and_hold(GRID).pause(2).move_to_element(DROP_AREA).release().perform()
