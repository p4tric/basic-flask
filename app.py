import json
import os
import re
import requests

from dotenv import load_dotenv
from flask import Flask, Response, request, redirect

from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Say

if os.path.exists(os.getcwd() + '/config.json'):
    with open('./config.json') as f:
        configData = json.load(f)
else:
    configTemplate = {
        "BOT_TOKEN": "",
        "CMC_TOKEN": ""
    }

    with open(os.getcwd() + '/config.json', 'w+') as f:
        json.dump(configTemplate, f)

load_dotenv()

bot_token = configData['BOT_TOKEN']
cmc_token = configData['CMC_TOKEN']

app = Flask(__name__)

def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def parse_msg(msg):
    chat_id = msg['message']['chat']['id']
    msg_txt = msg['message']['text']

    pattern = r'/[a-zA-Z]{2-4}'
    ticker = re.findall(pattern, msg_txt)
    if ticker:
        symbol = ticker[0][1:] # /btc ==> btc
    else:
        symbol = ''

    return chat_id, symbol


def send_msg(chat_id, text='You chinese?'):
    url = 'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = { 'chat_id': chat_id, 'text': text }

    r = requests.post(url, json=payload)
    return r


def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = { 'symbol': crypto, 'convert': 'USD' }
    headers = { 'X-CMC_PRO_API_KEY': cmc_token }


@app.route("/telegram", methods=['GET', 'POST'])
def zmz_reply():
    print(request.method)
    if request.method == 'POST':
        msg = request.get_json()
        print(msg)

        chat_id, symbol = parse_msg(msg)
        print(chat_id)
        print(symbol)

        if not symbol:
            send_msg(chat_id, 'Dope data')
            return Response('Ok', status=200)

        price = get_cmc_data(symbol)
        print(price)
        send_msg(chat_id, price)
        # write_json(msg, 'telegram_request.json')
        return Response('Ok', status=200)
    else:
        print('else H1')
        return '<h1>Hapichair Bot</h1>'

@app.route("/whatsapp", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    # resp.message("The Robots are coming! Head for the hills!")

    # Determine the right reply for this message
    if body == 'hello':
        msg = resp.message("Hi!")
        msg.media("https://images.pexels.com/photos/4126695/pexels-photo-4126695.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
    elif body == 'bye':
        msg = resp.message("Goodbye")
        # Add a picture message
        msg.media("https://images.pexels.com/photos/246804/pexels-photo-246804.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
    elif body == 'when':
        #resp = VoiceResponse()
        #resp.say('The Robots are coming! Head for the hills!')
        msg = resp.message("The Robots are coming! Head for the hills!")
        msg.media("https://images.pexels.com/photos/2085831/pexels-photo-2085831.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
    elif body == 'hi bangboy!':
        msg = resp.message("hi!")
        msg.media("https://scontent.fsin10-1.fna.fbcdn.net/v/t1.6435-9/134744884_2836624303292522_2481575298273072520_n.jpg?_nc_cat=110&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=Kcglr8XTHt4AX-mM1_q&_nc_ht=scontent.fsin10-1.fna&oh=97e1c7f6118d75d94d6392435aabb5c9&oe=60A38F87")
    else:
        msg = resp.message("Indeed.")


    return str(resp)

@app.route("/")
def hello():
  return "(x_-)___ ..|.."

if __name__ == "__main__":
    app.run()