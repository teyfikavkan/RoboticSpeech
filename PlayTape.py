# -*- coding: utf-8 -*-
from pygame import mixer,time
import toSpeech

# playTape(mystring) function takes the argument "tapeName"
# and it plays the tape which has already been recorded.
def playTape(mydoc):
    mixer.init()
    print ("mixer.init()")
    mixer.music.load(mydoc)
    print ("mixer.music.load(mydoc)")
    mixer.music.play()
    print ("mixer.music.play()")

    while mixer.music.get_busy():
        time.Clock().tick()
    mixer.music.stop()
    print ("mixer.music.stop()")
    mixer.quit()

