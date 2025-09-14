
import os
import importlib

# This function will clear the PowerShell interface
def clear_screen():
    os.system("clear")


# This function will execute the user-specified module
def exec_module(module_name, *args):

    file_path = os.path.join(os.getcwd(), 'modules', module_name, 'main.py')

    if os.path.exists(file_path):

        import_path = "modules.{}.main".format(module_name).replace("/", ".").replace("\\", ".")

        module = importlib.import_module(import_path)

        module.start(args)

    else:
        print(module_name, " does not exist")

def show_modules():
    print("------------------------")
    print("SELECT MODULES")
    print("------------------------")
    print("\t auth_token_get: Get Access Token and ID token using authorization code flow; requires tenant_id, client_id and client_secret")
    print("\t bearer_token_get : Get Access Token using client credentials flow; requires tenant_id, client_id and client_secret")
    print("\t bearer_token_validate : Validate if a bearer token is an Azure Oauth2.0 token, taken the file path to the token file as input")
    print("\t signed_in_user_list : List signed-in AD user")
    print("\t subscriptions_get : Get the informaiton of a Azure user subscription")
    print("\t subscriptions_list : List all Azure user subscriptions")
    print("\t user_list : List AD user")
    print("\t user_create : Create AD user")
    print("\t vm_create : Create VM")
    


def guide():
    print("""
    Please enter the following for the corresponding functions:\n
    modules -> List the modules available
    exec <module_name> -> Execute modules listed on the "module" function output
    guide -> View this guide message again
    exit -> Exit this tool
    """)

if __name__ == "__main__":

    command = ""

    print("Welcome!!!")
    guide()

    while command != "exit":

        command = input("AzPEXT $> ")

        user_command = command.split()

        if(user_command[0] == "exec"):
            if len(user_command) > 2:
                exec_module(user_command[1], user_command[2:])
            else:
                exec_module(user_command[1])

        elif(user_command[0] == "modules"):
            show_modules()

        elif(user_command[0] == "guide"):
            guide()

        elif(user_command[0] == "exit"):
            print("Exiting Tool...\nBye")
            exit()

        else:
            print("Error")
