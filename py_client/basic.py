import requests

endpoint = "http://localhost:8000/api/?abc2=1232"

# get_response = requests.get(endpoint, json={"producy_id":123})
get_response = requests.post(endpoint, json={"title2":"hi","a":123})
# print(get_response.text)
print(get_response.json())