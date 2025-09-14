import requests
import pprint


def start(args):
    token_file_path = input("Enter the filename of your access token [default: access_token.txt]: \n") or 'access_token.txt'
    with open(token_file_path, 'r') as file:
        access_token = file.read().strip()

    url = "https://graph.microsoft.com/v1.0/users"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {access_token}',
    }

    # Enter username and password
    name = input("Please enter username: ")
    password = input("Please enter password: ")

    mailName = input("Please enter mail nickname: ")
    principalName = input("Please enter principal name: ")


    payload = {
        "accountEnabled": True,
        "displayName": name, #"Adele Vance"
        "mailNickname": mailName, #"AdeleV"
        "userPrincipalName": f"{principalName}@keseceduoutlook.onmicrosoft.com", #"AdeleV@contoso.onmicrosoft.com"
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": password,
        },
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        # Check for successful response (HTTP status code 2xx)
        if response.status_code == 200 or response.status_code == 201:
            print("User created successfully.")
        else:
            print(f"Error creating user. Status code: {response.status_code}")
            pprint.pprint(response.text)

    except Exception as e:
        print(f"An error occurred: {e}")
