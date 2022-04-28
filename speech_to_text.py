# Speech to Text AI
# You saw my code about converting Text to Speech But do you know we can convert speech to text in Python too. '
# This awesome code will show you how to do it. Check the code below:
# Convert Speech to Text
#pip install SpeechRecognition
import speech_recognition as sr
def SpeechToText():
Ai = sr.Recognizer()
    with sr.Microphone() as source:
        listening = Ai.listen(source, phrase_time_limit = 6)  
    try:
        command = Ai.recognize_google(listening).lower()
        print("You said: " + command)
        
    except sr.UnknownValueError:
        print("Sorry Can't understand, Try again")
        SpeechToText()
