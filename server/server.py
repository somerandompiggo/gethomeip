from flask import *
import getpass
import hashlib

def startupchk():
    try:
        open("password").read()
    except:
        print("Password file not found. Please enter a password.")
        f = open("password", "w")
        f.write(hashlib.sha256(getpass.getpass("Password: ").encode("UTF-8")).hexdigest())
        f.close()
        print("Done. Running Flask server")

def getpwhash():
    f = open("password", "r")
    return(f.read())

startupchk()

app = Flask(__name__)

@app.route("/")
def index():
    return(send_file("index.html"))

@app.route("/style")
def style():
    return(send_file("css/style.css"))

@app.route("/access")
def access():
    if (request.args("password") == getpwhash()):
        return(render_template("access.html", ip="yes"))

app.run()