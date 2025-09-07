import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import json
import time
import pywhatkit
import keyboard as k
import random as rd
import requests
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Personal details
Mail_Dictionary = "F:\\Programs\\Python\\Project Friday\\Friday 2.0\\tomail.txt"

wb = webbrowser.get("windows-default")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning ")
    elif hour < 18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")

def Activation():
    activation_voice_lines = {
        1: "Rise and shine! Let's tackle the day!",
        2: "What can I assist you with today?",
        3: "Your friendly AI assistant reporting for duty!",
        4: "Time to unleash the power of technology!",
        5: "I'm online and ready. What's the plan?",
    }
    quote = rd.randrange(1, 6)
    print(activation_voice_lines[quote])
    speak(activation_voice_lines[quote])

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 250
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception:
        print("I couldn't recognize, please say that again...")
        speak("I couldn't recognize, please say that again")
        return "None"
    return query.lower()

def sendEmail(to, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to, content)
        server.quit()
        return True
    except Exception as e:
        print("Email Error:", e)
        return False

def get_weather(city="Hyderabad"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()
    print("Weather API Response:", res)
    if res.get("cod") != 200:
        speak("Couldn't fetch weather. Please check API key or city name.")
        return
    weather = res["weather"][0]["description"]
    temp = res["main"]["temp"]
    speak(f"The weather in {city} is {weather} with a temperature of {temp} degree Celsius.")

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWSAPI_API_KEY}"
    res = requests.get(url).json()
    articles = res.get("articles", [])
    if not articles:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_API_KEY}"
        res = requests.get(url).json()
        articles = res.get("articles", [])
    if not articles:
        speak("No news found.")
        return
    speak("Here are the top headlines:")
    for i, article in enumerate(articles[:5], 1):
        speak(f"{i}. {article['title']}")

def Whatsapp():
    speak("Enter phone number with country code, e.g., +91...")
    number = input("Phone number: ")
    speak("What should I say?")
    msg = takeCommand()
    speak("In how many minutes?")
    minutes = int(input("Minutes: "))
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute + minutes
    pywhatkit.sendwhatmsg(number, msg, hour, minute)
    speak("Message scheduled.")

# -------------------- MAIN --------------------
if __name__ == "__main__":
    wishMe()
    Activation()
    while True:
        query = takeCommand()

        if "search in google" in query:
            speak("Searching in Google...")
            query = query.replace("search in google", "")
            pywhatkit.search(query)

        elif "in wikipedia" in query:
            speak("Searching in Wikipedia...")
            query = query.replace("search", "").replace("in wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "in youtube" in query:
            speak("Searching in YouTube")
            query = query.replace("search in youtube", "")
            web = "https://www.youtube.com/results?search_query=" + query
            wb.open(web)

        elif "weather" in query:
            city = query.replace("weather in", "").strip()
            if not city:
                city = "Hyderabad"
            get_weather(city)

        elif "news" in query:
            get_news()

        elif "play a song" in query or "play" in query:
            song = query.replace("play", "").strip()
            if song:
                speak(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif "whatsapp message" in query:
            Whatsapp()

        elif "email" in query:
            try:
                tofile = open(Mail_Dictionary, "r")
                data = tofile.read()
                js = json.loads(data)
                print(js.keys())
                speak("To whom do you want to send?")
                n = input("Enter the name: ")
                to = js[n]
                speak("What should I say?")
                content = takeCommand()
                if sendEmail(to, content):
                    speak("Email has been sent successfully!")
                else:
                    speak("Sorry, I couldn't send the email.")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send the email.")

        elif "open visual studio code" in query:
            os.system("Code.exe")

        elif "close visual studio code" in query:
            os.system("TASKKILL /F /im code.exe")

        elif "open chrome" in query:
            os.system("chrome.exe")

        elif "close chrome" in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif "your name" in query or "who are you" in query:
            speak("I am Friday, your AI Voice Assistant.")

        elif "disconnect" in query or "take a break" in query:
            speak("Goodbye Sir, disconnecting...")
            break
