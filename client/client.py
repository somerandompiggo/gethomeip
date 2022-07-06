import requests
import getpass
import json

def startupchk():
    try:
        open("conf.json").read()
    except:
        print("Config file not found. Please enter a password and the URI to the server.\nRemember, the client password is stored in plaintext!")
        config = {}
        config["password"] = getpass.getpass("Password: ")
        config["uri"] = input("URI: ")
        f = open("conf.json", "w")
        f.write(json.dumps(config))
        f.close()
        print("Done. Running client.")

startupchk()
