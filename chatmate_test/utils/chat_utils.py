def to_str_messages(chat):
    if 'messages' not in chat:
        return ''
    else:
        return " ".join(chat['messages'])

def to_str_one(chat):
    return chat['id']

def to_str_many(chats):
    str_chats = []
    for chat in chats:
        str_chats.append(to_str_one(chat))

    return str_chats

def to_chat(str_chats, promt):
    messages = []

    for str_chat in str_chats:
        chat = str_chat.split(":")
        msg = {'text': chat[0], 'name': chat[1]}
        messages.append(msg)

    return {'messages': messages, 'promt': promt}
