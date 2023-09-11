import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
# import pyaudio

print("Initializing Keisha")
FRIEND = "Anaelle"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + FRIEND)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + FRIEND)
    else:
        speak("Good Evening" + FRIEND)
    # speak("I am Keisha. How may I help you?")

# this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: # pip install pipwin then, pipwin install pyaudio
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-CA')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        print(str(e))
        query = None
    return query


# main program starts here...
speak("Initializing Keisha...")
wishMe()
query = takeCommand()

# Logic for executing tasks as per the query
if 'wikipedia' in query.lower(): # need to change it to lower case so it can go thru this
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open google' in query.lower():
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'play music' in query.lower():
    songs_dir = "C:/Users/bakam/Music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[1]))
elif "time" in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"{FRIEND} the time is {strTime}")

# https://www.youtube.com/watch?v=4k9CphTdnWE&feature=emb_logo 
