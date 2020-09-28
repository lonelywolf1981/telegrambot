import requests
import json
from teltoken import teltoken
# from flask import Flask
# from flask_sslify import SSLify
#
#
# app = Flask(__name__)
# sslify = SSLify(app)
#
# @app.route('/')
# def index():
#     return '<h1>Test Flask app</h1>'


URL = 'https://api.telegram.org/bot' + teltoken + '/'

def write_json():
    pass

def main():
    r = requests.get(URL + 'getMe')
    print(r.json())

if __name__ == '__main__':
    main()
#    app.run()
