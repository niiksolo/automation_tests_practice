from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.get('https://demoqa.com/dynamic-properties')
Visible_after_button = (By.XPATH, "//button[@id='enableAfter']")
wait.until(EC.visibility_of_element_located(Visible_after_button)).click()

# enable_after_5sec = (By.XPATH, "//button[@id='enableAfter']")          #есть такой еще вариант
# wait.until(EC.element_to_be_clickable(enable_after_5sec)).click()

# wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON)) исчезла кнопка