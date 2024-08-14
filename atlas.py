# import cv2
# import numpy as np
# import keyword as p
# pip install DateTime
import datetime  
import os
import sys
import webbrowser
# from ast import Import
from os import close, system
from winsound import PlaySound
import pywhatkit as kit
 # pip install Pyttsx3
import pyttsx3  
# pip 
import requests
# pip install SpeechRecognition
import speech_recognition as sr 
 # pip install wikipedia
import wikipedia as wi  
from bs4 import BeautifulSoup
from PIL.Image import MAX_IMAGE_PIXELS
# pip install PyQt5
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QDate, Qt, QTime, QTimer
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pyautogui import KEYBOARD_KEYS, click,press

from jaavUI import Ui_jaavUI
import keyword as p

engine = pyttsx3.init('sapi5')

# define class 


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        TaskExecution_Main(self)


# **************************************************************************
# MAKING FUNCTION THAT OUR ASSISTANT CAN SPEAK AND WAIT FOR HEAR OUR QUERY
# **************************************************************************

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
 # this is the ma 
    
def TaskExecution_Main(self):
    # p.press('esc')
    # speak("verification successful")
    # speak("welcome back, sir")
    while True:
        permission = takecommand_Main(self)
        if "activate" in permission:
            TaskExecution(self)
        elif "terminate" in permission:
            sys.exit()
#------------------------------------------------------------------------          

# recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
# recognizer.read('D:/MAJOR PROJECT/trainer/trainer.yml')   #load trained model
# cascadePath = "D:\\MAJOR PROJECT\\haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

# font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


# id = 2 #number of persons you want to Recognize


# names = ['','jinal']  #names, leave first empty bcz counter starts from 0


# cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
# cam.set(3, 640) # set video FrameWidht
# cam.set(4, 480) # set video FrameHeight

# # Define min window size to be recognized as a face
# minW = 0.1*cam.get(3)
# minH = 0.1*cam.get(4)

# # flag = True

# while True:

#     ret, img =cam.read() #read the frames using the above created object

#     converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

#     faces = faceCascade.detectMultiScale( 
#         converted_image,
#         scaleFactor = 1.2,
#         minNeighbors = 5,
#         minSize = (int(minW), int(minH)),
#        )

#     for(x,y,w,h) in faces:

#         cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

#         id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

#         # Check if accuracy is less them 100 ==> "0" is perfect match 
# #         if (accuracy < 100):
# #             id = names[0]
# #             accuracy = "{0}%".format(round(100 - accuracy))
#             TaskExecution_Main(self)
#         else:
#             id = "unknown"
#             accuracy = "  {0}%".format(round(100 - accuracy))
        
#         cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
#         cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
#     cv2.imshow('camera',img) 

#     k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
#     if k == 27:
#         break

# # Do a bit of cleanup
# print("Thanks for using this program, have a good day.")
# cam.release()
# cv2.destroyAllWindows()

#------------------------------------------------------------------------          

# **************************************************************************
# MAKING FUNCTION THAT WHEN ITS RUN HE GREETS FIRST AND THEN RUN OUR QUERY 
# **************************************************************************
            
def wish(self):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir")

    elif hour>=12 and hour<=18:
        speak("good afternoon sir")   

    else:
        speak("good evening sir")
    speak("i'm jaav, please tell me how can i help you")



# **************************************************************************
#            THIS FUNCTION FOR RECEIVEING INFORMATION TO USER
# **************************************************************************
            
