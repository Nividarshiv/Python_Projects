from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import googletrans
from googletrans import Translator
from tkinter import messagebox

root=Tk()
root.geometry("1000x400+100+175")
root.resizable(False,False)
root.title("Google Translator")
root.configure(background="white")

def label_change():
    c1=combo1.get()
    c2=combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000,label_change) 

def translator():
    try: 
       text=text1.get(1.0,END)
       t=Translator()
       trans_text=t.translate(text,src=combo1.get(),dest=combo2.get())
       trans_text=trans_text.text

       text2.delete(1.0,END)
       text2.insert(END,trans_text)
    except:
       messagebox.showinfo("Select Language","Choose Languages to translate") 

photo=ImageTk.PhotoImage(Image.open("arrow.jpg"))
myimage=Label(image=photo,width=150)
myimage.place(x=430,y=75)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 10",state="r")
combo1.place(x=140,y=30)
combo1.set("Select Language")
label1=Label(root,font="sego 25 bold",bg="white",width=17,bd=5,relief=GROOVE)
label1.place(x=60,y=60)

combo2=ttk.Combobox(root,values=languageV,font="Roboto 10",state="r")
combo2.place(x=710,y=30)
combo2.set("Select Language")
label2=Label(root,font="sego 25 bold",bg="white",width=17,bd=5,relief=GROOVE)
label2.place(x=600,y=60)

f1=Frame(root,bg="Black",bd=2)
f1.place(x=60,y=110,width=350,height=210)
text1=Text(f1,font='Robote 20',bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=345,height=205)
scrollbar1=Scrollbar(f1)
scrollbar1.pack(side="right",fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

f2=Frame(root,bg="Black",bd=2)
f2.place(x=600,y=110,width=350,height=210)
text2=Text(f2,font='Robote 20',bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=345,height=205)
scrollbar2=Scrollbar(f2)
scrollbar2.pack(side="right",fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate=Button(root,text="Translate",font=("Roboto",15),activebackground="white",bd=1,
                 width=10,height=2,bg="black",fg="white",command=translator)

translate.place(x=445,y=245)
label_change()
root.mainloop()

'''
install
pip install googletrans==3.1.0a0
'''