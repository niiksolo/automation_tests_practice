from selenium import  webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()


def test_main_banner_visible(driver):
    driver.get('https://magento.softwaretestingboard.com')
    banner = driver.find_element(By.ID, "maincontent")
    assert banner.is_displayed()

def test_add_to_cart(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://magento.softwaretestingboard.com/proteus-fitness-jackshirt.html')
    driver.execute_script("""    
        document.querySelectorAll('iframe').forEach(el => el.remove());
    """)      # удаляем рекламу

    wait.until(EC.element_to_be_clickable((By.ID, 'option-label-size-143-item-166'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'option-label-color-93-item-49'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'product-addtocart-button'))).click()
    success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'message-success')))
    assert "You added" in success_message.text