import requests

endpoint = "http://localhost:8000/api/products/1/"

# get_response = requests.get(endpoint, json={"producy_id":123})
get_response = requests.get(endpoint)
# print(get_response.text)
print(get_response.json())