import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui as pg
import psutil

engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("Hi, This is Jarvis")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
#time()

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(year)
    speak(month)
    speak(day)
#date()

def wishing():

    #speak("HI, Buddy")
    #speak("time is")
    #time()
    #speak('date is')
    #date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning buddy")
        print("Good morning buddy")
    elif hour>=12 and hour<18:
        speak("good afternoon buddy")
        print("good afternoon buddy")
    elif hour>=18 and hour<24:
        speak("good evening buddy")
    else:
        speak("good night buddy")
    speak("What can i do for you")
#wishing()

def command():

    read = sr.Recognizer()

    with sr.Microphone() as soc:
        print("lisining...")
        read.pause_threshold=1
        audio = read.listen(soc)

    try:
        print("Recognising...")
        query = read.recognize_google(audio,language='eng-in')
        print(query)

    except Exception as e:
        print(e)
        speak(" Please say again")
        e.pause_threshold = 1
        return command()
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

'''def mail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gvenku22@gmail.com','Settivqm416')
    server.sendmail('gvenku22@gmail.com',to,content)
    server.close()'''


if __name__ == "__main__":
    wishing()

    while True:
        query = command().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query=query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'chrome' in query:
            speak('what should i search')
            path='C:/Program Files/Mozilla Firefox/firefox.exe %s'
            search = command().lower()
            wb.get(path).open_new_tab(search+'.com')
        elif 'bye' in query:
            speak("have a nice day!")
            quit()
        elif 'play' in query:
            songsdir='c:/Music'
            songs = os.listdir(songsdir)
            os.startfile(os.path.join(songsdir,songs[0]))
        elif 'remember that' in query:
            speak("what should i remember")
            data= command()
            speak('you said to remember'+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'bot' in query:
            screenshot()
            speak('done')
        elif 'cpu' in query:
            cpu()
        '''elif 'sendemail' in query:
            try:
                speak("what should i send?")
                content = command()
                to = 'manikanta14038@gmail.com'
                sendmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak('unable to sent the mail')
                
                elif  'do you know that':
            remember = open('data.txt','r')
            speak("you said to remember"+remember.read())
            remember.close()'''
