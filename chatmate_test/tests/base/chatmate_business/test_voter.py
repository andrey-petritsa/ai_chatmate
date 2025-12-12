from chatmate_business.vouter.voter import Voter
from mocks.stub_time_provider import StubTimeProvider


class TestVoter:
    def setup_method(self):
        self.voter = Voter()
        self.voter.time_provider = StubTimeProvider()

    def test_voter_declare_voting_start_empty_chat(self):
        self.voter.set_user_msgs([])
        self.voter.set_chatmate_msgs(['Ответ от бота!'])

        assert self.voter.declare_voting_start() == [
            '🚀 Голосование старт! Выберите лучший вариант отправив цифру в ответ! 🚀',
            '👻 В чате пока нет сообщений! 👻',
            '🔹🔹🔹',
            '1. Ответ от бота!',
            '🔹🔹🔹'
        ]

    def test_voter_declare_voting_start(self):
        self.voter.set_user_msgs([
            {'text':'Привет!', 'is_my':True, 'name':'Андрей'},
            {'text':'Привет!!', 'is_my':False, 'name':'Вика'}
        ])
        self.voter.set_chatmate_msgs(['Ответ от бота!'])

        assert self.voter.declare_voting_start() == [
            '🚀 Голосование старт! Выберите лучший вариант отправив цифру в ответ! 🚀',
            '⭐️⭐️⭐️',
            '🤖 Андрей: Привет!',
            '❤️ Вика: Привет!!',
            '⭐️⭐️⭐️',
            '🔹🔹🔹',
            '1. Ответ от бота!',
            '🔹🔹🔹'
        ]

    def test_voter_declare_voting_end(self):
        self.voter.set_chatmate_msgs(['Ответ от бота 1!', 'Ответ от бота 2!'])
        self.voter.set_voter_msgs([
            {'text':'2', 'is_my':False, 'name':'Павел', 'date':0, 'sender':{'id':'Павел'}},
            {'text':'2', 'is_my':False, 'name':'Николай', 'date':0, 'sender':{'id':'Николай'}},
            {'text':'1', 'is_my':False, 'name':'Василий', 'date':500, 'sender':{'id':'Василий'}},
            {'text':'Спам аахха', 'is_my':False, 'name':'Василий', 'date':500, 'sender':{'id':'Василий'}},
            {'text':'2', 'is_my':False, 'name':'Николай', 'date':501, 'sender':{'id':'Николай'}},
            {'text':'1', 'is_my':False, 'name':'Василий', 'date':502, 'sender':{'id':'Василий'}}
        ])
        self.voter.time_provider.now_date_timestamp = 500
        self.voter.vote_time_start = 500
        self.voter.declare_voting_end()

        assert self.voter.declare_voting_end() == [
            '🏁 Голосование завершено! 🏁',
            '🎉 Ответ от бота 1!'
        ]

    def test_get_winner(self):
        self.voter.set_chatmate_msgs(['Первое сообщение'])
        self.voter.set_voter_msgs([{'text':'1', 'is_my':False, 'name':'Николай', 'date':1, 'sender':{'id':'Николай'}}])

        assert 'Первое сообщение' == self.voter.get_winner()

    def test_has_winner(self):
        self.voter.set_chatmate_msgs(['Первое сообщение'])
        self.voter.set_voter_msgs([])
        assert False == self.voter.has_winner()

        self.voter.set_chatmate_msgs(['Первое сообщение'])
        self.voter.set_voter_msgs([{'text': '1', 'is_my':False, 'name': 'Николай', 'date': 1, 'sender': {'id': 'Николай'}}])
        assert True == self.voter.has_winner()

