import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_open_youtube(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.youtube.com')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div/yt-icon-button[@id='guide-button']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Shorts']"))).click()
