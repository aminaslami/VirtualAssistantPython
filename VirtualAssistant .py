import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

def listen():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the system's default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Adjust the pause threshold according to your environment
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        query = r.recognize_google(audio)
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech recognition service is currently unavailable.")
        return ""

def speak(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the properties for the generated audio
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Speak the provided text
    engine.say(text)
    engine.runAndWait()

def virtual_assistant():
    speak("Hello! How can I assist you today?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hello there!")
        elif "goodbye" in query:
            speak("Goodbye! Have a great day!")
            break
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif "search" in query:
            speak("What would you like to search for?")
            search_query = listen()
            webbrowser.open_new_tab(f"https://www.google.com/search?q={search_query}")
        elif "open" in query:
            speak("What application would you like to open?")
            app_name = listen()
            os.system(f"start {app_name}.exe")
        else:
            speak("Sorry, I don't have an answer for that.")

# Run the virtual assistant
virtual_assistant()
