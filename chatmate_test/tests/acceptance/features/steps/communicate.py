from behave import given, when, then

from chatmate_business.usecases.get_chats_command import GetChatsCommand
from chatmate_business.usecases.send_message_command import SendMessageCommand
from chatmate_test.mocks.platform_spy import PlatformSpy
from mocks.stub_assistant import StubAssistant


@given("есть платформа")
def step(context):
    platform = PlatformSpy()
    context.platform = platform

@when("общаюсь с собеседником платформы")
def step(context):
    cmd = SendMessageCommand()
    cmd.platform = context.platform
    cmd.assistant = StubAssistant()

    cmd.execute(chat={'id': 1})

@when("запрашиваю список собеседников платформы")
def step(context):
    cmd = GetChatsCommand()
    cmd.platform = context.platform

    persons = cmd.execute()
    context.persons = persons

@then('ии отправляет собеседнику сообщение')
def step(context):
    assert 'SendMessage 1->привет от ии' in context.platform.events

@then("получаю список собеседников платформы")
def step(context):
    assert len(context.persons) != 0



