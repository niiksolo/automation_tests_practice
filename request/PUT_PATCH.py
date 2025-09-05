import requests


#response = requests.put(   # если отправлять не все тело ресурса то остальные поля в put обнуляются опасная ситуация
#    url='https://jsonplaceholder.typicode.com/posts/1',
#    json={
#        'title': 'QWERTY'
#    }

#)
#print(response.json())

response = requests.patch(          #все поля на месте кроме то что мы меняем
    url='https://jsonplaceholder.typicode.com/posts/2',
    json={
        'title': 'HELLO'
    }

)
print(response.json())