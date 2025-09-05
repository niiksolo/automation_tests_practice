import requests
import pytest
import time

def test_body_is_ok():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    print(response.json())
    assert response.status_code == 200
    assert data['id'] == 1
    assert 'userId' in data
    assert 'body' in data
    assert 'title' in data


