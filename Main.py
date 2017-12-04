import toSpeech, PlayTape, BotConnection, SpeechToText

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


while True == True:
    go()
    cnt = cnt + 1
