import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib # used for sending emails through gmail only. Not through any other mailing platforms.
import re
import psutil # pip install psutil      Used for getting data such as RAM, CPU speed, etc.
import random


MASTER = "YOUR_NAME_HERE"
ASSISSTANTNAME = "JARVIS" # Or anything of your wish


# Starting the pyttsx3 module
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # To change to female voice, run this instead:   engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hourNow = int(datetime.datetime.now().hour)
    if hourNow > 0 and hourNow < 12:
        print("Good Morning, ", MASTER)
        speak("Good Morning!" + MASTER)


    elif hourNow >= 12 and hourNow < 15:
        print("Good Afternoon, ", MASTER)
        speak("Good Afternoon!" + MASTER)


    else:
        print("Good Evening, ", MASTER)
        speak("Good Evening!" + MASTER)




def receiveCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 350
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print("Say that again, please")
        speak("Could you please say that again " + MASTER + "?")
        return "None"
        query = receiveCommand()
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    to = str(to) + "@gmail.com"
    server.login('your-gmail-id@gmail.com', 'your-password')
    server.sendmail("your-gmail-id@gmail.com", to, content)
    server.close()

#Actual Code begins...
if __name__ == "__main__":
    print("Initializing " + ASSISSTANTNAME + "..." + " Version 2.19")
    speak("Initializing " + ASSISSTANTNAME + "..." + " Version 2.19")
    
    # Giving that cool effect
    satellite_no = random.randint(1, 2000) # Choosing a random number
    print("Connecting to secure satellite no.", str(satellite_no))
    speak("Establishing secure connection with satellite number" + str(satellite_no))
    print("Loading datasets...")
    speak("Loading datasets...")
    speak("Running through start-up process...") # Sounds cool when you run it, right?
    wishMe()
    print("I am " + ASSISSTANTNAME + " 2.1.9. How may I help you " + MASTER + "?")
    speak("I am " + ASSISSTANTNAME + " 2 point 1 9. How may I help you " + MASTER + "?")

    while True:
        query = receiveCommand()


        if 'wikipedia' in query.lower():
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)

        elif 'open youtube' in query.lower():
            print("Opening YouTube...")
            speak("Opening YouTube...")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.youtube.com')

        elif 'open google' in query.lower():
            print("Opening Google...")
            speak("Opening Google...")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.google.com')

        elif 'open facebook' in query.lower():
            print("Opening Facebook...")
            speak("Opening Facebook...")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.facebook.com')

        elif 'exit' in query.lower():
            print("Exitting " + ASSISSTANTNAME + "...")
            speak("Always at your service, " + MASTER + "!")
            speak("Exitting " + ASSISSTANTNAME + "Version 2 point 1 9.")
            break

        elif 'the time' in query.lower():
            currentTime = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is {currentTime}")
            speak(f"The time is {currentTime}")
        
        elif 'system statistics' in query.lower() or 'device analysis' in query.lower():
            cpu_speed = psutil.cpu_percent()
            ram = psutil.virtual_memory()[2]
            print("Device running at ", str(cpu_speed), " percent cpu speed and ", ram, " percent RAM.")
            analysis = "Device is running at", str(int(cpu_speed)), "percent cpu speed and consuming", str(ram), "percent of RAM.", str(100.00 - int(ram)), "percentage of RAM available out of the total 4 gigabytes of RAM" # Replace 4 GB with the GB of RAM you have
            speak(analysis)
        
        elif 'cpu speed' in query.lower() or 'the speed' in query.lower():
            cpu_speed = psutil.cpu_percent()
            print("Device running at ", str(cpu_speed), " percent cpu speed")
            cpu = "Device is running at", str(int(cpu_speed)), "percent cpu speed"
            speak(cpu)
        
        elif 'the ram' in query.lower() or 'ram is' in query.lower():
            ram = psutil.virtual_memory()[2]
            print("Device consuming ", str(ram), " percent RAM.")
            ram_reply = "Device is consuming", str(int(ram)), "percent of RAM.", str(100.00 - int(ram)), "percentage of RAM is available out of the total 4 gigabytesm of RAM"
            speak(ram_reply)

        elif 'an email' in query.lower():
            try:
                speak("What should be the content for the email?")
                content = receiveCommand()
                speak("Whom do you want to send this email to?")
                to = receiveCommand()
                receiverEmail = re.sub('[,!;\'+" "]', '', to)
                speak("Do you confirm this email address" + MASTER + "?")
                print("Do you confirm this email address: ", receiverEmail.lower())
                emailAddressConfirmation = receiveCommand()
                if 'yes' in emailAddressConfirmation:
                    sendEmail(receiverEmail.lower(), content)
                    speak("Email sent successfully! Quitting the Email send function...")

                else:
                    print("Quitting email send function...")
                    speak("Okay,", MASTER, "I am quitting the Email send function.")

            except Exception as e:
                print(e)

