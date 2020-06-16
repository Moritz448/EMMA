import pyttsx3

engine = pyttsx3.init() # object creation
engine.setProperty('rate', 150)# Setting for slower speaking
engine.setProperty('volume',1.0)

voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id) # Setting the voice: 0 is German, 1 is English


def voice_output(sentence):
    engine.say(sentence)
    engine.runAndWait()
    engine.stop()