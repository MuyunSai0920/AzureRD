import requests
import pprint

def start(args):
    # Retrieve Access Token from a file
    token_file_path = input("Enter the filename of your access token [default: access_token.txt]: \n") or 'access_token.txt'
    with open(token_file_path, 'r') as file:
        access_token = file.read().strip()

    subscription_id = input("Enter subscription ID: ")

    # Replace '{subscriptionId}' with your actual Azure subscription ID
    url = f'https://management.azure.com/subscriptions/{subscription_id}?api-version=2021-04-01'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pprint.pprint(response.json())
    else:
        print(f'Error: {response.text}')
