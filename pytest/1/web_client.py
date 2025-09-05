# import json
# import requests
# from datetime import datetime
#
# class SomeResourceClient:
#     def __init__(self, url):
#         self.url  = url
#
#     def user_get_status(self, user_id):
#         resp = requests.get(f'{self.url}/findByStatus')
#         json_data = json.loads(resp.text)
#         return json_data
#     def get_user_last_action_time(self, user_id):
#         json_data = self.user_get_status(user_id)
#         last_action_time = json_data['lastActionTime']
#         time_diff = json_data['timeDiff']
#         return datetime.fromtimestamp(last_action_time - time_diff)
#
#
# some_resource_client = SomeResourceClient('https://petstore.swagger.io/v2/pet/findByStatus?status=available')
# print(some_resource_client.user_get_status('findByStatus?status=available'))
# print(some_resource_client.get_user_last_action_time('findByStatus?status=available'))
        # json_data = json.loads(resp.content)
        # return  json_data



# response = requests.get('https://www.olx.ua/d/uk/obyavlenie/zdatsya-1k-kvartira-v-zhk-obolon-rezidens-obolonskiy-prs-26-IDYCmnG.html')
# print(response.text)

# import json
# import requests
# from datetime import datetime
#
# class SomeResourceClient:
#     def __init__(self, url):
#         self.url  = url
#
#     def user_get_status(self, user_id):  # user_id не нужен, но оставляем структуру
#         resp = requests.get(self.url)
#         json_data = json.loads(resp.text)
#         return json_data
#
#     def get_user_last_action_time(self, user_id):
#         json_data = self.user_get_status(user_id)
#         # Берем время обновления курса
#         updated_iso = json_data['time']['updatedISO']
#         return datetime.fromisoformat(updated_iso)
#
# some_resource_client = SomeResourceClient('https://api.coindesk.com/v1/bpi/currentprice.json')
#
# print("📦 JSON-ответ от API:")
# print(some_resource_client.user_get_status(1))
#
# print("\n🕒 Время последнего обновления курса BTC:")
# print(some_resource_client.get_user_last_action_time(1))

import pytest

@pytest.mark.parametrize(
    'a, b, res',
    [
        (3, 3, 6),
        (2, 2, 4)
    ]
)
def test_sum(a, b, res):
    assert(a + b) == res


