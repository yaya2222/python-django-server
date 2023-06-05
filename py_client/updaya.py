import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data={"title":"yaya","price":1111.23}
# get_response = requests.get(endpoint, json={"producy_id":123})
get_response = requests.put(endpoint,json=data)
# print(get_response.text)
print(get_response.json())