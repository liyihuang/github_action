from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''this is a hello world python'''
    return 'Web App with Python Flask!!'

app.run(host='0.0.0.0', port=8080)
