import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            print("Sorry, I did not understand that.")
            return "none"
        except sr.RequestError:
            speak("Sorry, the speech service is down.")
            print("Sorry, the speech service is down.")
            return "none"

# Function to tell the current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {current_time}")
    print(f"The time is {current_time}")

# Function to search Wikipedia
def search_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)
    print("According to Wikipedia")
    print(results)

# Function to greet the user
def greeting():
    speak("Hello, how can I help you today?")
    print("Hello, how can I help you today?")

if __name__ == "__main__":
    greeting()
    while True:
        query = recognize_speech()

        if 'time' in query:
            tell_time()
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            search_wikipedia(query)
        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't help with that.")
            print("Sorry, I can't help with that.")
