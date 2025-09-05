import pytest
import requests

@pytest.mark.parametrize('id',[0, 1.5, 9999, -1, 'abc'])
def test_not_valid_id(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
    data = (response.json())
    print(response.json())
    assert response.status_code == 404
    assert data == {}
