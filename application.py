from flask import Flask, request
from chatbot import Chatbot
from response import send_message
from configs import app_config
import sys

application = Flask(__name__)

def verify_webhook(req):
    print(f'{req.args.get("hub.verify_token")} is the hub.verifyß', file=sys.stderr)
    if req.args.get("hub.verify_token") == app_config["VERIFY_TOKEN"]:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"


def respond(sender, message):
    """Formulate a response to the user and
    pass it on to a function that sends it."""

    chatbot = Chatbot()
    response = chatbot.respond(message)
    
    send_message(sender, response)


def is_user_message(message):
    """Check if the message is a message from the user"""
    return (
        message.get("message")
        and message["message"].get("text")
        and not message["message"].get("is_echo")
    )


@application.route("/", methods=["GET", "POST"])
def home():
    return "This is a homepage."


@application.route("/webhook", methods=["GET", "POST"])
def listen():
    """This is the main function flask uses to
    listen at the `/webhook` endpoint."""

    if request.method == "GET":
        return verify_webhook(request)

    if request.method == "POST":
        payload = request.json
        event = payload["entry"][0]["messaging"]
        for x in event:
            if is_user_message(x):
                text = x["message"]["text"]
                sender_id = x["sender"]["id"]
                respond(sender_id, text)

        return "ok"


if __name__ == "__main__":
    application.run(host="0.0.0.0", port="8888", debug=True)
