import requests
import getpass
import json
import time

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

def loadconf():
    f = open("conf.json", "r") 
    j = json.loads(f.read())
    if not "/set" in j["uri"]:
        if not j["uri"][-1] == "/":
            j["uri"] = j["uri"] + "/set"
        else:
            j["uri"] = j["uri"] + "set"
    return j

def mainloop():
    config = loadconf()
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'password': config["password"]}
    while True:
        try:
            session = requests.Session()
            session.post(config["uri"], headers=headers,data=payload)
            time.sleep(15)
        except: pass

startupchk()
mainloop()
