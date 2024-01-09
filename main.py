import speech_recognition as sr
import pyttsx3
from googlesearch import search
import os
import webbrowser
import datetime

current_time = datetime.datetime.now().strftime("%H:%M:%S")
time = current_time.split(":")


def speak(op):
    speak = pyttsx3.init()
    voices = speak.getProperty('voices')
    speak.setProperty( 'voice', voices[1].id)
    speak.say(op)
    speak.runAndWait()


## AI Logic:
def greeting():
    if int(time[0])<=12:
        speak("Good Morning sir")
    elif int(time[0])>12 and int(time[0])<17:
        speak("Good Afternoon sir")
    elif int(time[0])>17 and int(time[0])<=24:
        speak("Good evening sir")
    else:
        speak("Time fetching error")
        ImportError

##Introduction
def intro():
    speak("I am Nucleus, How can i help you")

while True:

    r = sr.Recognizer()
    def recognition():
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            speak(text)

        #TODO: Logic and command:
            if text == "open command":
                os.system("cmd")

            elif "current time" in text:
                print(f"Current time is {current_time}")

            # elif "info about" in text:
            #     ##Info about the topic

            elif text == "open notepad":
                os.system("notepad")

            elif text== "open browser":
                os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

            elif 'youtube' in text:
                webbrowser.open_new_tab('youtube.com')

            elif 'get web' in text:
                topic= text.replace('get web' , '').strip()
                for i in search(topic):
                    f = open('google search result.md', 'a')
                    f.write(i + "\n")
                    f.close()

            elif 'search on YouTube' in text:
                topic = text.replace('search on YouTube', '').strip()
                youtube_url = f'https://www.youtube.com/results?search_query={topic}'
                webbrowser.open_new_tab(youtube_url)

            elif 'exit' in text:
                RuntimeError

            else:
                functions = ["Current time" , "open browser" , "open youtube", "open notepad" , "get web" , "search on youtube"]
                speak("Functions are:")
                for i in functions:
                    print(i)

        except:
            speak("Recongnization failed!")
            print("Recongization failed!")
            # except Exception as e:
            #     print(e)

    recognition()
    # speak("Hello World")
                
    # os.system("cmd")

    