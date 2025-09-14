import requests
import getpass
import json
import jwt
import pprint

def start(args):
    # Define the URL you want to make the POST request to
    url = 'https://login.microsoftonline.com/'
    tenant_id = input("Enter Tenant ID: \n")
    path = '/oauth2/v2.0/token'

    client_id = input("Enter Application (Client) ID: \n")
    client_secret = getpass.getpass("Enter Client Secret: \n")

    # Sanitize and trim the user's input (remove leading/trailing whitespace)
    tenant_id = tenant_id.strip()
    client_id = client_id.strip()

    # Define the data you want to send in the request body as a dictionary
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default',
        'grant_type': 'client_credentials'
    }

    # Send the POST request with the data
    response = requests.post(url + tenant_id + path, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print('POST request was successful')
        # You can access the response content if needed
        print('Response content:')
        pprint.pprint(response.text)

        response_data = response.json()
        #if "access_token" in response_data:
        print('\nDecoding JWT Token...')
        print('\nDecoded Access Token: ')
        pprint.pprint(jwt.decode(response_data.get("access_token", "Missing: access_token"), algorithms=None, options={"verify_signature": False}))
    else:
        print('POST request failed with status code:', response.status_code)
