from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image,ImageTk
import pyttsx3
import os

root=Tk()
root.title("Text to speach")
root.geometry("950x470+300+100")
root.title("Text to speach")
root.configure(background="#5D6D7E")

engine=pyttsx3.init()

def speak():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if (speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()      
                
def download():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

    if(text):
        if (speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()      
    
top_frame=Frame(root,bg="white",width=1000,height=135)
top_frame.place(x=0,y=0)
photo=ImageTk.PhotoImage(Image.open("mic1.jpg"))
myimage=Label(top_frame,image=photo,background="#305065",bd=0)
myimage.place(x=250,y=30)
Label(top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=425,y=50)

text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=170,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=185)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=185)

gender_combobox=ttk.Combobox(root,values=["Male","Female"],font="arial 14",state="r",width=10)
gender_combobox.place(x=550,y=240)
gender_combobox.set('Male')

speed_combobox=ttk.Combobox(root,values=["Fast","Normal","Slow"],font="arial 14",state="r",width=10)
speed_combobox.place(x=730,y=240)
speed_combobox.set('Normal')

btn_speak=Button(root,text="Speak",width=13,font="arial 14 bold",bg="#F8C471",command=speak)   
btn_speak.place(x=550,y=325)

btn_save=Button(root,text="download",width=13,font="arial 14 bold",bg="#82E0AA",command=download)
btn_save.place(x=730,y=325)

root.mainloop()