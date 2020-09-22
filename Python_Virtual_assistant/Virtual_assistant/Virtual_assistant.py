# Description: I used a virtual assistant program created by following the "Build a Vitrual Assistant Using Python" tutorial. I modified it by changing the controls and scripting. 
# https://www.youtube.com/watch?v=AGatX_8gaeM&feature=youtu.be

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS :  (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate’s text-to-speech API. 
# Writes spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout. 
#It features flexible pre-processing and tokenizing, as well as automatic retrieval of supported languages.


#import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import googlesearch
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 
import calendar
import random
import winshell
import webbrowser
import subprocess
import json
import wolframalpha
import pyttsx3
import operator
import time
import clint
import shutil
import tkinter
import ctypes

from twilio.rest import Client
from clint.textui import progress
import win32com.client as wincl
from urllib.request import urlopen

#Set up Pyttsx3 all commands are related to https://pyttsx3.readthedocs.io/en/latest/engine.html
engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)# switch voices: 1= Female, 2=Male

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        assistantname= ("Roscoe 2 point 0")
        speak("I am your Assistant")
        speak(assistantname)
        speak("What should I call you?")
        getName()
        

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        assistantname= ("Roscoe 2 point 0")
        speak("I am your Assistant")
        speak(assistantname)
        speak("What should I call you?")
        getName()
        
    elif hour>=18:
        speak("Good Evening")
        assistantname= ("Roscoe 2 point 0")
        speak("I am your Assistant")
        getName()
        
    
        
def getName():
        r=sr.Recognizer()
        with sr.Microphone() as source:
          try:
              
              while True:
                    print("Listening.....")
                    r.pause_threshold =1 #how many seconds it will wait
                    audio = r.listen(source)
                    print("Recognizing...")     
                    global name 
                    name = r.recognize_google(audio, language ='en-in')
                    print(f"Hey {name}")
                    speak(f"Hey {name}" )
                    return False
                    return name
          except Exception as e: 
            print(e)     
            print("Unable to recognize your voice.")   
            speak("Unable to recognize your voice.")
            getName()
            

            
           
                 
   #Create a pause to allow computer to process commands
   #Create a proper exit

def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
          try:
              
           
            print("Listening.....")
            r.pause_threshold =1 #how many seconds it will wait
            audio = r.listen(source)
            print("Recognizing...")     
            global name 
            name = r.recognize_google(audio, language ='en-in')
            print(f"You said {name}")
            speak(f"You said{name}" )
                    
                    
          except Exception as e: 
            print(e)     
            print("Unable to recognize your voice.")   
            speak("Unable to recognize your voice.")
            return "None"
          return name
             
def getDays():
        now= datetime.datetime.now()
        my_date= datetime.datetime.today()
        weekday = calendar.day_name[my_date.weekday()]
        monthNum = now.month
        dayNum= now.day
        months_names=['January','February','March','April','May','June','July','August','September','October','November','December']
        ordinalNumbers =['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th',
                        '20th','21st','22nd','23rd','24th','25th','26th','27th','28th','28th','30th','31st']
        return   'Today is ' +weekday+' '+months_names[monthNum-1]+ 'the ' + ordinalNumbers[dayNum-1] +'.'
        


def getTime():
     
    now=  datetime.datetime.now().time()
    current_time = now.strftime("%H %M")
    return 'The time is now ', current_time

def wakeWord(name):
     WAKE_WORD= ['hey', 'Roscoe']

     name=name.lower()

     for phrase in WAKE_WORD:
         if phrase in name:
             speak(f'Whats up')
             speak('How may I help you?')
            
# If the wake word is not in the name loop and so it returns False
     


# main fuction#
if __name__ == '__main__': 
    clear = lambda: os.system('cls')
    

    #This function will clean any 
    #command before execution of this python file

    clear()
    greeting()
    speak("how can I help you?")
    

        
    
    while True:
        clear()
        query=takeCommand().lower
        if(wakeWord(name)=="yes"):
                    print ('you said the wake word')
        elif("what is the date" in name):
               print (getDays())
               speak (getDays()) #works
        elif("what is the time"in name):
               print (getTime())
               speak (getTime())

     
    #pause to access new tree

        
        
    

            
exit()
    


   
    

    
            


