import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





checkbox_1 = ('xpath', "(//input[@type='checkbox'])[1]")
checkbox_2 = ('xpath', "(//input[@type='checkbox'])[2]")

def test_checkboxes(driver):
    driver.get('https://the-internet.herokuapp.com/checkboxes')

    check_1 = (driver.find_element(*checkbox_1))
    check_1.click()
    is_checked  = check_1.is_selected()
    assert is_checked is True

    check_2 = driver.find_element(*checkbox_2).is_selected()
    assert check_2 == True


