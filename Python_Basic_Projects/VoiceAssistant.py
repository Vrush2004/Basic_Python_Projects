import pyttsx3
import datetime
import os
import time
import pyjokes
import speech_recognition as sr 

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data.lower()
        except sr.UnknownValueError:
            print("Not Understand")
            return None

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":
    speechtx("Hello Vrush") 

    while True:
        data1 = sptext()

        if data1 is not None and "hey peter" in data1:
            print("hello")
            while True:
                data2 = sptext()

                if "your name" in data2:
                    name = "my name is peter"
                    speechtx(name)
                elif "old are you" in data2:
                    age = "i am two years old"
                    speechtx(age)
                elif "time" in data2:
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    speechtx(current_time)
                elif "joke" in data2:
                    joke = pyjokes.get_joke(language="en", category="neutral")
                    print(joke)
                    speechtx(joke)
                elif "play song" in data2:
                    add = "D:\\python"
                    listsong = os.listdir(add)
                    print(listsong)
                    os.startfile(os.path.join(add, listsong[0]))
                elif "exit" in data2:
                    speechtx("Thank you")
                    exit()

                time.sleep(5)

        else:
            print("Thanks")
            break
