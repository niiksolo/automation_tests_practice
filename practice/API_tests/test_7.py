import requests

def test_end_to_end():
    get =  requests.get('https://reqres.in/api/users/2')
    data = get.json()
    patch = requests.patch('https://reqres.in/api/users/2',
            headers={
                        'x-api-key': 'reqres-free-v1'
    },
    json = {
                        'first_name': 'Nik',
                        'last_name': 'Solo'
                         }
    )
    data_patch = patch.json()
    assert data_patch['first_name'] == 'Nik'
    assert data_patch['last_name'] =='Solo'
    print(data_patch)




