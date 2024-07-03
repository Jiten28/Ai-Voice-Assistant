import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search 
import json
import time
import pywhatkit #automation
import pyautogui #Screenshot
import keyboard as k #automatic press keyboard keys
import random as rd 

#Personal Details
gmail = "samplemail@gmail.com"
password = "password"

#Folder Paths#Add your tomail.txt path
screenshot_file = "D:\\Coding\\Python\\AI Voice Assistant\\Screenshot\\"            #Add your Screeshot folder path
Mail_Dictionary = "F:\\Programs\\Python\\Project Friday\\Friday 2.0\\tomail.txt"    #Add your tomail.txt path      

wb = webbrowser.get('windows-default')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('Rate',100)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ")   

    else:
        speak("Good Evening ")  


def Activation(): 
    activation_voice_lines = {
    1: "Rise and shine, human! Let's tackle the day!",
    2: "Good morning, sunshine! What's the plan?",
    3: "Greetings, Earthling! What can I assist you with today?",
    4: "Beep boop! Your friendly AI assistant reporting for duty!",
    5: "Hey there, [User's Name]! Ready to conquer the digital realm?",    #face recognition for user name identification
    6: "Time to unleash the power of technology! How can I serve you?",
    7: "It's AI o'clock! How can I assist?",
    8: "I'm online and ready to rock your socks off! So, What's the plan?",
    9: "Welcome back, [User's Name]! Let's make magic happen!",
    10: "Beep beep! I'm here to make your day easier than pie! What can I help you with?",
    11: "I've got your back, digitally speaking! How can I make your life smoother?",
    12: "Ready to be your digital sidekick! What's the mission?",
    13: "Consider me your genie in the cloud! What's your wish?",
    }   
    quote = rd.randrange(0,13)
    # Accessing a specific phrase
    print(activation_voice_lines[quote])  # Output: "Friday is online and geared up for some chat with a dash of fun!"
    speak(activation_voice_lines[quote])


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

    except Exception as e:   
        print("I couldn't recognize please say that again ...")
        speak("I couldn't recognize please say that again")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail, password)
    server.sendmail(gmail, to, content)
    server.quit()


def OpenApps():
    speak("Opening the Application")
    
    if 'code' in query:
        os.system("Code.exe")
    
    elif 'chrome' in query:
        os.system("chrome.exe")
        
    speak("Applications has been Opened Successfully")


def CloseApps():
    speak("Closing the Application")
    
    if 'code' in query:
        os.system("TASKILL /F /im code.exe")
    
    elif 'chrome' in query:
        os.system("TASKILL /F /im chrome.exe")
        
    speak("Applications has been closed Successfully")


def screenshot():             #In order to use this feature, you need to create a folder to save screenshots taken by the AI
    speak("Ok Sir, What Should I Name this File ")
    print("Ok Sir, What Should I Name this File ?")
    ss = takeCommand()
    ssname = ss+'.png'
    path = screenshot_file+ssname   #enter your screenshot folder path
    scst = pyautogui.screenshot()
    scst.save(path)
    speak("Screenshots has been saved successfully with name {}".format(ssname))
    os.startfile(path)  #enter your screenshot folder path
    speak("Here is your Screenshot")


# def YoutubeAuto():
#     print("Youtube Automation Protocol has been started !")
#     speak("Youtube Automation Protocol has been started")
#     com = takeCommand()

#     if 'pause' in com:
#         k.press('space bar')

#     elif 'forward' or 'skip' in com:
#         k.press('l')

#     elif 'rewind' or 'back' in com:
#         k.press('j')

#     elif 'mute' in com:
#         k.press('m')

#     elif 'reset' or 'restart' in com:
#         k.press('0')

#     elif 'full screen' in com:
#         k.press('f')

#     elif 'theater mode' in com:
#         k.press('t')

#     elif 'mini screen' in com:
#         k.press('i')

#     speak('Done Sir')


def ChromeAuto():
    print("Chrome Automation Protocol has been started !")
    speak("Chrome Automation Protocol has been started")
    cam = takeCommand()

    if 'close this tab' in cam:
        k.press_and_release('ctrl + w')

    elif 'open new tab' in cam:
        k.press_and_release('ctrl + t')

    elif 'history' in cam:
        k.press_and_release('ctrl + h')

    elif 'download' in cam:
        k.press_and_release('ctrl + j')

    elif 'reload' or 'refresh' in cam:
        k.press_and_release('ctrl + r')

    speak('Done Sir')


def Whatsapp():
    speak("Tell me the Name of the Person ")
    print("Tell me the Name of the Person :")
    Pname = takeCommand()

    if 'Name' in Pname:
        speak("What should I say ")
        print("What should I say :")
        msg = takeCommand()
        speak("Tell me the Time to send your message ")
        speak("Time in hour")
        hour = int(takeCommand()) 
        speak("Time in minutes")
        min = int(takeCommand()) 
        pywhatkit.sendwhatmsg('+911234567890',msg,hour,min,20)
        time.sleep(10)
        k.press_and_release("enter")
        speak("Whatsapp Message has been Sent to <Name> successfully")

    else:
        speak("Enter his/her Phone Number")
        num = input("Enter his/her Phone Number : +91 ")
        Pnum = '+91'+ num
        speak("What should I say ")
        print("What should I say :")
        msg = takeCommand()
        speak("Tell me the Time to send your message ")
        speak("Time in hour")
        hour = int(takeCommand()) 
        speak("Time in minutes")
        min = int(takeCommand()) 
        pywhatkit.sendwhatmsg(Pnum,msg,hour,min,20)  #here 20 is the wait time
        time.sleep(10)
        k.press_and_release("enter")
        speak("Whatsapp Message has been Sent successfully")


