# -*- coding: utf-8 -*-
from gtts import gTTS
import os,SpeechConfig

# recordTextToSpeech(myresponse) function takes the argument "myresponse" and
# it records bot's response as a mp3 type and it returns the name of tape.
def recordTextToSpeech(myresponse,counter):
    try :
        mywords = (myresponse)

        tts = gTTS(text=mywords, lang='tr')
        path = str(SpeechConfig.Tape_Record_Folder + str(counter) + ".mp3")
        tts.save(path)
        if counter >=2:
            os.remove(str(SpeechConfig.Tape_Record_Folder+ str(counter-2)+".mp3"))
    except Exception:
        path=SpeechConfig.TextToSpeechTempAudio1
    finally:
        return path


# calling deleteAllRecords() function before our infinite loop to avoid overflow...
def deleteAllRecords():
    dirPath = "records"
    fileList = os.listdir(dirPath)
    for FileName in fileList:
        os.remove(dirPath + "/" + FileName)

if __name__ == '__main__':
    print("Calling External Text To Speech Main")
