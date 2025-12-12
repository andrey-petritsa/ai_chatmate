from chatmate_details.gui.chat_presenter import ChatPresenter


class TestChatPresenter:
    def test_to_view_chat_info(self):
        presenter = ChatPresenter()
        chat_info = {
            'id': 1,
            'name': 'Анна',
            'is_handled': False,
            'avatar_url':'avatar_url',
            'last_message_timedelta': {'days': 137, 'hours': 23, 'minutes': 43},
            'is_answered': True,
        }
        chat_info_view = presenter.to_view_chat_info(chat_info)

        e_chat_view_info = {
            'id': 1,
            'name': 'Анна',
            'avatar_url':'avatar_url',
            'last_message_hint': '137 дней',
            'is_answered_status_icon': '👀',
        }
        assert chat_info_view == e_chat_view_info

    def test_present(self):
        presenter = ChatPresenter()

        chat = {
            'name': 'Чат',
            'messages': [
                {'name': 'bot', 'text': 'Тест1'},
                {'name': 'Анна', 'text': 'Тест2'},
                {'name': 'bot', 'text': 'Тест3'}
            ]
        }

        result = presenter.to_view_chat(chat)
        
        expected_messages = [
            {'name': 'bot', 'text': 'Тест1', 'position': 'left'},
            {'name': 'Чат', 'text': 'Тест2', 'position': 'right'},
            {'name': 'bot', 'text': 'Тест3', 'position': 'left'}
        ]
        
        assert result['messages'] == expected_messages