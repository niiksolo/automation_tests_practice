from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


users = ['user1@gmail.com', 'user2@gmail.com', 'user3@gmail.com']
passwords = ['dfdfdf', 'sdfsdfsdfs', 'fdfdsfsdgk']    # создаем парное тестирование для  того чтобы протести разные логины с разными паролями

def generate_pairs():  # продолжение попарного тестир
    pairs = []
    for user in users:
        for pwd in passwords:
            pairs.append(pytest.param((user, pwd), id=f'{user}, {pwd}'))
    return pairs



#@pytest.mark.parametrize(
#    'creds',
#   [
#        pytest.param(('user1@gmail.com','ddsdfsd'), id='user1@gmail.com, ddsdfsd'),
#        pytest.param(('user2@gmail.com','aaaaaaaa'), id='user2@gmail.com, aaaaaaaa'),
#        pytest.param(('user3@gmail.com','cccccccc'), id='user3@gmail.com, cccccccc')
        # мы подписали их таким ид для наглядности можно было просто id=user1 и все
        # если подписівать не нужно можно оставить так:
        # ('user3@gmail.com','cccccccc') - без пайтестпарам и ид
#    ]
#)
# @pytest.mark.skip - скип тестов
@pytest.mark.parametrize('creds', generate_pairs())
def test_login(creds):
    login, passw = creds
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    driver.find_element(By.NAME, 'login[username]').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(passw)
    driver.find_element(By.CSS_SELECTOR, '.action.login.primary').click()
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    assert 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.' == error_text


@pytest.fixture()
def page(request): # request - нужен для поискв в одном def несколько вариантов поиска
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    param = request.param    # продолжение
    if param == 'wats_new':
        driver.get('https://magento.softwaretestingboard.com/what-is-new.html')
    elif param == 'sale':
        driver.get('https://magento.softwaretestingboard.com/sale.html')
    return driver
@pytest.mark.parametrize('page', ['wats_new'], indirect=True)
def test_whats_new(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'What\'s New'

@pytest.mark.parametrize('page', ['sale'], indirect=True)
def test_sale(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'Sale'
