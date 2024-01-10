
import time
import websocket as ws
import requests

def send_message(token, message):
    
    if token is None or token == "":
        return "Please input a token"

    url = "https://discord.com/api/v9/channels/1193403120986902538/messages" #input channel exp: .../1190017920013713531/...
    payload = { 
        "content" : {message} #input content message @username before the content message
    }

    headers = {
        "Authorization" : {token}
    }

    res = requests.post(url, payload, headers=headers)
    return message