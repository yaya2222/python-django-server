import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"

userName = input("User name: ")
password = getpass()
# get_response = requests.get(endpoint, json={"producy_id":123})
auth_response = requests.post(auth_endpoint, json={"username":userName,"password":password})
# print(get_response.text)
print(auth_response.json())

if auth_response.status_code==200:
    token = auth_response.json()["token"]

    headers={
        "Authorization": f"Bearer {token}"
    }

    endpoint = "http://localhost:8000/api/products/"

    # get_response = requests.get(endpoint, json={"producy_id":123})
    get_response = requests.get(endpoint,headers=headers)
    # print(get_response.text)
    print(get_response.json())