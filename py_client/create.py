import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"this field is done2",
    "price":100.00
}

# get_response = requests.get(endpoint, json={"producy_id":123})
get_response = requests.post(endpoint,json=data)
# print(get_response.text)
print(get_response.json())