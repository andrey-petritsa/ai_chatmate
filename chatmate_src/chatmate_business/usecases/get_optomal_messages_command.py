class GetOptimalMessagesCommand:
    def __init__(self, assistant=None):
        self.assistant = assistant

    def execute(self, chat):
        msgs = self.assistant.generate_messages(chat)
        return msgs