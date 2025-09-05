import requests




def test_api_test():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = (response.json())
    assert response.status_code == 200
    assert len(data) == 10
    for user in data:
        email = user['email']
        assert '@' in email


