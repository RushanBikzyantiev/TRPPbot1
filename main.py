import vk_api
import time
import random

token = "04b2b43f23c55e32f201c68ff2791a2732fc8dd2ab8b046e24316c4a8f5c96ddbc77b9c4096e908321b5f"

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    try:

        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Здравствуйте, выберете команду:"
                                                     "\n- сайт"
                                                     "\n- программа", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "сайт":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": "ссылка на наш сайт:https://tatarlove.ru/",
                           "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "программа":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": "наше android-приложение:https://play.google.com/store/apps/details?id=tlmobile.TLMobile&hl=ru&gl=US",
                           "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "Для того, чтобы разместить свою информацию у нас в группе, зарегистрируйтесь у нас на сайте http://tatarlove.ru и вышлите нам ссылку на свою анкету.", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
