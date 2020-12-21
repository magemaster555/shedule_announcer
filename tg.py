import requests, json

class Tg:
    token:str
    chat_id = None
    def __init__(self, token, chat_id = None):
        self.token = token
        self.chat_id = chat_id

    def request(self, method, **params):
        r = requests.post(f"https://api.telegram.org/bot{self.token}/{method}", data=params).json()
        if not r['ok']:
            print("Ошибка TG API: "+str(r))
            return None
        return r['result']

    def say(self, text, to = None):
        if not to:
            if self.chat_id:
                to = self.chat_id
            else:
                print("Ошибка: Не указан ID для отправки сообщений. Отправка сообщения невозможна.")
                return None
        r = self.request("sendMessage", chat_id=to, text=text)
        return r
