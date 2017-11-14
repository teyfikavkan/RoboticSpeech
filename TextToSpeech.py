from gtts import gTTS

# recordTextToSpeech(myresponse) function takes the argument "myresponse" and
# it records bot's response as a mp3 type and it returns the name of tape.
def recordTextToSpeech(myresponse):
    mywords = (myresponse)
    tts = gTTS(text=mywords, lang='tr')
    tts.save("records/myrecord.mp3")
    return "myrecord.mp3"

