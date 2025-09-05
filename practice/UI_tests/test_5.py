
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


dropdown_locator = ('xpath', "//select[@id='dropdown']")

def test_dropdown(driver):
    driver.get('https://the-internet.herokuapp.com/dropdown')

    DROPDOWN = driver.find_element(*dropdown_locator)
    select = Select(DROPDOWN) # нужно обернуть его в селект

    select.select_by_visible_text('Option 1')
    assert select.first_selected_option.text != 'Option 2'

    select.select_by_value('2')
    assert select.first_selected_option.text == 'Option 2'
    print(len(select.options)) # сколько всего опций находиться в dropdown



