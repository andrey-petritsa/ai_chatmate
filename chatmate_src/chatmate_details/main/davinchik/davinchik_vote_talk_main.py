import time

from chatmate_details.factory.app_factory import AppFactory
TIME_FOR_VOTE = 60

class DaivinchikMain:
    def __init__(self):
        self.voter_interactor = AppFactory.create_voter_interactor()
        self.get_chats_command = AppFactory.create_get_chats_command()

    def run(self):
        while True:
            for chat in self.get_chats_command.execute():
                self.voter_interactor.set_chat(chat)
                self.voter_interactor.start_vote()
                time.sleep(TIME_FOR_VOTE)
                self.voter_interactor.end_vote()
            time.sleep(60)

if __name__ == '__main__':
    main = DaivinchikMain()
    main.run()
