import json, requests

""" Telegram Access Parameters. """
Telegram_ChatID = "@Smartbin1" #"@CHAT ID OF THE TELEGRAM CHANNEL"
Telegram_bottoken = "bot1925206689:AAEtSxswtMrbicRhJCJeYgimZs6B8WzY9Vc" #"TELEGRAM BOT TOKEN START WITH BOT[FOLLOWED BY TOKEN]"




def sendTelegram (message):
    url = "https://api.telegram.org/" + Telegram_bottoken + "/sendMessage"
    data = {
        "chat_id": Telegram_ChatID,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("Response From Telegram")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as error:
            print("Error Occured while send Telegram")
            print(error)
            return False

sendTelegram("Hello")