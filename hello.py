from flask import Flask

app = Flask(__name__)

@app.route("/suraaj", methods=['GET'])
def hello_world():
    return "<p>Hello, World- My name is suraaj!</p>"

@app.route("/ping", methods=['GET'])
def pinger():
    return {'message': 'suraaj'}



