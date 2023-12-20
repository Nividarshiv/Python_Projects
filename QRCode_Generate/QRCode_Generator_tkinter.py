from tkinter import *
import qrcode
from PIL import ImageTk,Image

root=Tk()
root.title("QR_GENERATOR")
root.geometry("850x500+300+130")
root.config(bg="#34C2EC")

def generate():
    name=title.get()
    data=entry.get()
    qr=qrcode.make(data)
    qr.save(str(name)+".jpg")

    global img
    img=ImageTk.PhotoImage(Image.open(str(name)+".jpg"))
    
    label=Label(root,image=img)
    label.place(x=450,y=115)

Label(root,text="QRCODE GENERATE",fg="white",bg="#34C2EC",font=("arial",25,"bold","italic")).place(x=250,y=10)

Label(root,text="Title",fg="white",bg="#34C2EC",font=("arial",15,"bold")).place(x=50,y=140)
title=Entry(root,width=13,font=("arial",15,"bold"))
title.place(x=50,y=170,height=35)

Label(root,text="Code to generate QRCode",fg="white",bg="#34C2EC",font=("arial",15,"bold")).place(x=50,y=235)
entry=Entry(width=28,font=("arial",15,"bold"))
entry.place(x=50,y=263,height=35)

Button(root,text="Generate",width=15,height=1,bg="#21618C",fg="white",font=("arial",15,"bold"),bd=0,command=generate).place(x=50,y=330)

root.mainloop()