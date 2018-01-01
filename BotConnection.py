# -*- coding: utf-8 -*-
#coding=utf8
import requests
import json
import os
from HTMLParser import HTMLParser



# calling deleteAllRecords() function before our infinite loop to avoid overflow...
def deleteAllRecords():
    dirPath = "records"
    fileList = os.listdir(dirPath)
    for FileName in fileList:
        os.remove(dirPath + "/" + FileName)
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
    request = requests.post(url, data=values, headers=headers)
    # fetching response as json object AND TURNING IT INTO A STRING HERE !
    response = request.text
    newResponse = response.replace("(", "")
    newResponse = newResponse.replace(")", "")
    newResponse = newResponse.replace(";", "")
    newResponse = newResponse.replace("\\r", "")
    newResponse = newResponse.replace("\\n","")
    newResponse = newResponse.replace("\\", "")
    newResponse = newResponse.encode('utf-8') # bizim şuan elimizdeki data'nın tipi unicode düz string değil yani
                                              # burada yaptığımız şey unicode'u stringe çevirmek ki & ile başlayan
                                              # değerleri silip tekrardan json'a çevirdiğimizde bot saçmalamasın.
    newResponse = newResponse.replace("&ouml","ö")
    newResponse = newResponse.replace("&uuml", "ü")
    newResponse = newResponse.replace("&ccedil","ç")
    newResponse = newResponse.replace("&deg","derece")
    newResponse = newResponse.replace(">","")
    newResponse = newResponse.replace("<", "")
    newResponse = newResponse.replace("center", "")
    newResponse = newResponse.replace("/center", "")
    newResponse = newResponse.replace("/", "")
    newResponse=strip_tags(newResponse) #  html ile bağlantılı ne varsa siliyoruz (ML_stripper)
    newResponse = json.loads(newResponse) # en son tekrar json'a döndürüyoruz ki sadece cevabı almamız kolaylaşsın.
    print(newResponse['answer']) # kontrol amaçlı söylenilen cümleyi biz de okuyalım diye burada bunu yazma ihtiyacı duyduk.
    return newResponse['answer']