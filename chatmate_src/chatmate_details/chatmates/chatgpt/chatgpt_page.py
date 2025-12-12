import os
from playwright.sync_api import sync_playwright
import time

class ChatgptPage:
    def __init__(self):
        self.playwright = sync_playwright().start()

        profile_path = os.path.abspath("settings/firefox-profile")

        self.context = self.playwright.firefox.launch_persistent_context(
            user_data_dir=profile_path,
            headless=True
        )

        self.page = self.context.pages[0]
        self.__go_to_main_page()

    def __go_to_main_page(self):
        self.page.goto("https://chatgpt.com", wait_until="networkidle")

    def go_to_chat(self, chat_name):
        self.page.get_by_text(chat_name, exact=True).first.click()
        self.page.wait_for_selector('div[data-message-id]')

    def write_text(self, msg):
        for line in msg.split("\n"):
            self.page.keyboard.type(line)
            self.page.keyboard.press("Shift+Enter")
        self.page.keyboard.press("Enter")

    def get_last_chat_message(self):
        self.__wait_until_chat_ready()
        messages = self.page.locator("div[data-message-author-role='assistant']")

        count = messages.count()
        last = messages.nth(count - 1)

        text = last.inner_text()
        text = text.strip()

        return text

    def __wait_until_chat_ready(self):
        self.page.wait_for_selector('[data-testid="stop-button"]',state='detached',timeout=15000)

    def close(self):
        self.context.close()
        self.playwright.stop()

    #Need block impl
    def create_chat(self, chat_name):
        self.page.get_by_text('New chat', exact=True).first.click()
        self.write_text('Привет!')
        self.rename_last_chat(chat_name)

    #Need block impl
    def rename_last_chat(self, chat_name):
        last_chat = self.page.locator("#history > *").first
        last_chat.hover()
        last_chat.locator("button").click()
        rename_btn = self.page.get_by_role("menuitem", name="Rename")
        rename_btn.click()
        time.sleep(2)
        self.write_text(chat_name)
        self.page.reload()