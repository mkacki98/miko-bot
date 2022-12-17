""" Module with an echo bot. """

import random
import requests

from configs import app_config

class StupidBot:

    def __init__(self):

        self.responses = [
        "i used to be an adventurer, then an arrow in my knee changed my plans..",
        "there are things more important than you, you know..",
        "did you know Peru has had 6 presidents in the past 5 years?",
        "you should try salsa, i think you'd love it.",
        "come to the dark side, we have cookies :)",
        ]

        self.greetings = ["hi", "hello", "welcome", "good morning", "wazaaaaaaaaap", "yo"]

        self.goodbyes = ["see you", "bye", "goodbye"]

    def is_greeting_message(self, message):
        """ Check if the message is a greeting. """

        message = message.lower()
        if message in self.greetings:
            return True
        return False

    def is_goodbye_message(self, message):
        """ Check if the message is a goodbye one. """

        message = message.lower()
        if message in self.goodbyes:
            return True
        return False

    def respond(self, input_message):
        """ Respond to a message according to simple rules. """

        if self.is_greeting_message(input_message):
            return random.choice(self.greetings)

        if self.is_goodbye_message(input_message):
            return "I was bored with this conversation anyway.."

        return random.choice(self.responses)

    def send_message(self, recipient_id, text):
        """Send a response to Facebook"""

        payload = {
            "message": {"text": text},
            "recipient": {"id": recipient_id},
            "notification_type": "regular",
        }

        auth = {"access_token": app_config["PAGE_ACCESS_TOKEN"]}

        response = requests.post(app_config["FB_API_URL"], params=auth, json=payload)

        return response.json()
