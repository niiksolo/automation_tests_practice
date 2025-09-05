import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
driver = webdriver.Chrome(options=options)

FOR_BUSINESS_LOCATOR = ('xpath', "//a[text()='Click Here']")
START_FREE_LOCATOR = ('xpath', "//input[@type='submit']")

#print(driver.current_window_handle) # дискриптор нашего окна уникальный индификатор окна в котором мы работаем
driver.get('https://demo.guru99.com/popup.php')
time.sleep(3)  #вручную создаюновое окно во время теста
#print(driver.window_handles)   # это список всех идентификаторов всех открытых вкладок
#driver.find_element(*FOR_BUSINESS_LOCATOR).click()
#time.sleep(3)
#tabs = driver.window_handles
#driver.switch_to.window(tabs[1]) # переключаеся на открывшуюся вкладку и там нажимаем клик
#driver.find_element(*START_FREE_LOCATOR).click()

##windows = driver.window_handles
##driver.switch_to.window(windows[1])
##driver.get('https://rozetka.com.ua')
##time.sleep(3)

driver.switch_to.new_window('tab')  # автоматически переключит на открывшуюся вкладку
time.sleep(3)

