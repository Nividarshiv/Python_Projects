from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk,Image
import os
from stegano import lsb

root=Tk()
root.geometry("700x500+300+80")
root.resizable(False,False)
root.title("Steganography - Hide a Secrete Text Message in an Image")
root.configure(background="#2f4155")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        type="Select Image File",
                                        filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt")))
    img=ImageTk.PhotoImage(Image.open(filename))
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    text1.delete(1.0,END)

def saveimage():
    secret.save("hidden.png")

def Hidedata():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)
    text1.delete(1.0,END)

def ShowData():
    try:
       secret_message=lsb.reveal(filename)
       text1.delete(1.0,END)
       text1.insert(END,secret_message)
    except:
       messagebox.showinfo("Data","This Picture has no secret data")

photo=ImageTk.PhotoImage(Image.open("logo.png"))
myimage=Label(image=photo,background="#4a4a4a")
myimage.place(x=10,y=0)

Label(root,text="CYBER SCIENCE",bg="#2d4155",fg="white",font="araial 25 bold").place(x=100,y=20)

frame1=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
frame1.place(x=10,y=80)
lbl=Label(frame1,bg="black")
lbl.place(x=40,y=10)

frame2=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
frame2.place(x=350,y=80)
text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE)
text1.place(x=0,y=0,width=320,height=295)
scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)
Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=saveimage).place(x=180,y=30)
Label(frame3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)
Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hidedata).place(x=20,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=ShowData).place(x=180,y=30)
Label(frame4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)


root.mainloop()