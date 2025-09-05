import requests
from requests.auth import HTTPBasicAuth


#простой GET запрос
response = requests.get(
    url='https://petstore.swagger.io/v2/pet/findByStatus',           # Endpoint(конечная точка)
    # auth=HTTPBasicAuth(username: 'NIK', password:'sdfsdf')     #аутентификация через логин и пароль
    headers={
        'api_key':'spicial-key'   #токены
    },
    params={
        'status':'sold'
    }           #qwery фильтрации выбор
    #verify=True/False
)
print(response.json())
#print(response.status_code)
#print(response.json()["pending"])

