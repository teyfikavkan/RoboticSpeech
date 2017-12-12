# -*- coding: utf-8 -*-
import toSpeech, PlayTape, BotConnection, SpeechToText,checkDB,FaceRecognizer

cnt = 0

def go():


    # talkSpeechToText() function gets our voice by using computer microphone and
    # it returns what we are saying to computer as a string
    myspeech = SpeechToText.talkSpeechToText()

    # connectBot(myspeech) function takes the argument "myspeech" and
    # it returns as the response of our talk
    myresponse = BotConnection.connectBot(myspeech)

    # recordTextToSpeech(myresponse) function takes the argument "myresponse" and
    # it records bot's response as a mp3 type and it returns the name of tape.
    tapeName = toSpeech.recordTextToSpeech(myresponse, cnt)

    # playTape(mystring) function takes the argument "tapeName"
    # and it plays the tape which has already been recorded.
    PlayTape.playTape(tapeName)

BotConnection.deleteAllRecords()

entrysentence = unicode("Merhaba  kartınızı okutabilir misiniz", "utf-8")
PlayTape.playTape(toSpeech.recordTextToSpeech(entrysentence, cnt))
id = raw_input("Merhaba ID kartınizi okutabilir misiniz?")
verifiedName = checkDB.copyToTextFile(id);
print(verifiedName)
recognizedName = FaceRecognizer.FaceRecognize()
if (verifiedName == recognizedName):
    print("Erişime izin verildi")
    # sentence=unicode("Hoş geldin ")+unicode(recognizedName)+unicode(" nasıl yardımcı olabilirim")
    # sentence=sentence.encode("utf-8")
    sentence = unicode("Hoş geldin " + recognizedName + " nasıl yardımcı olabilirim", "utf-8")
    PlayTape.playTape(toSpeech.recordTextToSpeech(sentence, cnt+1))

else:
    print("")
    PlayTape.playTape(toSpeech.recordTextToSpeech("kim oldugunu bilemedim", cnt+1))




while True == True:
     go()
     cnt = cnt + 1


#  Silme işi halloldu.
#  No Text To Speech raise exception diye bir exception alıyoruz ama bu seferki daha farklı
#  tutabileceğimiz bir exception tanımlanmamış yani. Bir daha gördüğümüzde ss alıp slack'e atalım.

#  Bot anlamadığı şeylerde çok farklı bir json data döndürebiliyor, ve o kısım çalışmadığında muhtemelen
#  tüm o yaptığımız hard-coding tarafı hataya sebep oluyor onu da halletmemiz lazım.
#  json datayı parse edip türüne(ceyd-a tarafının anlayıp-anlamadığına) göre iki farklı fonksiyona atabiliriz gerekli işlemleri yapmak için



