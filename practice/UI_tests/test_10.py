from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def test_drag_and_drop(driver):
    wait = WebDriverWait(driver,10,1)
    driver.get('https://demoqa.com/droppable')

    element = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@id='droppableExample-tab-revertable']")))
    driver.execute_script('arguments[0].scrollIntoView(true);', element)
    element.click()

    NOT_REVERT = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='notRevertable']")))
    driver.execute_script('arguments[0].scrollIntoView(true);', NOT_REVERT)

    DROP_HERE = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='droppable'])[3]")))
    driver.execute_script('arguments[0].scrollIntoView(true);', DROP_HERE)

    ActionChains(driver).drag_and_drop(NOT_REVERT, DROP_HERE).perform()
    assert DROP_HERE.text == 'Dropped!'
    driver.save_screenshot('test_10.py.png')

