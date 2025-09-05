import pytest
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


LOCATOR_USERNAME = (By.XPATH, "//input[@id='userName']")
LOCATOR_PASSWORD = (By.XPATH, "//input[@id='password']")
LOCATOR_BUTTON_LOGIN = (By.XPATH, "//button[@id='login']")
LOCATOR_INVALID_DATA = (By.XPATH, "//p[@id='name']")

@pytest.fixture
def open_close_browser():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()



@pytest.mark.parametrize('login , password',
                         [
                             (12321, '@#@@$#@@'),
                             ('#$@#$$@#' , 'a'),
                             ('іваівааі', 'аыаваыв'),
                             ('FSFSFSD', 'SDFSDFSD')
                         ]
                         )

def test_login_page(open_close_browser,login,password):
    wait = WebDriverWait(open_close_browser,10,1)
    open_close_browser.get('https://demoqa.com/login')

    user = wait.until(EC.element_to_be_clickable(LOCATOR_USERNAME))
    open_close_browser.execute_script('arguments[0].scrollIntoView();', user)
    user.send_keys(login)

    passw = wait.until(EC.element_to_be_clickable(LOCATOR_PASSWORD))
    open_close_browser.execute_script('arguments[0].scrollIntoView();', passw)
    passw.send_keys(password)

    button = wait.until(EC.element_to_be_clickable(LOCATOR_BUTTON_LOGIN))
    open_close_browser.execute_script('arguments[0].scrollIntoView();', button)
    button.click()

    INVALID_DATA = wait.until(EC.visibility_of_element_located(LOCATOR_INVALID_DATA))
    assert INVALID_DATA.text == 'Invalid username or password!'



