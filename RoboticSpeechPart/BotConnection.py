# -*- coding: utf-8 -*-

import requests
import json
import sys

from HTMLParser import HTMLParser


        #print(FileName)


# connectBot(myspeech) function takes the argument "myspeech" and
# it returns a string as the response of our talk
        #dahi.ai
# def connectBot(myspeech):
#     url = "http://api.dahi.ai/dahi/bot/tkn/59f307dfe4b0f7db8924368b"
#     values ="""
#         {
#         'recipientId': 'rec1',
#         'message':
#         {
#           'text': '%s',
#           'type': 'text'
#         }
#       }
#     """
#
#     headers = {
#         'Content-Type': 'application/json'
#     }
#
#     #assigning user input into values string here...
#     values = values %(myspeech)
#
#     #converting string to json object
#     data = json.dumps(values).encode("utf-8")
#     values = values.encode("utf-8")
#     request = requests.post(url,data=values,headers=headers)
#
#     #fetching response as json object
#     response = request.json()
#
#     if response['result'] == None:
#         print('[BOT]: idk yet')
#         return "Anlamadim"
#     else:
#         print('[BOT]: ' + response['result']['messages'][0]['text'])
#         return response['result']['messages'][0]['text']
        #dahi.ai

        #Ceyd-a

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()





# connectBot(myspeech) function takes the argument "myspeech" and
# it returns a string as the response of our talk
def connectBot(myspeech):
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    print(myspeech)
    url = "http://beta.ceyd-a.com/jsonengine.jsp?username=gokhantok&token=57afc561f880eb8bfcbdf61821ea8626&code=%s"
    values = """
          {
            "username": "gokhantok",
            "token": "57afc561f880eb8bfcbdf61821ea8626",

          }
        """
    headers = {
        'Content-Type': 'application/json'
    }

    # assigning user input into values string here...
    url = url %(myspeech)

    # converting string to json object
    data = json.dumps(values).encode("utf-8")
    values = values.encode("utf-8")

    # post atıyoruz burada
    response = requests.post(url, data=values, headers=headers)
    # fetching response as json object AND TURNING IT INTO A STRING HERE !

    response = response.text
    # print(response)

    newResponse = response.encode('utf-8')

    newResponse = newResponse.replace("(", "")
    newResponse = newResponse.replace(")", "")
    newResponse = newResponse.replace(";", "")
    newResponse = newResponse.replace("-","")
    newResponse = newResponse.replace("/","")




    newResponse=strip_tags(newResponse) #  html ile bağlantılı ne varsa siliyoruz (ML_stripper)
    # print newResponse

    try:
        newResponse = json.loads(newResponse) # en son tekrar json'a döndürüyoruz ki sadece cevabı almamız kolaylaşsın.
        CleanResponse = newResponse['answer']
    except Exception:
        CleanResponse = "Anlamadım"

    finally:
        if CleanResponse.__contains__("Sözlük anlamını gösteriyorum"):
            return "Anlamadım"
        else:
            return CleanResponse

if __name__ == '__main__':
    print("Calling External Bot Connection Main")
    connectBot("asdasdsadsad")