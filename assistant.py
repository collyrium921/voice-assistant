import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os

# this is done to take the voice from the system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# it will speak whatever is passed to this function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# this will wish you according to the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Ma'am. How may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    # Voice recognition
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Sorry, Can you say that again please?")
        return "None"
    return query

# driver code
if __name__ == "__main__":
    wishMe()
    while (True):
        query = takeCommand().lower()

        # Executing queries based on queries
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\KAJAL SINGHAL\\Music\\anyvid'  # Your file directory location of music
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0])) #playing songs from starting

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\KAJAL SINGHAL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # file path for IDE
            os.startfile(codePath)
        
         elif 'exit' in query:
            speak("Okay, Have a nice day ma'am. Thank you!")
            d=False
