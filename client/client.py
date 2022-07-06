import request

def startupchk():
    try:
        open("password").read()
    except:
        print("Password file not found. Please enter a password.")
        f = open("password", "w")
        f.write(hashlib.sha256(getpass.getpass("Password: ").encode("UTF-8")).hexdigest())
        f.close()
        print("Done. Running Flask server")

startupchk()
