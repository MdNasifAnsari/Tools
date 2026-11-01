# Install required package via terminal: --"pip install pyttsx3"--


import pyttsx3

engine = pyttsx3.init()
engine.say("hello")
engine.runAndWait()