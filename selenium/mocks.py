import requests
import requests_mock
import time

from request.GET import response


with requests_mock.Mocker() as mock:                     #GET запрос
    mock.get(
        url='https://api.example.com/users/123',
        json={
            'id':123,
            'name': 'Nikita'
        },
        status_code=101,
        headers={"NIK": "MOCK"}
    )

    response = requests.get('https://api.example.com/users/123')
    print(response.json())
    print(response.status_code)
    print(response.headers)

with requests_mock.Mocker() as mock:                #POST запрос
     mock.post(
         url='https://api.example.com/users/',
         json={
             'id':123,
             'name': 'Spider Man'
         },
         status_code=201
     )
     response = requests.post(
         url='https://api.example.com/users/',
         json={'name': 'Spider Man'}
     )
     print(response.json())


with requests_mock.Mocker() as mock:                     #типо с задержкой сервер отвечает
    mock.get(url='https://api.example.com/delayed', json={'key': 'value'})
    start_time = time.time()
    time.sleep(2.5)
    response = requests.get('https://api.example.com/delayed')
    end_time = time.time()

    print(end_time - start_time)
    print(response.json())






