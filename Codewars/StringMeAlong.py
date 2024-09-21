class MessageBuilder:
    def __init__(self, initial_message):
        self.messages = [initial_message]
    
    def __call__(self, new_message=None):
        if new_message is not None:
            self.messages.append(new_message)
            return self  # Return the instance for chaining
        return ' '.join(self.messages)  # Return the joined messages

def create_message(initial_message):
    return MessageBuilder(initial_message)