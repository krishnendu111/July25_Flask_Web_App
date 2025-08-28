from flask import Flask

app = Flask(__name__)

@app.route("/krish", methods=['GET'])
def hello_world():
    return "<p>Hello, World- My name is krish!</p>"

@app.route("/ping", methods=['GET'])
def pinger():
    return {'message': 'krish'}



