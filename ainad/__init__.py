from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

    
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


