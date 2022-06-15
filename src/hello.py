''' this is hello world python module '''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''this is a hello world python function'''
    return 'hello ci cd pipeline 4:59pm'

app.run(host='0.0.0.0', port=8080)