def takecommand(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
         playsound('E:\\Python projrct\\atlas\\Sound\\Active.mp3')
         print("listening......")
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
        print("Recorgnizing......")
        query = r.recognize_google(audio, language='en-in')
        print(F"user said: {query}\n")
    except Exception as e:
        speak("say that again please.....")
        return "none"
    return query  


# **************************************************************************
#            THIS FUNCTION FOR RECEIVEING INFORMATION TO USER for firse time
# **************************************************************************

def takecommand_Main(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("listening......")
         r.pause_threshold = 0.5
         audio = r.listen(source)
    try:
        print("Recorgnizing......")
        query = r.recognize_google(audio, language='en-in')
        print(F"user said: {query}\n")
    except Exception as e:
        return "none"
    query = query.lower()
    return query  


# **************************************************************************
# THIS FUNCTION IS USED FOR GIVE A INFORMATION ACCORDINGLY USER'S WANT
# **************************************************************************

def TaskExecution(self):
    # wish(self)
   
    while True:
         self.query = takecommand(self).lower()

# For Playing Music

         if 'play music' in  self.query:
            music_dir = ("E:\\Python projrct\\atlas\\Music\\music.mp3")
            os.startfile(os.path.join(music_dir))
            break
          
# For Turn off the Assistant   
          
         elif 'take rest' in self.query:
             hour = int(datetime.datetime.now().hour)
             if hour>=0 and hour<=12:
                 speak("ok sir , have a nice day")
                 

             elif hour>=12 and hour<=18:
                 speak("ok sir , have a nice day")
                 
                 
  
             else:
                 speak("ok sir, good night")
                 speak("just let me know if you need any help")
                    
             break 
                 


# For Geting Information about Assistant  


         elif 'who are you'  in  self.query:
             speak("hello i'm one off the most handsome A I in the world")
             speak(", just kidding")
             speak("hello i'm jaav,  an AI assistant") 
             speak("i'm best example of artificial intelligence ")
             speak("my main work is to assist my boss")
             speak("i was made by some I T's students")
             break
             
# For Send Message on whatsapp
   
         elif 'send a message on whatsapp' in self.query or 'send message' in self.query:
            speak("Tell me the name of the person!")
            n = takecommand(self).lower()
            if 'aditya' in n:
                 speak("Tell me the message!")
                 msg = takecommand(self)
                 speak("ok sir, sending whatsapp message !")
                 kit.sendwhatmsg_instantly("+917623967294",msg)
                #  p.press('enter')
                 click(x=1840, y=968)
                 speak("message was sent")
                 break

            elif 'aj' in n:
               speak("Tell me the message!")
               msg = takecommand(self)
               speak("ok sir, sending whatsapp message !")
               kit.sendwhatmsg_instantly("+917435073614",msg)
            #    p.press('enter')
               click(x=1840, y=968)
               speak("message was sent")
               break
            
            elif 'varun' in n:

               speak("Tell me the message!")
               msg = takecommand()
               speak("ok sir, sending whatsapp message !")
               kit.sendwhatmsg_instantly("+918347647311",msg)
            #    p.press('enter')
               
               click(x=1840, y=968)
               speak("message was sent")
               break
             
# For Geting Current time  
             
         elif 'time' in  self.query:
              strftime = datetime.datetime.now().strftime("%H %M")
              print(strftime)
              speak(F"sir,the time is{strftime}")
              break
          
# for geting information about the person through wikipidia   

         elif 'wikipedia' in self.query:
             speak("searching ', ' wikipedia' ")
             self.query =  self.query.replace("wikipedia", "")
             result = wi.summary(self.query,sentences = 2)
             print(result)
             speak(" according to', ' wikipedia ")
             speak(result)
             break
            
# for break the program 
         elif 'code red'  in self.query:
             hour = int(datetime.datetime.now().hour)
             if hour>=0 and hour<=12:
                 speak("ok sir , have a nice day")
                 sys.exit()

             elif hour>=12 and hour<=18:
                 speak("ok sir , have a nice day")
                 sys.exit()   
  
             else:
                 speak("ok sir, good night")
                 speak("just let me know if you need any help")
                 sys.exit()    
                 
         elif 'open youtube' in self.query:
             webbrowser.open("https://www.youtube.com/")
             speak("opening youtube")
             break
             
# for open google

         elif 'open google' in  self.query:
             webbrowser.open("www.google.com")
             speak("opening google")
             break

# for open google meet

         elif 'open meet' in  self.query:
             webbrowser.open("https://meet.google.com/")
             speak("ok sir,opening google meet")
             break
# for open stack overflow

         elif 'stack overflow' in  self.query:
             webbrowser.open("https://stackoverflow.com/")
             speak("opening stack over")
             break

# for creators information

         elif 'creators' in  self.query:
             speak("jinal shah , ADITYA , A J , VARUN ,ajay")
             break
         
         elif 'jinal shah' in  self.query:
            speak("he is one of my creator")
            speak("currently he is pursuing BCA from sabarmati university")
            break

         elif 'aditya' in  self.query:
            speak("he is one of my creator")
            speak("currently he is pursuing BCA from sabarmati university")
            break
        
         elif 'aj' in  self.query:
            speak("he is one of my creator")
            speak("currently he is pursuing BCA from sabarmati university")
            break

         elif 'varun' in  self.query:
            speak("he is one of my creator")
            speak("currently he is pursuing BCA from sabarmati university")
            break

# for open whatsapp in browser
         elif 'open whatsapp' in  self.query:
             webbrowser.open("https://web.whatsapp.com/")
             speak("opening whatsapp web")
             break
             
# for open visual studio code

         elif 'open code' in   self.query:
             os.startfile("C:\\Users\jinal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
             speak("opening visual studio code")
             break

# for open google crome
             
         elif 'open chrome' in   self.query:
             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
             speak("opening google chrome")
             break

# for open MY PC

         elif 'open my pc' in   self.query:
             os.startfile("C:\\Users\\USER\\Desktop\\This PC - Shortcut.lnk")
             speak("opening my pc")  
             break           

# for close crome

         elif 'close my browser' in  self.query:
            os.system("taskkill /im chrome.exe /f")
            break

# for open command promt

         elif 'open terminal' in  self.query:
             os.startfile("C:\\Users\\jinal\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
             speak("opening terminal")
             break

# for open my computer

         elif 'open this pc' in  self.query:
             speak("opening this pc")
             os.startfile("C:\\Users\\jinal\Desktop\\This PC - Shortcut.lnk")
             break

# for knowing current temprature

         elif 'temperature' in  self.query:
            search = "temprature in ahmedabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(F"current {search} is {temp}")
            break
        
         elif 'hello' in self.query or 'hey jaav' in self.query:
             speak("hello, what is your name?") 
             n = takecommand(self)
             speak("nice to meet you"+ n)
             speak("tell me how can i help you?")

         elif 'how are you' in self.query:
             speak("i am fine , what about you?")
             n = takecommand(self)
             if 'fine' in n:
                speak("nice to here about that")
             else:
                 speak("i can help you with your mood by play music for you")
                 n  = takecommand(self)
                 if 'yeah' in n:
                     music_dir = ("E:\\Python projrct\\atlas\\Music\\music2.mp3")
                     os.startfile(os.path.join(music_dir))
                     break

                 elif 'no' in n:
                         speak("then tell me what can i do for you?")
                         takecommand(self).lower

# for close music

         elif 'close music' in  self.query:
             os.system("taskkill /im  Microsoft.Media.Player.exe /f")
             break

# for close terminal

         elif 'close terminal' in  self.query:
            os.system("taskkill /im  cmd.exe /f")    
            break
            
# open my task manager
         elif 'open my manager' in  self.query:
             os.startfile("C:\\Windows\\System32\\Taskmgr.exe")
             speak("opening task manager")
             break

#**************************************************************************
#             THIS CODE IS FOR CONNECT BACK-END TO FRONT-END
#**************************************************************************


startExecution = MainThread()
             
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jaavUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
# **************************************************************************
#                    THIS CODE IS CONNECT TWO PYTHON FILE
# **************************************************************************
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:\\Python projrct\\atlas\\Gif\\aed11d6975231b91c8e992c02b8376da.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.start(1000)   
        startExecution.start()



app = QApplication(sys.argv)
atlas = Main()
atlas.show()
exit(app.exec_())
                     
             
             
             
             
             
             
             
             
        
# def TaskExecutionMain():
#     while True:
#         permission = takecommand()
#         if "wake up" in permission:
#             TaskExecution()
#         elif "goodbye" in permission:
#             sys.exit()
            
# TaskExecutionMain()
