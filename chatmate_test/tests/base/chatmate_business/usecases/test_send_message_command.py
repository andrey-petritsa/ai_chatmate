from chatmate_test.mocks.platform_spy import PlatformSpy
from chatmate_business.usecases.send_message_command import SendMessageCommand
from mocks.stub_assistant import StubAssistant


class TestSendMessageCommand:
    def test_execute(self):
        platform = PlatformSpy()
        assistant = StubAssistant()
        cmd = SendMessageCommand(platform)
        cmd.assistant = assistant

        cmd.execute(chat={'id': 1, 'msgs':[]})

        assert "SendMessage 1->привет от ии" in platform.events