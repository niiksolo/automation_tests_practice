import pytest
import requests
from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User
from tests.conftest import get_number

def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    #print(make_number)

@pytest.mark.production
@pytest.mark.skip('issue-2300')   # скипать тесты можна так
def test_another():
    '''
    IN that test we try to check that 1 is equal to 2
    '''
    assert 1 == 1

def test_calculate(calculate):
    print(calculate(1, 2))

@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result',[
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value,second_value, result, calculate):
    '''
    in test we are testing calculating with different values(valid and invalid)
    '''
    assert calculate(first_value, second_value)== result

@pytest.mark.fail
def test_another_failed():
    assert 1 == 2
