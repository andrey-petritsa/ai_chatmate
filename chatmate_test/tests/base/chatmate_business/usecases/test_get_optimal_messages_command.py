from chatmate_business.usecases.get_optomal_messages_command import GetOptimalMessagesCommand
from mocks.stub_assistant import StubAssistant


class TestGetOptimalMessagesCommand:
    def test_execute(self):
        cmd = GetOptimalMessagesCommand()
        cmd.assistant = StubAssistant()

        chat = {'id': 1, 'msgs':[]}
        msgs = cmd.execute(chat)

        assert len(msgs) == 2