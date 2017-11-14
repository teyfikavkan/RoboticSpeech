import speech_recognition as sr

# talkSpeechToText() function gets our voice by using computer microphone and
# it returns what we are saying to computer as a string
def talkSpeechToText():
    r=sr.Recognizer()


    with sr.Microphone() as source:


        print("Say Something")
        audio=r.listen(source)
        '''r.energy_threshold = 500 '''
        '''Increasing the energy_threshold seemed to resolve this issue for me.
         It appears that under quiet conditions, my microphone returns an energy
          level of 300~ forcing the recorder to record indefinitely.'''
        try:
            print("Google thinks you said: \n"+r.recognize_google(audio,language="tr-TR"))
        except:
            pass
        return r.recognize_google(audio,language="tr-TR")
