import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for audio and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Request error; check your internet connection.")
            return None

def main():
    """Main function for the voice assistant."""
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        if command:
            if 'hello' in command:
                speak("Hi there!")
            elif 'how are you' in command:
                speak("I'm good, thank you!")
            elif 'stop' in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()