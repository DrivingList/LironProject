from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<body style="background-color:Yellow;"><h1 style="color:Blue;">Ayra is fat and super gay</h1></body>'

app.run(host='0.0.0.0', port=8081)
