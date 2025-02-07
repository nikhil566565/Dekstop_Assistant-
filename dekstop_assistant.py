import psutil
import requests
import speech_recognition as sr 
import os
import pyttsx3 
import pywhatkit 
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init() 
voices = engine.getProperty('voices')
if voices:  # Ensure voices are available
    engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(text):
    engine.say(text)   
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}\n")
            return query.lower()
        except sr.UnknownValueError :
            print("Sorry, I didn't catch that. Please repeat.")
        except sr.RequestError:
            print("Network Error...")
        return "None"

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12) :
        speak("Good Morning Sir!")

    elif (hour>=12 and hour<18) :
        speak("Good Afternoon Sir!")

    else :
        speak("Good Evening Sir!")
    speak("I am Sara. How may I help you?")

def getBatteryStatus():
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f"Sir, your system battery is at {percent} percent.")

if (__name__ == "__main__") :
    wishMe()
    while(True) :
        query = takeCommand().lower()

        if ('wikipedia' in query) :
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try :
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia.")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError :
                speak("Sorry, I couldn't find anything on that topic.")
        elif('hello Sara' == query) :
            speak("Hello Sir.. What can i help you.")

        elif('introduction yourself' == query or 'Introduce yourself' == query) :
            speak('Hello! I am sara. I am a desktop assistance created by Nikhil kumawat. I can perform various tasks like opening an app, open websites in browser, search in wikipedia, search a video in youtube, search a query in google and so on. ')
            
        elif('open youtube' in query ):
            webbrowser.open("youtube.com")

        elif('open google' in query) :
            webbrowser.open("google.com")

        elif('time' in query) :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif('vs code' in query or 'visual studio code' in query ) :
            os.system("code")
            
        elif('open chrome' in query) :
            chrome_open = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_open)

        elif('cmd' in query or 'command prompt' in query) :
            os.system("start cmd")
        
        elif ('play music' in query or 'song' in query):
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'battery' in query:
            getBatteryStatus()
        if ('search in browser' in query):
            try:
                query = query.replace('search in browser', '')
                webbrowser.open(f'https://www.google.com/search?q={query}')
            except:
                speak('Could not perform the task. Please try again.')    
            
        elif 'thank you sara' in query or 'thank u sara' in query:
            speak('You are welcome sir !')
            break
        elif ('exit sara' in query):
            speak("Goodbye. ")
            break