import subprocess
import json
import pprint

def start(args):

    if len(args) > 0:
        return

    client_id = input("Enter Application (Client) ID: \n")
    client_id = client_id.strip()

    print("Listing App Permission...")
    permission_list = subprocess.run(['az', 'ad', 'app', 'permission', 'list', '--id', client_id], stdout=subprocess.PIPE)
    permission_list_json = json.loads(permission_list.stdout.decode('utf-8'))

    pprint.pprint(permission_list_json)
