import pyttsx3  # library to convert text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random as rd
import pyaudio


engine=pyttsx3.init('sapi5')        #windows api of sapi version 5 which is being initialised on your pc

voice=engine.getProperty('voices')  # fetching the properties
# print(voice)
engine.setProperty('voice',voice[1].id) # setting the property voice of a girl or a boy for your assistant

def speak(audio):           # function to speak
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >0 and hour<12:
        speak('Good Morning Sir')
        
    elif hour >=12 and hour <=18:
        speak('Good Afternoon Sir')
  
    else:
        speak('good evening sir')
    
    speak("I am jarvis, your assistant sir, How may i assist you")

def inputcommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        
        print('Listening sir0 .......  ')
        r.pause_threshold=2 # for how many seconds it should wait for your command
        print('Listening sir1 .......  ')
        
        # audio=r.record(source=source)
        # print('Listening sir2 .......  ')
        try:
            audio = r.listen(source,timeout=2)
        except Exception as e:
            print(f"Error occurred during listening: {e}")

        
    
    try:
        print('recognizing...')
        query=r.recognize_amazon(audio,language='en-in')
        print(f'USER SAID: {query}')
        
    except Exception as e:
        print('error occured ',e)
        print('say that again sir')
    return query
if __name__== "__main__":
    wishme()
    # while True:
    query=inputcommand().lower()
    

    
    if 'wikipedia' in query:
        speak('Searching wikipedia')
        query=query.replace('wikipedia','')
        results=wikipedia.summary(query,sentences=3)
        speak('According to wikipedia')
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open('google.com')
    elif 'open stackoverflow' in query:
        webbrowser.open('stackoverflow.com')
    elif 'play music' in query:
        path='C:\\ music\\favourite'
        songs=os.listdir(path)
        for i in range(len(songs)-1):
            num=rd.randint(0,5)
            os.startfile(os.path.join(path,songs[num]))
    elif 'the time' in query:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"The time is {current_time}")
    elif 'open code' in query:
        code_path="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    else:
        print('nothing to do...')
        
    
    
    