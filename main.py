import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
speak("Welcome to Google Speech Recognition! I'm Python buddy. Before we begin, what's your name? ")
user=input("Welcome to Google Speech Recognition! I'm Python Buddy. Before we begin, what's your name? ")

print(f"Welcome {user}!! Let's get started!")
speak(f"Welcome {user}!! Let's get started!")
print("Speak now!!")
while True:
    try:
        with sr.Microphone() as source:
            print("Listening....")
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio=r.listen(source)
            text=r.recognize_google(audio)
            text_lower=text.lower().strip()
            print(f"{user}: {text_lower}")
            if text_lower=="exit":
                print("Python Buddy: Thank you for using our application!!")
                speak("Thank you for using our application!!")
                print("Python Buddy: Powered with Python, Created by Gopi!")
                speak("Powered with Python, Created by Gopi!")
                break
            speak(text_lower)
    except sr.UnknownValueError:
        print("Python Buddy: Sorry, I cannot understand")
        speak("Sorry, I cannot understand")
    except sr.RequestError:
        print("Python Buddy: Could not request results from Google Speech Recognition service")
        speak("Could not request results from Google Speech Recognition service")
    except sr.WaitTimeoutError:
        print("Python Buddy: I don't hear anything! :(")
        speak("I don't hear anything! :(")
