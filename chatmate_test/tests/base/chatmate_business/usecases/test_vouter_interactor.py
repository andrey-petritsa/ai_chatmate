from chatmate_details.factory.app_factory import AppFactory
from mocks.platform_spy import PlatformSpy
from mocks.spy_voter_port import SpyVoterPort
from mocks.stub_assistant import StubAssistant
import time



class TestVoterInteractor:
    def test_start_vote(self):
        interactor = AppFactory.create_voter_interactor()
        interactor.platform = PlatformSpy()
        interactor.voter_port = SpyVoterPort()
        interactor.chatmate_assistant = StubAssistant()

        chat = {'id': '1', 'msgs': []}
        interactor.set_chat(chat)
        interactor.start_vote()

        assert 'старт' in interactor.voter_port.sended_msg

    def test_end_vote(self):
        interactor = AppFactory.create_voter_interactor()
        interactor.platform = PlatformSpy()
        interactor.voter_port = SpyVoterPort()
        interactor.chatmate_assistant = StubAssistant()

        interactor.voter_port.msgs = [
            {'text':'2', 'is_my':False, 'name':'Павел', 'date':int(time.time()) + 1, 'sender':{'id':'Павел'}},
        ]
        chat = {'id': '1', 'msgs': []}
        interactor.set_chat(chat)
        interactor.start_vote()
        interactor.end_vote()

        assert 'завершено' in interactor.voter_port.sended_msg
        assert ['SendMessage 1->привет от ии 2'] == interactor.platform.events