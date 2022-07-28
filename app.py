from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<body style="background-color:yellow;"><h1 style="color:blue;">Liron webserver</h1><p style="color:blue;">cyberpunk 2077 color scheme</p></body>'
