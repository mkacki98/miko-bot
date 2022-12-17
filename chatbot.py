import random
from chatbot_components import greetings, goodbyes, responses


class StupidBot:
    def is_input_message(self, message):

        message = message.lower()
        if message in greetings:
            return True
        return False

    def is_goodbye_message(self, message):

        message = message.lower()
        if message in goodbyes:
            return True
        return False

    def respond(self, input_message):

        if self.is_input_message(input_message):
            return "Wazaaaap"

        if self.is_goodbye_message(input_message):
            return "I was bored with this conversation anyway.."

        return random.choice(responses)
