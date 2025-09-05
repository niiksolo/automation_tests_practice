from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10,1)

def test_search():
    driver.get('https://www.youtube.com')
    search_field = wait.until(EC.element_to_be_clickable(('xpath', "//input[@class='ytSearchboxComponentInput yt-searchbox-input title']")))
    search_field.send_keys('футбол')
    #driver.find_element('xpath', "//button[@title='Введите запрос']").click()
    search_field.send_keys(Keys.ENTER)
    driver.quit()

