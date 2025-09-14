import subprocess
import json
import pprint

def start(args):

    if len(args) > 0:
        return

    print("Getting signed-in AD users...")

    print("Signed-in AD Users:")
    user_list = subprocess.run(['az', 'ad', 'signed-in-user', 'show'], stdout=subprocess.PIPE)
    user_list_json = json.loads(user_list.stdout.decode('utf-8'))

    pprint.pprint(user_list_json)

    print("\nSigned-in Users Owned Objects:")
    user_owned_objects = subprocess.run(['az', 'ad', 'signed-in-user', 'list-owned-objects'], stdout=subprocess.PIPE)
    user_owned_objects_json = json.loads(user_owned_objects.stdout.decode('utf-8'))

    pprint.pprint(user_owned_objects_json)
