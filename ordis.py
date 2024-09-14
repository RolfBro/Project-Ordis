"""This program is developed and written by Ralph and George.
____ is a personal project that is used to further improve our Python skills
while experimenting with Conversational Artificial Intelligence"""

#Libraries--------------------------------------------------------------
import pyttsx3
import speech_recognition as sr
import time

#Variables--------------------------------------------------------------

r = sr.Recognizer()
keywords = [("ordis", 1), ("hey ordis", 1), ] # Wake up words
source = sr.Microphone()

#Functions--------------------------------------------------------------
def Speak(text): #voice settings
    rate = 100
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate+50)
    engine.say(text)
    engine.runAndWait()

def callback(recognizer, audio): #listen for keyword call
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)
        if "ordis" in speech_as_text or "hey ordis":
            Speak("Yes sir?")
            recognize_main()
    except sr.UnknownValueError:
        print("Sorry, please repeat again")

def start_recognizer(): #keyword call function

    print("Waiting for a keyword...")
    r.listen_in_background(source, callback)
    time.sleep(1000000)

def recognize_main(): #main reply function
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say soemthing!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        data.lower()
        print("You said: " + data)
    
        """Greetings"""
        if "how are you" in data:
            Speak("Never been better")
        elif "hello" in data:
            Speak("How may I help you sir?")
        else:
            Speak("Sorry sir, please repeat that")
    except sr.UnknownValueError:
        print("Ordis did not understand your request")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


#Main Program--------------------------------------------------------------
while 1:
    start_recognizer()