if __name__ == "__main__":
    wishMe()
    Activation()
    while True:
        # query = input("Enter your query: ")
        query = takeCommand().lower()
        wb = webbrowser.get('windows-default')

        if 'in google' in query:
            speak('Searching in google...')
            query = query.replace("friday","")
            query = query.replace("search","")
            query = query.replace("in google","")
            for link in search(query, num_results=3, lang='en' ): 
                wb.open(link)

        elif 'in wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("friday","")
            query = query.replace("search","")
            query = query.replace("in wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'yourself' in query:
            speak('I am Friday your personal AI Voice Assistant.')
            speak('I have been created by Master Jiten Kumar.')
            speak('I can search anything from anywhere, I can send Email to anyone')
            speak('I can play any musics from youtube')
            speak('and also I can open any folder which you have added in my data.')

        elif 'your name' in query:
            speak('I am Friday')

        elif 'who are you' in query:
            speak('I am your personal assistant Friday Sir')

        elif 'in youtube' in query:
            print("Searching in Youtube")
            speak("Searching in Youtube")
            query = query.replace("friday","")
            query = query.replace("search","")            
            query = query.replace("in youtube","")
            web = "https://www.youtube.com/results?search_query=" + query
            wb.open(web)
            speak("Showing the Results")

        elif 'website' in query:
            speak("Which Website do you want to launch")
            query = query.replace("friday","")
            query = query.replace("website","")
            query = query.replace("open","")
            webname = query.replace(" ","")
            web = 'https://www.' + webname + '.com'
            wb.open(web)
            speak("Launching the Website")

        elif 'facebook' in query:
            speak("opening Facebook")
            wb.open('https://www.facebook.com/')

        elif 'instagram' in query:
            speak("opening Facebook")
            wb.open('https://www.instagram.com/')

        elif 'NPTEL' in query:
            speak("opening N P T E L website")
            wb.open('https://swayam.gov.in/nc_details/NPTEL')

        elif 'MRITS' in query:
            speak("opening M R I T S Website")
            wb.open('http://www.mrits.ac.in/')

        elif 'weather' in query:
            speak("Showing Weather Status")
            wb.open('https://weather.com/en-IN/weather/today/l/d7f5a4af529e40b0a82d339e5467e89458e5ad5e2cf0ffdd05c853ed3e98fd38')

        elif 'open mp3 downloader' in query:
            speak("opening MP3 Downloader")
            wb.open('https://mp3download.to/')

        elif 'open telegram' in query:
            speak("opening Telegram")
            wb.open('https://web.telegram.org/')

        elif 'open cbse site' in query:
            speak("opening CBSE site")
            wb.open('https://cbse.nic.in/')

        elif 'open spotify' in query:
            speak("opening Spotify")
            wb.open('https://www.spotify.com/')

        elif 'open discord' in query:
            speak("opening Discord")
            wb.open('https://discord.com/')

        elif 'open visual studio code' in query:
            OpenApps()

        elif 'close visual studio code' in query:
            CloseApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseApps()

        elif 'my location' in query:
            wb.open("https://www.google.com/maps/@17.4316778,78.3500869,15z")
            speak("Jiten Kumar lives in GPRA Quaters which is located in Gachibowli hyderabad telangana ")

        elif 'take screenshot' in query:
            screenshot()

        elif 'pause' in query:
            k.press('space bar')

        elif 'forward' in query:
            k.press('l')

        elif 'back' in query:
            k.press('j')

        elif 'mute' in query:
            k.press('m')

        elif 'restart' in query:
            k.press('0')

        elif 'full screen' in query:
            k.press('f')

        elif 'theater mode' in query:
            k.press('t')

        elif 'mini screen' in query:
            k.press('i') 
            
        # elif 'youtube tools' in query:
        #     YoutubeAuto()

        elif 'close this tab' in query:
            k.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            k.press_and_release('ctrl + t')

        elif 'history' in query:
            k.press_and_release('ctrl + h')

        elif 'download' in query:
            k.press_and_release('ctrl + j')

        elif 'reload' in query:
            k.press_and_release('ctrl + r')

        elif 'chrome tools' in query:
            ChromeAuto()

        elif 'repeat after me' in query:
            speak('ok Sir')
            batt = takeCommand()
            speak(f"You Said : {batt}")

        elif 'play a song' in query:
            speak("of course")
            print("What would you like to hear")
            speak("What would you like to hear")
            SongName = takeCommand()
            pywhatkit.playonyt(SongName)
                
            print("Your Song has been Started Playing, Enjoy Sir.")
            speak("Your Song has been Started Playing, Enjoy Sir")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")    
            speak(f"Sir, the time is {strTime}")

        elif 'whatsapp message' in query:
            Whatsapp()

        elif 'email' in query:
            try:
                tofile = open(Mail_Dictionary, "r")
                data = tofile.read()
                js = json.loads(data)
                Persons = js.keys()
                print(Persons)
                print("To whom do you want to send? ")
                speak("To whom do you want to send? ")
                n = input("Enter the name ")
                value = js[n]
                to = value
                
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent successfully!")
                print("Email has been Sent Successfully!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif 'disconnect' in query:
            print('Good Bye Sir.')
            speak('Good Bye Sir.')
            print("Disconnecting...")
            break

        elif 'take a break' and 'take rest' in query:
            print('OK Sir, You can call me Anytime !')
            speak('OK Sir, You can call me Anytime !')
            print("Disconnecting...")
            break