import requests
import json
import pprint


def start(args):
    # Replace these values with your actual Azure details
    subscription_id = input("Enter your Azure subscription ID: ")
    resource_group_name = input("Enter the resource group name (defualt: test): ") or "test"
    vm_name = input("Enter the VM name (default: testVM): ") or "testVM"
    location = input("Enter the location (default: eastus): ") or "eastus"
    admin_username = input("Enter the admin username: ")
    admin_password = input("Enter the admin password: ")

    token_file_path = input("Enter the filename of your access token [default: access_token.txt]: \n") or 'access_token.txt'
    with open(token_file_path, 'r') as file:
        access_token = file.read().strip()

    # Create VM configuration
    vm_config = {
    "location": f"{location}",
    "properties": {
        "hardwareProfile": {
        "vmSize": "Standard_B1s"
        },
        "storageProfile": {
        "imageReference": {
            "publisher": "canonical",
            "offer": "0001-com-ubuntu-server-focal",
            "sku": "20_04-lts-gen2",
            "version": "latest",
            "exactVersion": "20.04.202312080"
        },
        "osDisk": {
            "osType": "Linux",
            "name": "test.lin.api",
            "createOption": "FromImage",
            "caching": "ReadWrite",
            "managedDisk": {
            "storageAccountType": "Standard_LRS"
            }
        }
        },
        "osProfile": {
        "adminUsername": f"{admin_username}",
        "computerName": "myVM",
        "adminPassword": f"{admin_password}"
        },
        "networkProfile": {
        "networkInterfaces": [
            {
                "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkInterfaces/test_NIC3",
            "properties": {
                "primary": "true"
            }
            }
        ]
        }
    }
    }

    # Create the VM using HTTP request
    create_vm_url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}?api-version=2023-07-01"

    headers = {
        'Content-Type': 'application/json',
        "Authorization": f'Bearer {access_token}',
    }

    response = requests.put(create_vm_url, headers=headers, data=json.dumps(vm_config))

    if response.status_code == 201:
        print("VM creation successful.")
    else:
            print(f"Error creating VM. Status code: {response.status_code}")
            pprint.pprint(response.text)
