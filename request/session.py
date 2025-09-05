import requests

session = requests.Session()


response = session.get('https://httpbin.org/cookies/set?freeform=123')
print(response.json())

response = session.get('https://httpbin.org/cookies')
print(response.json())

#соединение с сервером установилось и теперь куки и в во второй раз сохранились.
# при работе с сессиями в рамках единого соединения
