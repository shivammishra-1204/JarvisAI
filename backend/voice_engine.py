
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime


def say(text):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 160)
    engine.setProperty("volume", 1.0)
    engine.say(str(text))
    engine.runAndWait()
    engine.stop()


def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.5
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print("User said:", query)
        return query

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable")
        return ""


def execute_command(query):
    query = query.lower().strip()

    if "open youtube" in query:
        say("Opening YouTube sir")
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "open google" in query:
        say("Opening Google sir")
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "open wikipedia" in query:
        say("Opening Wikipedia sir")
        webbrowser.open("https://www.wikipedia.org")
        return "Opening Wikipedia"

    elif "the time" in query or "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"Sir, the time is {current_time}"
        say(response)
        return response

    elif "open camera" in query:
        say("Opening camera sir")
        os.system("start microsoft.windows.camera:")
        return "Opening Camera"

    else:
        say("Sorry sir, I did not understand that command")
        return "Command not recognized"
