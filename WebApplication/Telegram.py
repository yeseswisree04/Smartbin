import json, requests


""" Telegram Access Parameters. """
Telegram_ChatID = "@Smartbin3" #"@CHAT ID OF THE TELEGRAM CHANNEL"
Telegram_bottoken = "bot2038238671:AAEXTO6fNXzgG3DUBntyVnZy1At0tRkZG1w" #"TELEGRAM BOT TOKEN START WITH BOT[FOLLOWED BY TOKEN]"


# sms = Sms(Twilio_SSID, Twilio_Auth, My_Number, Twilio_Number)

def sendTelegram (Telegram_ChatID, Telegram_bottoken, message):
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

# sendTelegram(Telegram_ChatID, Telegram_bottoken,"Hello")