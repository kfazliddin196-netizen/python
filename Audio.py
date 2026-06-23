import pyttsx3
e=pyttsx3.init()
while True:
 a=input('so\'z')
 def s():
    e.say(a)
    e.runAndWait()
 s()
