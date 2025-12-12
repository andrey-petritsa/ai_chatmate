from playwright.sync_api import sync_playwright
#import chatmate_details.utils as utils

class VkDateTokenExtractor:
    @classmethod
    def extract(cls):
        with sync_playwright() as playwright:
            return cls.__extract_token_from(playwright)

    @classmethod
    def __extract_token_from(cls, playwright):
        browser = playwright.chromium.connect_over_cdp('http://127.0.0.1:9222')
        context = browser.contexts[0]
        page = context.new_page()
        page.on("request", lambda request: cls.__handle_request(cls, request))
        page.goto("https://vk.com/dating")
        page.wait_for_timeout(5000)

        if "У вас большие запросы!" in page.title():
            page.click('text=Продолжить')

        utils.logger.send_info(f"Токен {cls.token} получен из браузера")
        return cls.token

    @staticmethod
    def __handle_request(cls, request):
        endpoint_with_token = "https://dating.vk.com/api/user.state"
        if request.url == endpoint_with_token:
            token = cls.__extract_token(request.post_data)
            cls.token = token

    @staticmethod
    def __extract_token(post_data):
        boundary = post_data.splitlines()[0].split('=')[-1].strip()

        parts = post_data.split(f'--{boundary}')

        for part in parts:
            if 'Content-Disposition: form-data; name="_token"' in part:
                start = part.find("\r\n\r\n") + 4
                end = part.find("\r\n--")
                token = part[start:end].strip()
                return token

        raise Exception('Токен не найден в браузере')


