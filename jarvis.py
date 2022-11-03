

from random import Random
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess as sp




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir! how can i help you")
    elif hour>=12 and hour<18:
        speak("good efternoon sir! how can i help you")
    else:
        speak("good evening sir! how can i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print('recognize...')
        query = r.recognize_google(audio, language='en-in')
        speak(f"user said:{query}\n")
        print(f"user said:{query}\n")


    except Exception as e:
        speak("say that again")
        return "none"
    return query

def openapps():
     
    speak('ok sir')
    if "play music" in query:
        sp.Popen('C:\\Users\\bhask\\AppData\\Local\\Programs\\Resso\\Resso.exe')
    elif "open ms" in query:
        sp.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif "about bhaskar" in query:
        sp.Popen('C:\\Users\\bhask\\OneDrive')




if __name__ =="__main__":
    wishme()
    # speak("")
        
    # while True:
    if 1:
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")    

        elif "play music" in query:
            openapps()
        elif "open ms" in query:
            openapps()
        elif "the date and time" in query:
            strTime = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            speak(f"sir the date and time is :{strTime}")
            print(f"sir the date and time is :{strTime}")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is :{strTime}")
            print(f"sir the time is :{strTime}")
        elif "the date" in query:
            strTime = datetime.datetime.now().strftime("%y-%m-%d")
            speak(f"sir the date is :{strTime}")
            print(f"sir the date is :{strTime}")
        elif "about bhaskar" in query:
            openapps()


        
        

            

           
        
        

 

