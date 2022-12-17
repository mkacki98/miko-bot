""" Module with an echo bot. """

import random
from chatbot_components import greetings, goodbyes, responses

class StupidBot:
    def is_greeting_message(self, message):
        """ Check if the message is a greeting. """

        message = message.lower()
        if message in greetings:
            return True
        return False

    def is_goodbye_message(self, message):
        """ Check if the message is a goodbye one. """

        message = message.lower()
        if message in goodbyes:
            return True
        return False

    def respond(self, input_message):
        """ Respond to a message according to simple rules. """

        if self.is_greeting_message(input_message):
            return random.choice(greetings)

        if self.is_goodbye_message(input_message):
            return "I was bored with this conversation anyway.."

        return random.choice(responses)
