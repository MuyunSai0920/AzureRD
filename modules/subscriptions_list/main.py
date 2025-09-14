import requests
import pprint

def start(args):
    # Retrieve Access Token from a file
    token_file_path = input("Enter the filename of your access token [default: access_token.txt]: \n") or 'access_token.txt'
    with open(token_file_path, 'r') as file:
        access_token = file.read().strip()

    # Azure endpoint to list subscriptions
    url = 'https://management.azure.com/subscriptions?api-version=2020-01-01'

    # Set the authorization header with your access token
    headers = {'Authorization': f'Bearer {access_token}'}

    # Make the GET request to list subscriptions
    response = requests.get(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        subscriptions = response.json()
        print("\nRetrieving Subscription Information...")
        pprint.pprint(subscriptions)
        
        print("\nListing Subscription IDs...")
        for subscription in subscriptions['value']:
            print(f"Subscription ID: {subscription['subscriptionId']}, Display Name: {subscription['displayName']}")
    else:
        print(f'Error: {response.status_code} - {response.text}')
