import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import json
from googlesearch import search 
import time
import pywhatkit
import keyboard as k
import random as rd
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Initialize text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('Rate', 100)

wb = webbrowser.get('windows-default')

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greet
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

# Activation line
def Activation(): 
    activation_voice_lines = {
        1: "Rise and shine, human! Let's tackle the day!",
        2: "Sunshine! What's the plan?",
        3: "Earthling! What can I assist you with today?",
        4: "Beep boop! Your friendly AI assistant reporting for duty!",
        5: "Hey there! Ready to conquer the digital realm?",
        6: "Time to unleash the power of technology! How can I serve you?",
        7: "It's AI o'clock! How can I assist?",
        8: "I'm online and ready to rock your socks off! So, What's the plan?",
        9: "Welcome back! Let's make magic happen!",
        10: "Beep beep! I'm here to make your day easier than pie! What can I help you with?",
        11: "I've got your back, digitally speaking! How can I make your life smoother?",
        12: "Ready to be your digital sidekick! What's the mission?",
        13: "Consider me your genie in the cloud! What's your wish?",
    }   
    quote = rd.randrange(1,14)
    print(activation_voice_lines[quote])
    speak(activation_voice_lines[quote])

# Take voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 250
        r.adjust_for_ambient_noise(source, duration = 1)
        r.phrase_threshold = 0.5
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except:
        print("I couldn't recognize. Please say that again.")
        speak("I couldn't recognize. Please say that again.")  
        return "None"
    return query.lower()

CONTACTS_JSON = "contacts.json"
# Send email
def get_email_contact(name):
    contacts = {}
    if os.path.exists(CONTACTS_JSON):
        with open(CONTACTS_JSON, 'r') as f:
            contacts = json.load(f)
    if name in contacts and "email" in contacts[name]:
        return contacts[name]["email"]
    # Ask user if not found
    email = input(f"Enter email for {name}: ")
    if name not in contacts:
        contacts[name] = {}
    contacts[name]["email"] = email
    with open(CONTACTS_JSON, 'w') as f:
        json.dump(contacts, f)
    return email

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to, content)
        server.quit()
        speak("Email sent successfully!")
    except Exception as e:
        print(f"Email Error: {e}")
        speak("Failed to send email. Check your App Password and contact info.")

# WhatsApp
def get_whatsapp_contact(name):
    contacts = {}
    if os.path.exists(CONTACTS_JSON):
        with open(CONTACTS_JSON, 'r') as f:
            contacts = json.load(f)
    if name in contacts and "whatsapp" in contacts[name]:
        return contacts[name]["whatsapp"]
    number = input(f"Enter WhatsApp number for {name} (+91): ")
    if name not in contacts:
        contacts[name] = {}
    contacts[name]["whatsapp"] = "+91" + number
    with open(CONTACTS_JSON, 'w') as f:
        json.dump(contacts, f)
    return contacts[name]["whatsapp"]

def sendWhatsApp():
    speak("Tell me the Name of the Person")
    name = input("Enter contact name: ").title()
    number = get_whatsapp_contact(name)
    speak("What should I say?")
    msg = takeCommand()
    speak("Do you want to send now or later? Type 'now' or 'later'")
    choice = input("Send now or later? (now/later): ").lower()
    if choice == 'now':
        pywhatkit.sendwhatmsg_instantly(number, msg, wait_time=10, tab_close=True)
        speak(f"WhatsApp message sent to {name} instantly")
    else:
        hour = int(input("Hour (24h format): "))
        minute = int(input("Minute: "))
        pywhatkit.sendwhatmsg(number, msg, hour, minute)
        speak(f"WhatsApp message scheduled for {hour}:{minute}")

# Weather
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url).json()
        if response.get("cod") == 200:
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            speak(f"Weather in {city}: {desc}, temperature {temp} degree Celsius")
        else:
            speak("City not found or invalid API key.")
    except Exception:
        speak("Failed to fetch weather. Check your API key.")

# News
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_API_KEY}"
    try:
        response = requests.get(url).json()
        articles = response.get("articles", [])
        if articles:
            speak("Here are the top headlines:")
            for i, art in enumerate(articles[:5], 1):
                print(f"{i}. {art['title']}")
                speak(art['title'])
        else:
            speak("No news found right now.")
    except Exception:
        speak("Failed to fetch news. Check your API key.")

# Main
if __name__ == "__main__":
    wishMe()
    Activation()
    while True:
        query = takeCommand()
        if 'google' in query:
            speak('Searching in Google...')
            query = query.replace("google","").replace("search","").replace("friday","")
            for link in search(query, num_results=3, lang='en'):
                wb.open(link)
                
        elif 'wikipedia' in query:
            query = query.replace("wikipedia","").replace("search","").replace("friday","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'youtube' in query:
            speak("Searching in YouTube...")
            query = query.replace("youtube","").replace("search","").replace("friday","")
            web = "https://www.youtube.com/results?search_query=" + query
            wb.open(web)
            
        elif 'song' in query or 'music' in query:
            speak("What would you like to hear?")
            song = takeCommand()
            pywhatkit.playonyt(song)
            speak("Playing your song.")
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
            
        elif 'send whatsapp' in query:
            sendWhatsApp()
            
        elif 'send email' in query:
            name = input("Enter recipient name: ").title()
            to = get_email_contact(name)
            speak("What should I say?")
            content = takeCommand()
            sendEmail(to, content)
            
        elif 'news' in query:
            get_news()
            
        elif 'weather' in query:
            speak("Tell me the city name:")
            city = takeCommand()
            get_weather(city)
        elif 'disconnect' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye Sir!")
            break