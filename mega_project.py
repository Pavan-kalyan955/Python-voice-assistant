import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests



recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="0f90e0cdfce949b583903064b168c109"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google"in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook"in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube"in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open stake"in c.lower():
        webbrowser.open("http://stake.bet")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    
    elif "news"in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code ==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])
        
        

if __name__=="__main__":
    speak("initializing jarvis...")
    while True:
        r=sr.Recognizer()
         
        
        print("recognizing...")
        try:
            with sr.Microphone()as source:
               print("Listening...")
               audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Ya")
                #listen for command
                with sr.Microphone()as source:
                     print("jarvis active")
                     audio=r.listen(source)
                     command=r.recognize_google(audio)

                processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))