class SpyLogger:
    def __init__(self):
        self.msgs = []

    def send_info(self, msg):
        self.msgs.append(msg)