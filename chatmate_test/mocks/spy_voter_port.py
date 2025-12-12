class SpyVoterPort:
    def __init__(self):
        self.sended_msg = ""
        self.msgs = []

    def send_message(self, text):
        self.sended_msg = text

    def get_messages(self):
        return self.msgs