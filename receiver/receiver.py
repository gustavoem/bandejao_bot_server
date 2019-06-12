from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


def get_app ():
    return app

@app.route("/cardapio", methods=['POST', 'GET'])
def hello():
    resp = MessagingResponse ()
    resp.message ("Arroz, feijão, batata e macarrão.")
    return str (resp)
