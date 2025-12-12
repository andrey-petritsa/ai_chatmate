from chatmate_details.chatmates.deepseek.deepseek_assistant import DeepseekAssistant


class TestDeepseekAssistant:
    def test_generate_message(self):
        msgs = [
            {'text': 'привет!'}
        ]
        chat = {'msgs': msgs}
        assistant = DeepseekAssistant()

        msg = assistant.generate_message(chat)

        assert msg != None

    def test_generate_messages(self):
        msgs = [
            {'text': 'привет!'}
        ]
        chat = {'msgs': msgs}
        assistant = DeepseekAssistant()

        msgs = assistant.generate_messages(chat)

        assert len(msgs) > 1