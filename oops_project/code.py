import pywhatkit
import speech_recognition as sr
import pyttsx3  # python text to speech
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
from tkinter import*
from PIL import ImageTk,Image#To display an image requires the use of Image and ImageTk imported from the Python Pillow (aka PIL) package.
import time
import sounddevice
from scipy.io.wavfile import write
import numpy as np
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
from google_trans_new import google_translator
import winsound#The winsound module provides access to the basic sound-playing machinery provided by Windows platforms
#name_file = open("Alexa", "r")
#name_assistant = name_file.read()

engine = pyttsx3.init('sapi5')#Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft
listener = sr.Recognizer()  # Creating a recognizer who can recognize voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# engine=pyttsx3.init(): The init function is the main function, we have to use this function every time. This function initializes the connection and creates an engine and we can perform all the things on the engine created by the .init() function
# engine.say(text): This function will convert the text to speech (text is the input from the user)
# engine.runAndWait(): This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you.
# engine.setProperty(): This method sets different properties of the model.
# engine.getProperty(): This method is used to get the details with the help of this function.
# voice: If we want the Voices and ascent of the model, we can get it with the help of the voice method.

def talk(said):
    engine.say(said)
    engine.runAndWait()
   


hour = int(datetime.datetime.now().hour)#for current date and time
if hour >= 0 and hour < 12:
    talk("Good Morning Sir !")

elif hour >= 12 and hour < 18:
    talk("Good Afternoon Sir !")

else:
    talk("Good Evening Sir !")
engine.say("i am your alexa")
engine.say("How can I help you")
engine.runAndWait()
def takeinput():
        try:
            with sr.Microphone() as source:
                print("listening...")  # used for indication that our assistant is listening
                listener.adjust_for_ambient_noise(source,duration=1)
                voice = listener.listen(source) 
                 # using microphone as source and then calling speech recognizer to listen to this source and thus we can use functions which speech recognizer uses to convert voice to  text
                command = listener.recognize_google(voice) 
                 # Using google API ,pass the voice to google and it will give text
                command = command.lower()
                if "alexa" in command:  # our output will be printed only if we call alexa
                    command = command.replace("alexa", "")  # To remove word alexa from the printed  command
                    command = command.replace("play", "playing")
                    print(command)
        except:
            pass
        return command





# command=''
class Widget:
    def __init__(self):
        root=Tk()
        root.title('Alexa')
        root.geometry('520x320')
        img=ImageTk.PhotoImage(Image.open('assisstant.png'))#The PhotoImage class is used to display grayscale or true color icons, as well as images in labels.
        #The BitmapImage class is used to display only monochrome (two-color) images in labels.
        panel=Label(root,image=img)# A Label is a Tkinter Widget class, which is used to display text or an image. The label is a widget that the user just views but not interact with.
        panel.pack(side='right',fill='both',expand='yes')#The pack() geometry manager organizes widgets in blocks before placing them in the parent widget
        userText=StringVar()#A variable defined using StringVar() holds a string data where we can set text value and can retrieve it.
        #A normal variable can be used to set the value for any application whenever it is required. However, we can take the user input by creating an instance of the StringVar() object.
        userText.set('Your Alexa')
        #userText='Your Alexa'
        userFrame=LabelFrame(root,text='Alexa',font=('Railways',24,'bold'))#('Railways',24,'bold')
        userFrame.pack(fill='both',expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black', 
        fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
#config is used to access an object's attributes after its initialisation.
        top.pack(side='top', fill='both', expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),
        bg='red', fg='white', command=self.runfun).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 
        'bold'), bg='yellow', fg='black', command=root.destroy).pack(
        fill='x', expand='no')

        root.mainloop()
    
    def runfun(self):
        command = takeinput()
    #print(command)
        if "play" in command or "open" in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)  # To play song on youtube
            #r=Tk()
            #img1=ImageTk.PhotoImage(Image.open('music.png'))
            #panel=Label(r,image=img1)
            #r.mainloop()
          

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M:%p")  # to get the current time in string format
            # %H for hour %M for minute %p for AM or PM
            print(time)
            talk("The time is " + time)
        elif 'search' in command or 'what' in command or 'who' in command:
            if 'who' in command:
                try:
                    person = command.replace('who is', '')
                    info = wikipedia.summary(person, 1)  # 1 denotes the number of lines
                    print(info)
                    talk(info)
                except Exception as e:
                    pass

                command = command.replace("search", "")
                command = command.replace("play", "")
                pywhatkit.search(command)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'wikipedia' in command:  # if wikipedia found in thecommand then this block will be executed
            talk('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)
    # elif "alarm" in command or "reminder" in command:
        elif ("plus" in command )or ("minus" in command )or ("multiply " in command )or ("divide" in command) :
            opr = command.split()[1]
            if opr == 'plus':
                talk(int(command.split()[0]) + int(command.split()[2]))
                print(int(command.split()[0]) + int(command.split()[2]))
            elif opr == 'minus':
                talk(int(command.split()[0]) - int(command.split()[2]))
                print(int(command.split()[0]) - int(command.split()[2]))
            elif opr == 'multiply':
                talk(int(command.split()[0]) * int(command.split()[2]))
                print(int(command.split()[0]) * int(command.split()[2]))

            elif opr == 'divide':
                talk(int(command.split()[0]) / int(command.split()[2]))
                print(int(command.split()[0]) / int(command.split()[2]))

            elif opr == 'power':
                talk(int(command.split()[0]) ** int(command.split()[2]))
                print(int(command.split()[0]) ** int(command.split()[2]))
            else:
                talk("Wrong Operator")

        elif ("open my mail" in command) or ("gmail" in command) or ("check my email" in command):
            search_term = command.split("for")[-1]
            url = "https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            talk("here you can check your gmail")
        elif "record" in command:
            fps=44100
            duration=10
            print('Recording')
            rec=sounddevice.rec(int(duration*fps),samplerate=fps,channels=2)
            sounddevice.wait()
            print('Done')
            write('recording.wav',fps,rec)
        elif "capture" in command:
            webcam=cv2.VideoCapture(0)
            video=VideoWriter('webcam.avi',VideoWriter_fourcc(*'MP42'),25.0,(640,480))
            while True:
                #stream_ok checks webcam is working or not
                stream_ok,frame=webcam.read()
                if stream_ok:
                    cv2.imshow('webcam',frame)
                    video.write(frame)
                if cv2.waitKey(1) &0xFF ==27:
                    break
            cv2.destroyAllWindows()
            webcam.release()
            video.release
        elif "translate" in command:
            with sr.Microphone() as source:
                print('Speak')
                voic = listener.listen(source)
                voice= listener.recognize_google(voic,language='en') 
                #result=listener.recognize_google(voic,language='en')
                engine.say('Please tell the language you want to translate to')
                voi = listener.listen(source) 
                voice1=listener.recognize_google(voi) 
                translator=google_translator()
                text=translator.translate(str(voice1),lang_tgt=str(voice))
                engine.say(str(text))
                engine.runAndWait




        else:
            talk('Sorry! Could you please repeat')


   
        




# Python offers numerous inbuilt libraries to ease our work. Among them pywhatkit is a Python library for sending WhatsApp messages at a certain time, it has several other features too.

# Following are some features of pywhatkit module
# Send WhatsApp messages.
# Play a YouTube video.
# Perform a Google Search.
# Get information on a particular topic.




#if __name__== '__main__':
widget = Widget()
time.sleep(1)
while True:
    command = widget.runfun()
    #respond(command)
engine.runAndWait

    
