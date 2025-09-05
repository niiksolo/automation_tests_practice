import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


LARGE_BUTTON = (By.XPATH, "//button[@class='mt-2 btn btn-primary']")
SMALL_BUTTON = (By.XPATH, "//button[@class='mr-4 mt-2 btn btn-primary']")
CHECK_LARGE_TEXT = (By.XPATH, "//div[text()='Large Modal']")
CHECK_SMALL_TEXT = (By.XPATH, "//div[text()='Small Modal']")
CLOSE_LARGE_BUTTON = (By.XPATH,"//button[@id='closeLargeModal']")
CLOSE_SMALL_BUTTON = (By.XPATH,"//button[@id='closeSmallModal']")

@pytest.mark.parametrize('different_modal,check_text,close_button, result',
                         [
                            (LARGE_BUTTON , CHECK_LARGE_TEXT,CLOSE_LARGE_BUTTON, 'Large Modal'),
                            (SMALL_BUTTON , CHECK_SMALL_TEXT,CLOSE_SMALL_BUTTON, 'Small Modal')
                         ]
                         )


def test_modal(browser,different_modal,check_text,close_button,result):
    wait = WebDriverWait(browser,10,1)
    browser.get('https://demoqa.com/modal-dialogs')
    wait.until(EC.element_to_be_clickable(different_modal)).click()
    TEXT = wait.until(EC.visibility_of_element_located(check_text))
    assert TEXT.text == result
    wait.until(EC.element_to_be_clickable(close_button)).click()
