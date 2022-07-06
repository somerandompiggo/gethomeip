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

def gethomeip():
    return("real")

startupchk()

app = Flask(__name__)

@app.route("/")
def index():
    return(send_file("index.html"))

@app.route("/style")
def style():
    return(send_file("css/style.css"))

@app.route("/access", methods=["POST"])
def access():
    if (hashlib.sha256(request.form.get("password").encode("UTF-8")).hexdigest() == getpwhash()):
        return(render_template("access.html", ip=gethomeip()))
    else:
        return(render_template("access.html", ip="Incorrect password"))

app.run()