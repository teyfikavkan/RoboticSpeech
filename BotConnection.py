import requests
import json
import os
# connectBot(myspeech) function takes the argument "myspeech" and
# it returns a string as the response of our talk
def connectBot(myspeech):
    url = "http://api.dahi.ai/dahi/bot/tkn/59f307dfe4b0f7db8924368b"
    values ="""
        {
        'recipientId': 'rec1',
        'message':
        {
          'text': '%s',
          'type': 'text'
        }
      }
    """

    headers = {
        'Content-Type': 'application/json'
    }

    #assigning user input into values string here...
    values = values %(myspeech)

    #converting string to json object
    data = json.dumps(values).encode("utf-8")
    values = values.encode("utf-8")
    request = requests.post(url,data=values,headers=headers)

    #fetching response as json object
    response = request.json()

    if response['result'] == None:
        print('[BOT]: idk yet')
        return "Anlamadim"
    else:
        print('[BOT]: ' + response['result']['messages'][0]['text'])
        return response['result']['messages'][0]['text']