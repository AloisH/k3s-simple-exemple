from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route("/whoami")
def whoami():
    return os.environ.get("WHOAMI", "No hostname set");
