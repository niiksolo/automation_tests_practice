import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

select_locator = ('xpath', "//select[@id='dropdown']")

driver.get('https://the-internet.herokuapp.com/dropdown')

DROPDOWN = Select(driver.find_element(*select_locator))

# DROPDOWN.select_by_visible_text('Option 1') - можно выбрать по тексту как здесь нужную опцию в dropdown
# DROPDOWN.select_by_value('2')   # или выбрать по value
# DROPDOWN.select_by_index(1) # или по индексу

ALL_OPTIONS = DROPDOWN.options # Список веб элементов опшенов наших
# print(ALL_OPTIONS)

for option in ALL_OPTIONS:
    time.sleep(3)
    if 'Option 1' in option.text:   # проверка есть ли в списке опций
        print('Эта опция есть в списке')
    DROPDOWN.select_by_visible_text(option.text)     # перебор всех опций