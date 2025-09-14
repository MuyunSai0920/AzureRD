import json
import jwt
import re
import pprint

def start(args):
    file_path = input("Enter the file path where the bearer token is stored: \n")

    try:
    # Open and read the file
        with open(file_path, 'r') as file:
            token = file.read().strip()
            print("File Contents:")
            print(token)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    print('\nDecoding JWT Token...')
    decode_token = jwt.decode(token, algorithms=None, options={"verify_signature": False})

    version = decode_token.get("ver", "Missing: ver")
    issuer = decode_token.get("iss", "Missing: iss")
    tenant_id = decode_token.get("tid", "Missing: tid")

    print("ver: " + version)
    if version != "1.0":
        print("This JWT is NOT issued by Microsoft Entra-only applications!")
        return

    print("issuer: " + issuer)
    azure_issuer_pattern = r"^https:\/\/sts.windows.net\/"
    if not re.match(azure_issuer_pattern, issuer):
        print("This JWT does NOT belongs to Azure!")
        return

    print("tenant_id: " + tenant_id)
    azure_tenant_id_pattern = r"^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$"
    if not re.match(azure_tenant_id_pattern, tenant_id):
        print("This JWT does NOT belongs to Azure!")
        return

    print("All checks passed... This is an Azure bearer token!")
