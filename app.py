from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/newtest')
def hello_world_newtest():
    return 'Hello world - new test'