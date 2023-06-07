import requests

endpoint = "http://localhost:8000/api/products/"

token = "b10810b619e3cf7f3adac955cf8bed961854a794"

headers={
        "Authorization": f"Bearer {token}"
}

data = {
    "title":"this field is done2",
    "price":100.00
}

# get_response = requests.get(endpoint, json={"producy_id":123})
get_response = requests.post(endpoint,json=data , headers=headers)
# print(get_response.text)
print(get_response.json())