import pyttsx3
import datetime
import pyaudio
import wave
import speech_recognition as sr
import wikipedia,webbrowser
import os,random as rd
import time

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning Sir')
    elif 12 <= hour <= 18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')
    speak("I am Jarvis, your assistant sir. How may I assist you?")

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    
def youtube_search(query):
    search_url = f"https://www.youtube.com/search?q={query}"
    webbrowser.open(search_url)

   
def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return frames


def save_audio(frames, filename="output.wav"):
    audio = pyaudio.PyAudio()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

def inputcommand():
    frames = record_audio()
    save_audio(frames)
    
    r = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        print('Listening sir .......  ')
        audio = r.record(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'USER SAID: {query}')
    except Exception as e:
        print('Error occurred ', e)
        print('Say that again sir')
        query = ""

    return query.lower()

if __name__ == "__main__":
    wishme()
    while True:
        query = inputcommand()
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)
        
        elif 'search on google' in query:
            google_search(query)
            
        elif 'search on youtube' in query:
            youtube_search(query)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open chat gpt' in query:
            webbrowser.open('openai.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            path = "C:\\music\\favourite"
            songs = os.listdir(path)

            if len(songs) == 0:
                print("No songs found in the specified directory.")
            else:
                # Choose a random song
                num = rd.randint(0, len(songs) - 1)

                # Play the selected song
                song_path = os.path.join(path, songs[num])
                os.startfile(song_path)
                

                print(f"Now playing: {songs[0]}")
                time.sleep(5)

        elif 'the time' in query:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {current_time}")
            
        elif 'the date' in query:
            curr_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {curr_date}")
        elif 'open code' in query:
            code_path="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
        elif 'close' in query:
            speak('Closing Sir')
            speak('Thank You ')
            exit()
            
        else:
            print('nothing to do...')
        
