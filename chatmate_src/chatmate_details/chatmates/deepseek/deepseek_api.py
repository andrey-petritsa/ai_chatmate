import requests



class DeepseekApi:
    def __init__(self, token):
        self.token = token

    def get_chat_response(self, messages):
        url = "https://api.deepseek.com/chat/completions"
        headers = {"Content-Type": "application/json","Authorization": f"Bearer {self.token}"}

        data = {
            "model": "deepseek-chat",
            "messages":messages,
            "stream": False,
            "temperature": 0.8
        }

        response = requests.post(url, json=data, headers=headers)
        if not response.ok:
            raise Exception(response.text)

        return response