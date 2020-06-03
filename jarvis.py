import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    elif hour>=18 and hour<=23:
        speak("Good evening")
    else:
        speak("Good night")
    speak("I m jarviz    please tell how may i help u")

def takeCommand():
    ''' it takes microphone input from user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User  said: {query}\n ")
    except Exception as e:
        print(e)
        print("Say that again...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls('sdfgh','fghj')
    server.sendmail('isha26701@gmail.com', to, content)
    server.close()

if __name__=='__main__':
    speak("isha is a good girl")
    # wishMe()
    if 1:
        query=takeCommand().lower()
        #logics for executing tasks
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir="C:\\Users\\Isha Gupta\\Desktop\\musicp"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"Sir the time is {strtime}")
            print(strtime)
        elif 'open code' in query:
            codepath="C:\\Users\\Isha Gupta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email' in query:
            try:
                speak("What should i say:")
                content=takeCommand()
                to="ishagupta4580@gmail.com"
                sendEmail(to,content)
                speak("Email sent")
            except Exception as e:
                print(e)
                speak("Email not sent")