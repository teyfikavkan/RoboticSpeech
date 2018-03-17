# -*- coding: utf-8 -*-
import speech_recognition as sr
import pyaudio
import sys
# talkSpeechToText() function gets our voice by using computer microphone and
# it returns what we are saying to computer as a string
def talkSpeechToText():
    r=sr.Recognizer()

    pa = pyaudio.PyAudio()
    pa_info = pa.get_default_input_device_info()
    pa_info_string = pa_info['index']  # Returns json objects...
    pa_info_index= int(pa_info_string)

    with sr.Microphone(pa_info_index) as source:


        print("Say Something")
        r.adjust_for_ambient_noise(source,pa_info_index)
        audio=r.listen(source)

        '''r.energy_threshold = 500 '''
        '''Increasing the energy_threshold seemed to resolve this issue for me.
         It appears that under quiet conditions, my microphone returns an energy
          level of 300~ forcing the recorder to record indefinitely.'''
        try:
            print("Google thinks you said: \n"+r.recognize_google(audio,language="tr-TR"))
        except sr.UnknownValueError:
            print("tam anlayamadım")
            print(sr.UnknownValueError)
        return r.recognize_google(audio,language="tr-TR")
