from behave import given, when, then

from mocks.spy_messanger import SpyMessanger
from mocks.testable_daivinchik import TestableTelegramPlatform


@given("есть платформа дайвинчик")
def step(context):
    messanger = SpyMessanger()
    platform = TestableTelegramPlatform(messanger)
    platform.messanger = messanger

    context.platform = platform
    context.messanger = messanger

@given("у пользователя платформы есть сообщения о метчах в главном чате")
def step(context):
    context.platform.main_chat = [
        'С вами хотят познакомиться! Идентификатор чата 123'
    ]

@when("общаюсь с собеседником дайвинчика")
def step(context):
    context.platform.send_message(chant_id=1, text='привет')

@when("запрашиваю список собеседников дайвинчика")
def step(context):
    persons = context.platform.get_chats()
    context.persons = persons

@then('собседнику дайвинчика отправляется сообщение')
def step(context):
    assert 'send_message 1->привет' in context.messanger.events

@then("получаю список собеседников дайвинчика")
def step(context):
    assert len(context.persons) != 0




