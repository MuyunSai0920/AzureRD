import subprocess
import json
import pprint

def start(args):

    if len(args) > 0:
        return

    print("Getting AD groups...")

    group_list = subprocess.run(['az', 'ad', 'group', 'list'], stdout=subprocess.PIPE)
    group_list_json = json.loads(group_list.stdout.decode('utf-8'))

    pprint.pprint(group_list_json)
