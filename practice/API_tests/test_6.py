import requests


def test_put_id():
    resp = requests.put('https://jsonplaceholder.typicode.com/posts/1',
                        json = {
                            'id': 888 ,
                            'title': 'put_change',
                            'userId': 123 ,
                            'body': '90_kg schastya'
                        }
                        )
    data = (resp.json())
    print(data)
    assert resp.status_code == 200
    assert 'userId' in data and data['userId'] == 123
    assert 'title' in data and data['title'] == 'put_change'
    assert 'body' in data and data['body'] == '90_kg schastya'