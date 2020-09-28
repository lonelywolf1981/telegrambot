import requests
import json
from teltoken import teltoken
from flask import Flask
from flask_sslify import SSLify


app = Flask(__name__)
#sslify = SSLify(app)

URL = 'https://api.telegram.org/bot' + teltoken + '/'

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_updates():
    url = URL + "getUpdates"
    r = requests.get(url)
    #write_json(r.json())
    return r.json()


def send_message(chat_id, text='bla-bla-ba'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


@app.route('/')
def index():
    return '<h1>Helo bot!</h1>'

#def main():
#     r = requests.get(URL + 'getMe')
#     #write_json(r.json())
#     r = get_updates()
#     chat_id = r['result'][-1]['message']['chat']['id']
#     send_message(chat_id)


if __name__ == '__main__':
    app.run()
