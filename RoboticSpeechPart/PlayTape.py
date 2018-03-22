# -*- coding: utf-8 -*-
from pygame import mixer,time
import os
import pyglet

# playTape(mystring) function takes the argument "tapeName"
# and it plays the tape which has already been recorded.
def playTape(mydoc):
    mixer.init()
    mixer.music.load(mydoc)
    mixer.music.play()
    #print("çaldım")
    while mixer.music.get_busy():
        time.Clock().tick()
        #print("while dayim")
    mixer.music.stop()
    mixer.quit()
    #print("çıkıyorum")
if __name__ == '__main__':
    print("Calling External Play Tape Main")

