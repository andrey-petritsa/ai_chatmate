from chatmate_details.repository.in_file_chat_repository import InFileChatRepository


class TestInFileChatRepository:
    def setup_method(self):
        self.rep = InFileChatRepository()

    def test_save_chat(self):
        chat = {'id': 'test1', 'messages': [
            {'date': '2025-01-27T16:14:21.211Z', 'text': 'Тестовое сообщение'},
            {'date': '2025-01-27T16:14:21.211Z', 'text': 'Тест 123'},
        ]}

        self.rep.save(chat)
        saved_chat = self.rep.find_chat('test1')

        assert chat == saved_chat

    def test_find_all_chats(self):
        chat = {'id': 'test1', 'messages': [{'date': '2025-01-27T16:14:21.211Z', 'text': 'тст'}]}
        self.rep.save(chat)
        chat = {'id': 'test2', 'messages': [{'date': '2025-01-27T16:14:21.211Z', 'text': 'тст'}]}
        self.rep.save(chat)

        chats = self.rep.find_all_chats()
        assert len(chats) == 2