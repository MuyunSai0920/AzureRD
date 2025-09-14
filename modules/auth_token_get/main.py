
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import urllib.parse
import json
import pprint
import jwt
import re
import pyperclip


# A function to extract authorization code from a copied URL
def extract_code_from_url(url):
    pattern = r"[?&]code=([^&]+)"

    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None


def start(args):

    # Step 1: Configure your credentials and URLs
    tenant_id = input("Enter your tenant ID: ")
    client_id = input("Enter your client ID: ")
    client_secret = input("Enter your client secret: ")
    redirect_uri = "https://oauth.pstmn.io/v1/browser-callback"  # This should match the registered redirect URI
    authorization_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize"
    token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    #scope = "https://graph.microsoft.com/DelegatedPermissionGrant.ReadWrite.All"  # Adjust the scope according to your needs
    #scope = "https://graph.microsoft.com/.default openid profile"
    #scope = "https://management.azure.com/.default openid profile"

    # Use a selection menu to let user choose from a set of pre-defined scopes
    print("\nPlease select a scope from the following list:")
    scope_options = [
    "https://graph.microsoft.com/.default openid profile",
    "https://management.azure.com/.default openid profile"
    ]
    for number, option in enumerate(scope_options, start=1):
        print(f"{number}. {option}")

    scope_choice = int(input("Please enter your choice of scope (by number): "))
    while (scope_choice < 1 or scope_choice > len(scope_options)):
        scope_choice = int(input("Please re-enter your choice of scope (by number): "))
    scope = scope_options[scope_choice-1]


    access_token_file = "access_token.txt"

    # Step 2: Redirect user to Microsoft login page
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scope,
        "response_mode": "query"
    }
    login_url = f"{authorization_url}?{urllib.parse.urlencode(params)}"
    print("The default web browser will be opened, please login and copy the URL to which you are redirected to after login...")
    webbrowser.open_new(login_url)

    check_continue = input("Type y after you copied the URL: ")
    while check_continue != "y":
        check_continue = input("Type y after you copied the URL: ")

    copied_text = pyperclip.paste()
    auth_code = extract_code_from_url(copied_text)
    print("\nUsing Authorization Code: " + auth_code)

    data = {
    'client_id': client_id,
        'code': auth_code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
        'client_secret': client_secret
    }

    # Send the POST request with the data
    response = requests.post(token_url, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print('\nPOST request was successful')
        # You can access the response content if needed
        print('Response content:')
        pprint.pprint(response.text)

        response_data = response.json()

        #if "access_token" in response_data:
        # Output the access token to a separated file for future API call
        with open(access_token_file, 'w') as file:
            file.write(response_data.get("access_token", "Missing: access_token"))
        print(f'\nAccess Token written to {access_token_file}')

        print('\nDecoding JWT Token...')
        print('\nDecoded Access Token: ')
        pprint.pprint(jwt.decode(response_data.get("access_token", "Missing: access_token"), algorithms=None, options={"verify_signature": False}))
        print('\nDecoded ID Token: ')
        pprint.pprint(jwt.decode(response_data.get("id_token", "Missing: id_token"), algorithms=None, options={"verify_signature": False}))
    else:
        print('POST request failed with status code:', response.status_code)
