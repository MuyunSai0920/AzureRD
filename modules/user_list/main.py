import subprocess
import json
import pprint

def start(args):

    if len(args) > 0:
        return

    print("Getting AD users...")

    user_list = subprocess.run(['az', 'ad', 'user', 'list'], stdout=subprocess.PIPE)
    user_list_json = json.loads(user_list.stdout.decode('utf-8'))

    pprint.pprint(user_list_json)
