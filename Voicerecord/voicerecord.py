from tkinter import *
from PIL import ImageTk,Image
import sounddevice as sound
from scipy.io.wavfile import write
import time
from tkinter import messagebox

root=Tk()
root.geometry("400x625+400+80")
root.resizable(False,False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

def record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,samplerate=freq,channels=2)
    
    try:
        temp=int(duration.get())
    except:
        print("Please enter the right value")  

    while(temp>0):
        root.update()
        time.sleep(1)
        temp-=1

        if temp==0:
            messagebox.showinfo("Count down","Time's up")
        Label(text=f"{str(temp)}",font="arial 35",width=4,background="#4a4a4a").place(x=135,y=540)

    sound.wait()
    write("recording.wav",freq,recording)
            

photo=ImageTk.PhotoImage(Image.open("voicerecoed.jpg"))
myimage=Label(image=photo,background="#4a4a4a")
myimage.pack(padx=5,pady=45)

Label(text="Voice Recorder",font="arial 30 bold",background="#4a4a4a",fg="white").pack()

duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 30",width=15).pack(pady=10)
Label(text="Enter time in seconds",font="arial 15",background="#4a4a4a",fg="white").pack()

record=Button(root,text="Record",font="arial 20",bg="#111111",fg="white",border=0,command=record).pack(pady=10)
root.mainloop()

'''
Install
pip install sounddevice
pip install scipy'''