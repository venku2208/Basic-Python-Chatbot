import pyttsx3
import speech_recognition as sr
import os
import webbrowser as wb
import wikipedia
import datetime
import random
import pyautogui as pg
import psutil

tts = pyttsx3.init()
voice_Id= "HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN-US_ZIRA_11"


def speak(message):
    tts.setProperty('voice',voice_Id)
    tts.setProperty('rate',120)
    tts.say(message)
    tts.runAndWait()
#speak('hi')

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
#time()

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(day)
    speak(month)
    speak(year)
#date()

def greet():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning ")
        print("Good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon ")
        print("Good afternoon")
    elif hour>=18 and hour<24:
        speak("good evening ")
        print("Good Evening")
    else:
        speak("good night")
        quit()
    speak("Wellcome to Jarvis virtual intelligence project. At your service sir.")
#greet()

def user_input():
    read = sr.Recognizer()
    with sr.Microphone() as voice:
        print("Listining...")
        read.pause_threshold = 1
        message = read.listen(voice)

    try:
        print("Recognising...")
        query = read.recognize_google(message,language='eng-in')
        print(query)

    except Exception as e:
        print(e)
        speak("I did not understand, Please say again")
        e.pause_threshold = 1
        return user_input()
    return query

def screenshot():
    img= pg.screenshot()
    img.save('D:/AI python notebook/chatbot/ss.png')

def cpu():
    use = str(psutil.cpu_percent())
    speak('cpu usage'+ use)
    battery = psutil.sensors_battery()
    speak('battery usage')
    speak(battery)

if __name__ == "__main__":

    greet()

    while True:
        query = user_input().lower()

        if 'bye' in query:
            answers = ['Goodbye Sir', 'Jarvis powering off in 3, 2, 1, 0','Bye Sir Have a nice day']
            speak(random.choice(answers))
            quit()

        elif query == 'Jarvis':
            speak("Yes sir, What can i do for you")

        
        
        elif 'your name' in query:
            speak("I am jarvis, At your service sir")
        
        
        elif 'wikipedia' in query:
            speak("Searching....")
            print("Searching...")
            query=query.replace('Search on wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'bot' in query:
            screenshot()
            speak('done')
        elif 'cpu' in query:
            cpu()

        elif 'what do you do' in query:
            lst = ['i can say time','i can say give', 'i can take screenshot', 'i can give informaion like CPU Usuage', 'I can search on Wikipedia']
            speak(lst)
            print(lst)

        elif 'oh great' in query:
            speak('thank you')
        '''elif 'chrome' in query:
            speak("what should i search")
            #print('Searching...')
            #query = query.replace("search on chrome",'')
            #print("please wait")
            path='C:/Program Files/Mozilla Firefox/firefox.exe %s'
            #print('please wait')
            search = user_input().lower()
            wb.get(path).open_new_tab('https://www.'+search+'.com')
'''

