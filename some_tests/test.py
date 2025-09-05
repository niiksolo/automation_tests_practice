import pytest
import allure


@pytest.fixture()
def separator():
    print('1' * 3)  # функция говорит что 1 умножить на 3
    yield 'value'   # постусловия после теста
    print('test finished')

@pytest.fixture(scope='session')  # отрабатывает для все сессии
def all_tests():
    print('before all')  # будет писать до тестов
    yield
    print('after all')   # будет писать после

@pytest.mark.regrassion   # можно помечать и запускать по отдельности командой  pytest test.py -v -s -m regrassion
@allure.feature(3 == 3)
@allure.story('check_3')
def test_1(separator, all_tests):
    print('number1')
    print(separator)
    assert 3 == 3

@pytest.mark.smoke
@allure.feature( 10==10 )
@allure.story('check_10')
 # @pytest.mark.skip('bug42')  # можно скипать баг
def test_2(separator):
    print('number2')
    print(separator)
    assert 10 == 10

