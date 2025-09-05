
import requests


def test_end_to_end():
    POST = requests.post('https://reqres.in/api/users',
                         headers={
                             'x-api-key': 'reqres-free-v1'
                         },
                         json={
                             'name': 'Nikita',
                             'job': 'QC'
                         }
                         )

    post_json = POST.json()
    id = post_json['id']
    assert POST.status_code == 201

    PATCH = requests.patch(f'https://reqres.in/api/users/{id}',
                           headers={
                               'x-api-key': 'reqres-free-v1'
                           },
                           json={
                               'job': 'QA-junior'
                           }
                          )
    data = PATCH.json()
    assert data['job'] == 'QA-junior'
    delete_user = requests.delete(f'https://reqres.in/api/users/{id}',
                                  headers={
                                      'x-api-key': 'reqres-free-v1'
                                  }
                                  )
    assert delete_user.status_code == 204


