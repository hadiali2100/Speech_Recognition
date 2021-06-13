#Import the required Modules
import speech_recognition as sr
import requests
import pyttsx3 as pt
import os


#Initialize the engine and recognizer
listener = sr.Recognizer()
engine = pt.init()


#Listen to the user
with sr.Microphone() as source:
    print("Listening....")
    engine.say("What is your command")
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()

    #Command for lights
    if 'turn on the lights' or 'switch on the lights' or 'turn on lights' or 'switch on lights' or 'turn the lights on' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=0&state=HIGH&deviceName=BOLT1119308')
        engine.say('turning on the lights')
        print('Turning on the Lights')
    elif 'turn off the lights' or 'switch off the lights' or 'turn off lights' or 'switch off lights' or 'turn the lights off' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=0&state=LOW&deviceName=BOLT1119308')
        engine.say('turning off the lights')
        print('Turning off the Lights')

    #Command for fans
    elif 'turn on the fans' or 'switch on the fans' or 'turn on fans' or 'switch on fans' or 'turn the fans on' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=1&state=HIGH&deviceName=BOLT1119308')
        engine.say('turning on the fans')
        print('Turning on the Fans')
    elif 'turn off the fans' or 'switch off the fans' or 'turn off fans' or 'switch off fans' or 'turn the fans off' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=1&state=LOW&deviceName=BOLT1119308')
        engine.say('turning off the fans')
        print('Turning off the Fans')

    #Command for Doors
    elif 'turn on the doors' or 'switch on the doors' or 'turn on doors' or 'switch on doors' or 'turn the doors on' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=2&state=HIGH&deviceName=BOLT1119308')
        engine.say('turning on the doors')
        print('Turning on the Doors')
    elif 'turn off the doors' or 'switch off the doors' or 'turn off doors' or 'switch off doors' or 'turn the doors off' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=2&state=LOW&deviceName=BOLT1119308')
        engine.say('turning off the doors')
        print('Turning off the Doors')

    #Command for Projector
    elif 'turn on the projector' or 'switch on the projector' or 'turn on projector' or 'switch on projector' or 'turn the projector on' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=3&state=HIGH&deviceName=BOLT1119308')
        engine.say('turning on the projector')
        print('Turning on the Projector')
    elif 'turn off the projector' or 'switch off the projector' or 'turn off projector' or 'switch off projector' or 'turn the projector off' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=3&state=LOW&deviceName=BOLT1119308')
        engine.say('turning off the projector')
        print('Turning off the Projector')

    #Command for Curtains
    elif 'open curtains' or 'slide on curtains' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=4&state=HIGH&deviceName=BOLT1119308')
        engine.say('opening curtains')
        print('Opening the Curtains')
    elif 'close curtains' or '' in command:
        res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=4&state=LOW&deviceName=BOLT1119308')
        engine.say('closing curtains')
        print('Closing the Curtains')

    #Default Output
    else:
        engine.say('invalid command')
