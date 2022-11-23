class Chatbot:

    def __init__(self):
        self.default_msg = "I like pancakes, do you?"

    def respond(self, input_message):
        
        if input_message == "hi":
            return "hi to you too!"
        if input_message == "thanks you":
            return "ur welcome man"

        return self.default_msg



