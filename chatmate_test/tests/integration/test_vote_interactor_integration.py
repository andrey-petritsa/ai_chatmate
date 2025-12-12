import time

from chatmate_details.factory.app_factory import AppFactory

gleb_chat_id = '@mark_kl2025'

class TestVoteInteractorIntegration:
    def test_interactor_no_winner(self):
        get_chats_command = AppFactory.create_get_chats_command()
        voter_interactor = AppFactory.create_voter_interactor()

        chat = get_chats_command.execute()[0]
        voter_interactor.set_chat(chat)
        voter_interactor.start_vote()
        voter_interactor.end_vote()

    def test_interactor_has_winner(self):
        get_chats_command = AppFactory.create_get_chats_command()
        voter_interactor = AppFactory.create_voter_interactor()

        chat = get_chats_command.execute()[0]
        voter_interactor.set_chat(chat)
        voter_interactor.start_vote()
        time.sleep(10)
        voter_interactor.end_vote()


