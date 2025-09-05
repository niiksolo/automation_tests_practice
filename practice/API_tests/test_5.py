import requests


def test_POST():
    POST = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json={
        'title':'Мой ПОСТ тест',
        'body':'90_kg schastya',
        'userId': 777
}
)
    data = (POST.json())
    assert POST.status_code == 201
    assert 'id' in data and data['id'] is not None #Сначала проверяем, что ключ есть (чтобы не было ошибки) Потом, что значение ключа — не пустое (None)
    assert data['title'] == 'Мой ПОСТ тест'
    assert data['userId'] == 777
    assert data['body'] == '90_kg schastya'
