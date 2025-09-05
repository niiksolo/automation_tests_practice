import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



LOCATOR_BUTTON = (By.XPATH, "//button[@id='promtButton']")
LOCATOR_RESULT = (By.XPATH, "//span[@id='promptResult']")

@pytest.mark.parametrize('NAME',['Nik', 'Bysya', 'Katya'])
def test_alert(driver, NAME):
    wait = WebDriverWait(driver,10,1)
    driver.get('https://demoqa.com/alerts')
    button = wait.until(EC.element_to_be_clickable(LOCATOR_BUTTON))
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()   # пришлось добавить изза iframe
    alert = driver.switch_to.alert
    alert.send_keys(NAME)
    alert.accept()
    result = wait.until(EC.visibility_of_element_located(LOCATOR_RESULT))
    assert result.text == f'You entered {NAME}'

