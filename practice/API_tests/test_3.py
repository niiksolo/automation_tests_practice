import pytest
import requests


@pytest.mark.parametrize('num', [6, 7, 8, 9, 10])
def test_title(num):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{num}')
    data = (response.json())
    assert response.status_code == 200
    assert data['title'] != ''

