import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options)

NAME_LOCATOR = ('xpath', "//input[@id='email']")
PRACTICE_LOCATOR = ('xpath', "//a[@class='navbar-brand p-0 me-2 logo_title']")

driver.get('https://practice.expandtesting.com/iframe')

driver.switch_to.frame('email-subscribe')  #не находил элимент из-за iframe пишем это и в скобочках id его или другой индификатор какойто
driver.find_element(*NAME_LOCATOR).send_keys('NIKITA')
time.sleep(3)
driver.switch_to.default_content()  # возврат назад из iframe на дефолтный контент
driver.find_element(*PRACTICE_LOCATOR).click()
time.sleep(3)

#что делаем когда iframe внутри iframe
#driver.get('https://demoqa.com/frames')
#driver.switch_to.frame('frame1')
#print(driver.find_element('xpath','//body').text)

#driver.switch_to.frame(0) # у меня плохой пример но схема такая
#print(driver.find_element('xpath','//body').text)

#driver.switch_to.parent_frame() #это чтобы с iframe вернуться в первый iframe
#print(driver.find_element('xpath','//body').text)