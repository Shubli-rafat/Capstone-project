#!/usr/local/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello WORLD! My name is Shubli Rafat and this is my Capstone Project<h2h>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
