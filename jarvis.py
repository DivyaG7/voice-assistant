import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes
import cv2
from time import sleep
import subprocess as sp


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 80
engine.setProperty('Rate',newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Hello! This is Helana")

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def wish():
    speak("welcome back mam!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening!")
    else:
        speak("Good Night!")
        
    speak("Helana at your service. How I can help you?")


def command():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "none"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("divyaneela75@gmail.com","9095242941")
    server.sendmail("divyaneela75@gmail.com",to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\ELCOT\Pictures\Screenshots.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at" + usage)
    battery = psutil.sensors_battery
    speak("battery is at")
    speak(battery.percentage)

def jokes():
    speak(pyjokes.get_jokes())

def detect_face():
    cascPath = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    while True:

        ret, frames = video_capture.read()

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
                )

        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x,y), (x+y, y+h), (0, 255, 0), 2)

        
        cv2.imshow('Video', frames)
        speak("detecting face")
        print("Detecting face.......")
        sleep(10)
        pyautogui.press('q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

#def login():
    #speak("login pls...")
    #print("login pls...")
    #if command() == "hi":
        #speak("have a nice day")
    #else:
        #speak("sorry!... you can't access the assistant, password doesn't match ")
        #quit()








if __name__ == "__main__":

    detect_face()
    #login()
    wish()

    said = True
    

    while said:
        query = command().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query or "go offline" in query:
            speak("ok!.... thank you")
            quit()

        elif "wikipedia" in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif "mail to divya" in query:
            try:
                speak("what should I say")
                content = command()
                to = "divyaneela75@gmail.com"
                sendmail(to,content)
                speak("Email send successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "send mail" in query:
            try:
                speak("what should i say")
                content = command()
                to = input()
                sendmail(to,content)
                speak("Email send successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "search in chrome" in query:
            speak("what should I search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = command().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "log out" in query:
            os.system("shutdown - 1")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query or "play music" in query or "song" in query or "music" in query:
            speak("sure... which song you want to hear?")
            song = command().lower()
            if song == "anything":
                songs_dir = r"C:\Users\ELCOT\Music\new"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
            elif song == "vijay song":
                songs_dir = r"C:\Users\ELCOT\Music\new\vijay song"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
            elif song == "mother song":
                songs_dir = r"C:\Users\ELCOT\Music\song\mother song"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
            elif song == "friendship songs":
                songs_dir = r"C:\Users\ELCOT\Music\friendship songs"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))


        elif "remember that" in query:
            speak("what shoul I remember?")
            data = command()
            speak("you said me to remember" + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "open chrome" in query or 'open google' in query:
            speak("here you go to google")
            wb.open("google.com")

        elif "open youtube" in query:
            speak("you go to youtube")
            wb.open("youtube.com")

        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("you said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done")

        elif "cpu" in query:
            cpu()

        elif "jokes" in query:
            jokes()

        elif "open notepad" in query:
            np = r"C:\Users\ELCOT\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories"
            os.startfile(np)

        elif "write notes" in query:
            speak("what should I write?")
            note = command()
            notes = open("np.txt","w")
            notes.write(note)

        elif "read note" in query:
            speak("reading notes")
            file = notes.open("np.txt", "r")
            speak(file.read(5))

        elif "how are you" in query:
            speak("I am fine, Thank you")
            speak("How are you, Mam")

        elif "fine" in query or "good" in query:
            speak("it's good")

        elif "hi helana" in query:
            speak("hi")

        elif "what's your name" in query or "what is your name" in query:
            speak("My name is Helana")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Divi")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Divi")

        elif "morning" in query:
            speak("Good morning mam! Have a nice day")

        elif "online shop" in query:
            speak('From which online shopping website, you want to shop? Amazon, Flipkark, Snapdeal or Naaptol?')
            query = command().lower()
            if 'Amazon' in query:
                wb.open('https://www.amazon.com/')
                time.sleep(10)
            elif 'Flipkart' in query:
                wb.open('https://www.flipkart.com/')
                time.sleep(10)
            elif 'Snapdeal' in query:
                wb.open('https://www.snapdeal.com/')
                time.sleep(10)
            elif 'Naaptol' in query:
                wb.open('https://www.naaptol.com/')
                time.sleep(10)
            else:
                speak('Sorry sir, you have to search in browser as his shopping website is not reachable for me')

        elif 'face' in query and ('detect' in query or 'identifi' in query):
             speak('yes')
             detect_face()

        elif 'camera' in query or 'photo' in query or 'take photo' in query:
             speak('ok')
             open_camera()

        elif ('identif' in query and 'emoji' in query) or ('sentiment' in query and ('analysis' in query or 'identif' in query)):
            speak('please enter only one emoji at a time')
            emoji = input('enter emoji here:')
            if '😃' in emoji or '😄' in emoji or '😁' in emoji or '😊' or '☺' in emoji or '🙂' in emoji or '😇' in emoji or '😀' in emoji:
                speak('Happy')
                print('Happy')
            elif '😝' in emoji or '😆' in emoji or '😂' in emoji or '🤣' in emoji:
                speak('Laughing')
                print('Laughing')
            elif '😡' in emoji or '😠' in emoji or '🤬' in emoji:
                speak('Angry')
                print('Angry')
            elif '🤫' in emoji:
                speak('Keep quite')
                print('Keep quite')
            elif '😷' in emoji:
                speak('Face with mask')
                print('Face with mask')
            elif '🥳' in emoji:
                speak('party')
                print('party')
            elif '😥' in emoji or '😓' in emoji or '😢' in emoji or '😰' in emoji or '☹' in emoji or '🙁' in emoji or '😟' in emoji or '😔' in emoji or '😞' in emoji or '😔' in emoji:
                speak('Sad')
                print('Sad')
            elif '😭' in emoji:
                speak('Crying')
                print('Crying')
            elif '😋' in emoji:
                speak('Tasty')
                print('Tasty')
            elif '🤨' in emoji:
                speak('Doubt')
                print('Doubt')
            elif '😴' in emoji:
                speak('Sleeping')
                print('Sleeping')
            elif '🥱' in emoji:
                speak('Feeling sleepy')
                print('Feeling sleepy')
            elif '😍' in emoji or '🥰' in emoji or '😘' in emoji:
                speak('Lovely')
                print('Lovely')
            elif '😱' in emoji:
                speak('Horrible')
                print('Horrible')
            elif '🎂' in emoji:
                speak('Cake')
                print('Cake')
            elif '🥺' in emoji:
                speak('Emotional')
                print('Emotional')
            else:
                speak("I  don't know about this emoji")
                print("I  don't know about this emoji")
            
             
            
        




            
    








