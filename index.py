import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("I will speak this text! Let's begin")
engine.runAndWait()

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 150)
engine.say("The speed is set to slow")

engine.runAndWait()

with open('file/text.txt', encoding='utf-8') as f:
    for line in f:
        engine.say(line)
        engine.runAndWait()
        print(line , end = '')