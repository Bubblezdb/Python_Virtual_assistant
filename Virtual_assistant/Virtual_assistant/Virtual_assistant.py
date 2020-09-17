# Description: This is a virtual assistant program created by following the "Build a Vitrual Assistant Using Python" tutorial. 
# https://www.youtube.com/watch?v=AGatX_8gaeM&feature=youtu.be

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS :  (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate’s text-to-speech API. 
# Writes spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout. 
#It features flexible pre-processing and tokenizing, as well as automatic retrieval of supported languages.
#pip install spotify
#pip install google

#import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import googlesearch
import spotify
import calendar

# ignore any warning messages
warnings.filterwarnings ('ignore')
# record audio and return it as a string
def recordAudio():

    # record the audio
    r= sr.Recognizer() #Creating a recognizer object

    #Open Microphone and start recording
    with sr.Microphone() as source:
        print('Say Something...')
        audio= r.listen(source)

    #use google's speech recognition
    data= ' '
    try:
     data = r.recognize_google(audio)
     print('You said: '+data)
    except sr.UnknownValueError: #Check for unknown errors
        print('Google Speech Recognition could not understand the audio, please try again')
    except sr.RequestError as e:
        print('Request results from google speech recognition service error'+ e)

    return data

recordAudio()# it works! 

