from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from .bandex_fetcher import fetch_bandex

app = Flask(__name__)


def get_app ():
    return app

@app.route("/cardapio", methods=['POST', 'GET'])
def asnwer_cardapio ():
    bandex_message = fetch_bandex ()

    resp = MessagingResponse ()
    resp.message (bandex_message)
    return str (resp)
