import pytest
import requests


@pytest.mark.parametrize('number', [1,2,3,4,5])
def test_id(number):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{number}')
    data = response.json()
    assert data ['id'] == number

