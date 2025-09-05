from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def test_iframe_screen(driver):
    wait = WebDriverWait(driver,10,1)
    driver.get('https://demoqa.com/frames')
    IFRAME = wait.until(EC.presence_of_element_located((By.ID, "frame1")))
    driver.switch_to.frame(IFRAME)
    sample_page = driver.find_element(By.ID, 'sampleHeading')
    assert sample_page.text == 'This is a sample page'
    driver.switch_to.default_content()