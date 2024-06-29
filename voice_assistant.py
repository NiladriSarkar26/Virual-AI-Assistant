#importing modules
import pyttsx3 #converts text to speech
import speech_recognition as sr 
import webbrowser
import datetime 
import pyjokes
import Joking
import os
import time

def speechToText(): #sptext()
    while True:
        recognizer= sr.Recognizer() #recognizer object is created, and class is recognizer
        with sr.Microphone() as source:
            print("Detecting voice....")
            recognizer.adjust_for_ambient_noise(source) #noise cancellation of source is performed
            audio = recognizer.listen(source)

            try:
                print("Recognizing...")
                data = recognizer. recognize_google(audio)
                print(data) #prints the speech that it recognises
                return data
            except sr.UnknownValueError:
                print("Sorry but I am unable to understand")
        time.sleep(5)

def textToSpeech(x):
    engine = pyttsx3.init() #object engine of class init is initialized
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id) #for male voice
    #engine.setProperty('voice',voices[1].id) #for female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',140) #setting rate of speech
    engine.say(x)
    engine.runAndWait()
#textToSpeech("Hi Niladri!!")

if __name__ == '__main__':
    
    if "orion" in speechToText().lower() :
        #pass 
        textToSpeech("Hello, how may I help you?")

        while True: #running an infinite loop
            data1 = speechToText().lower()

            if "your name" in data1: #detects the phrase "your name" from the input
                name = "my name is orion" 
                textToSpeech(name)

            elif "old are you" in data1:
                age = "I was created by Niladri Sarkar in june 2024 as a part of his Code in Place,Stanford final project"
                textToSpeech(age)

            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I %M %p") #%I %M %p gives us hour, minute and am/pm 
                textToSpeech(time)
            
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'browser' in data1:
                webbrowser.open("https://www.google.co.in/")

            elif 'google' in data1:
                webbrowser.open("https://www.google.co.in/")

            elif 'calender' in data1:
                webbrowser.open("https://www.timeanddate.com/calendar/")

            # elif "joke" in data1:
            #     rand_joke = pyjokes.get_joke(language="en",category="neutral") #randomly selects a joke in english of natural category
            #     print(rand_joke)
            #     textToSpeech(rand_joke)

            elif "joke" in data1:
                rand_joke = Joking.random_joke() #randomly selects a joke in english of natural category
                print(rand_joke)
                textToSpeech(rand_joke)

            elif "dark joke" in data1:
                dark_joke= Joking.DarkJoke()
                print(dark_joke)
                textToSpeech(dark_joke)

            # elif 'play song' in data1:
            #     address = 

            elif "exit" in data1:
                textToSpeech("Thank you. Have a good day!")
                break

            time.sleep(7) #each iteration takes place after 5s
    else:
        print("thanks")




