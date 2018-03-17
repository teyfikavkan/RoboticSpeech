# -*- coding: utf-8 -*-
from gtts import gTTS
import os

# recordTextToSpeech(myresponse) function takes the argument "myresponse" and
# it records bot's response as a mp3 type and it returns the name of tape.
def recordTextToSpeech(myresponse,counter):
    mywords = (myresponse)

    tts = gTTS(text=mywords, lang='tr')
    print("tts = gTTS(text=mywords, lang='tr')")
    folder = "records"
    path = str("records/myrecord" + str(counter) + ".mp3")
    print ("path = str")
    tts.save(path)
    print ("tts.save()")
    if counter==0 | counter ==1 | counter ==2:
        pass
    if counter >2:
        os.remove(str("records/myrecord" + str(counter-2)+".mp3"))

    return path


