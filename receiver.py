from flask import Flask
app = Flask(__name__)
from twilio.twiml.messaging_response import MessagingResponse


@app.route("/cardapio", methods=['POST', 'GET'])
def hello():
    resp = MessagingResponse ()
    resp.message ("Arroz, feijão, batata e macarrão.")
    return str (resp)


if __name__ == "__main__":
    app.run(debug=True)

