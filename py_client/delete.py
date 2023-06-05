import requests

endpoint = "http://localhost:8000/api/products/1/"
endpoint = "http://localhost:8000/api/products//delete"

# get_response = requests.get(endpoint, json={"producy_id":123})
get_response = requests.delete(endpoint)
# print(get_response.text)
print(get_response.status_code,get_response.status_code==204)