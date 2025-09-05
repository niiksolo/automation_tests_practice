from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



LOCATOR_YES = (By.XPATH, "//label[@for='yesRadio']")
RESULT_LOCATOR = (By.XPATH, "//span[@class='text-success']")
LOCATOR_IMPRESS = (By.XPATH, "//label[@for='impressiveRadio']")


@pytest.mark.parametrize('button_locator, expect_result',
    [
        (LOCATOR_YES, 'Yes'),
        (LOCATOR_IMPRESS, "Impressive")
    ]

     )
def test_radio_button(driver, button_locator, expect_result):
    wait = WebDriverWait(driver,10,1)
    driver.get('https://demoqa.com/radio-button')
    wait.until(EC.element_to_be_clickable(button_locator)).click()
    result = wait.until(EC.visibility_of_element_located(RESULT_LOCATOR)).text
    assert result == expect_result




