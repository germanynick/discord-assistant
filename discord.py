
import time
import websocket as ws
import requests

def send_message(message):
    
    url = "https://discord.com/api/v9/channels/1193403120986902538/messages" #input channel exp: .../1190017920013713531/...
    payload = { 
        "content" : {message} #input content message @username before the content message
    }

    headers = {
        "Authorization" :"MTA2NDI3MDQyODYzOTYwMDY1MA.GxMMsR.UlMotld5pFexeztkJuVzfd_oaDz9eIX7FTCbFU"
    }

    res = requests.post(url, payload, headers=headers)
    return message