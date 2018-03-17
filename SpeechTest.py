# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import toSpeech, PlayTape, BotConnection, SpeechToText,checkDB

import speech_recognition as sr
import pyaudio
import sys
# talkSpeechToText() function gets our voice by using computer microphone and
# it returns what we are saying to computer as a string
def talkSpeechToText():
    r=sr.Recognizer()
    #
    # pa = pyaudio.PyAudio()
    # pa_info = pa.get_default_input_device_info()
    # pa_info_string = pa_info['index']  # Returns json objects...
    # pa_info_index= int(pa_info_string)
    with sr.Microphone() as source:


        print("Say Something")

        # r.adjust_for_ambient_noise(source,pa_info_index)
        r.dynamic_energy_threshold = True
        r.pause_threshold = 0.5
        r.dynamic_energy_adjustment_ratio = 1.2

        try:
            audio = r.listen(source)
            print ("dinlendi!")
            recognized_google_audio= None
            recognized_google_audio = r.recognize_google(audio, language="tr-TR")

            '''r.energy_threshold = 500 '''
            '''Increasing the energy_threshold seemed to resolve this issue for me.
             It appears that under quiet conditions, my microphone returns an energy
              level of 300~ forcing the recorder to record indefinitely.'''
            print("Google thinks you said: \n" + recognized_google_audio)
            # print("Google thinks you said: \n" + recognized_google_audio)
            # print("Google thinks you said: \n" + recognized_google_audio)
            # print("Google thinks you said: \n" + recognized_google_audio)
            # print("Google thinks you said: \n" + r.recognize_google(audio, language="tr-TR"))
            # print("Google thinks you said: \n" + r.recognize_google(audio, language="tr-TR"))
            # print("Google thinks you said: \n" + r.recognize_google(audio, language="tr-TR"))
            # print("Google thinks you said: \n" + r.recognize_google(audio, language="tr-TR"))
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.UnknownValueError:
            print("tam anlayamadım")
            print(sr.UnknownValueError)
            talkSpeechToText()
        return recognized_google_audio

from gtts import gTTS
import os

# recordTextToSpeech(myresponse) function takes the argument "myresponse" and
# it records bot's response as a mp3 type and it returns the name of tape.
def recordTextToSpeech(myresponse,counter):
    mywords = (myresponse)
    print(myresponse)

    tts = gTTS(text=mywords, lang='tr', slow= False)
    print("ses kaydedildi!")
    folder = "records"
    path = str("records/myrecord" + str(counter) + ".mp3")
    tts.save(path)
    print("tts.save(path)")

    if counter==0 | counter ==1 | counter ==2:
        pass
    if counter >2:
        os.remove(str("records/myrecord" + str(counter-2)+".mp3"))

    return path
cnt = 0

def go():
    myspeech=talkSpeechToText()
    myresponse = BotConnection.connectBot(myspeech)
    tapeName = recordTextToSpeech(myresponse, cnt)
    PlayTape.playTape(tapeName)
BotConnection.deleteAllRecords()
while True == True:
     go()
     cnt = cnt + 1