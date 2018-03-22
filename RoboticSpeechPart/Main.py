# -*- coding: utf-8 -*-
import TextToSpeech, PlayTape, BotConnection, SpeechToText

cnt=0

def go():

    # talkSpeechToText() function gets our voice by using computer microphone and
    # it returns what we are saying to computer as a string
    myspeech = SpeechToText.startSpeech()

    # connectBot(myspeech) function takes the argument "myspeech" and
    # it returns as the response of our talk
    myresponse = BotConnection.connectBot(myspeech)

    # recordTextToSpeech(myresponse) function takes the argument "myresponse" and
    # it records bot's response as a mp3 type and it returns the name of tape.
    tapeName = TextToSpeech.recordTextToSpeech(myresponse, cnt)

    # playTape(mystring) function takes the argument "tapeName"
    # and it plays the tape which has already been recorded.
    PlayTape.playTape(tapeName)






if __name__ == '__main__':
    TextToSpeech.deleteAllRecords()
    while True == True:


        go()

        cnt=cnt+1


#  Silme işi halloldu.
#  No Text To Speech raise exception diye bir exception alıyoruz ama bu seferki daha farklı
#  tutabileceğimiz bir exception tanımlanmamış yani. Bir daha gördüğümüzde ss alıp slack'e atalım.

#  Bot anlamadığı şeylerde çok farklı bir json data döndürebiliyor, ve o kısım çalışmadığında muhtemelen
#  tüm o yaptığımız hard-coding tarafı hataya sebep oluyor onu da halletmemiz lazım.
#  json datayı parse edip türüne(ceyd-a tarafının anlayıp-anlamadığına) göre iki farklı fonksiyona atabiliriz gerekli işlemleri yapmak için



