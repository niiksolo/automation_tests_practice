from importlib.metadata import files
from wsgiref.headers import Headers

import requests
from requests.auth import HTTPBasicAuth

#response = requests.post(
#    url='https://petstore.swagger.io/v2/pet',
#    headers={
#        'api_key': 'special-key'
#    },
#    json={
#     "id": 555555,
#      "category": {
#        "id": 0,
#        "name": "string"
#      },
#      "name": "NIKA",
#      "photoUrls": [
#        "string"
#      ],
#      "tags": [
#        {
#          "id": 0,
#         "name": "dogs"
#        }
#      ],
#     "status": "available"
#    }
#)
#print(response.json())

##get_pet_by_id = requests.get(
##    url='https://petstore.swagger.io/v2/pet/555555',
##    headers={
##        'api_key': 'special-key'
##    }
##)
##print(get_pet_by_id.json())

# грузим картинку для животного своего
response = requests.post(
    url='https://petstore.swagger.io/v2/pet/555555/uploadImage',
    headers={
        'api_key': 'special-key'

    },
    files={
    'file': ('cat.jpg', open('cat.jpg', 'rb'), 'image/jpeg')
    }
)
print(response.status_code)
print(response.json())