import time
from chatmate_details.chatmates.chatgpt.chatgpt_page import ChatgptPage


class BrowserChatgpt:
    def __init__(self):
        self.page = ChatgptPage()

    def ask_question(self, chat_name, text):
        self.page.go_to_chat(chat_name)
        self.page.write_text(text)
        return self.page.get_last_chat_message()

    def close(self):
        self.page.close()

if __name__ == "__main__":
    browser = BrowserChatgpt()
    answer = browser.ask_question('test', 'Как дела?')
    print(answer)
    time.sleep(100)
