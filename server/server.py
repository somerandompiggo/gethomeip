from flask import *
import getpass
import hashlib

homeip = ""

def startupchk():
    try:
        open("password").read()
    except:
        print("Password file not found. Please enter a password.")
        f = open("./password", "w")
        f.write(hashlib.sha256(getpass.getpass("Password: ").encode("UTF-8")).hexdigest())
        f.close()
        print("Done. Running Flask server")

def getpwhash():
    f = open("./password", "r")
    return f.read().strip()

def chkpass(password):
    print(hashlib.sha256(password.encode("UTF-8")).hexdigest())
    print(getpwhash())
    if (hashlib.sha256(password.encode("UTF-8")).hexdigest() == getpwhash()):
        return True
    else:
        return False

startupchk()

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("./index.html")

@app.route("/style")
def style():
    return send_file("./css/style.css")

@app.route("/access", methods=["POST"])
def access():
    global homeip
    if (chkpass(request.form.get("password"))):
        if (homeip == ""):
            return render_template("./access.html", ip=("The client has not sent an IP yet!"))
        else:
            return render_template("./access.html", ip=("Your home IP is: " + homeip))
    else:
        return render_template("./access.html", ip="That password is incorrect, please try again.")

@app.route("/set", methods=["POST"])
def set():
    global homeip
    if (chkpass(request.form.get("password"))):
        homeip = request.remote_addr
        return
    else:
        return

app.run(host='0.0.0.0')
