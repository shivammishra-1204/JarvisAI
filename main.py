import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime


# TEXT TO SPEECH
def say(text):
    engine = pyttsx3.init('sapi5')

    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)

    engine.say(str(text))
    engine.runAndWait()
    engine.stop()


# SPEECH RECOGNITION
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(
            audio,
            language='en-in'
        )

        print(f"User said: {query}")

        return query

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable")
        return ""


# MAIN PROGRAM
if __name__ == "__main__":

    print("PyCharm")

    say("Hello Shivam Prakash Mishra")

    while True:

        text = takeCommand()

        if text:

            say(text)

        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]

        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in text:
            musicPath = R"D:\movies\Choozay Udta Teer 320 Kbps.mp3"
            os.startfile(musicPath)

        elif "the time" in text:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open camera".lower() in text.lower():
            os.system("start microsoft.windows.camera:")