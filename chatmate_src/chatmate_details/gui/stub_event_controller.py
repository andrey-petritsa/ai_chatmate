
class StubEventController:
    def handle_event(self, event):
        print(event)

        if event['name'] == 'show_options':
            return ['оп1', 'оп2']

        if event['name'] == 'get_chat':
            return {'id': 1, 'name': 'Анастасия', 'messages': [
                {'name': 'Андрей', 'text': 'Тест1', 'position': 'left'},
                {'name': 'Анна', 'text': 'Тест2', 'position': 'right'},
                {'name': 'Анна', 'text': 'Новое сообщение', 'position': 'right'}
            ]}