from tkinter import *
from tkinter import messagebox
import base64
from PIL import ImageTk, Image

def decrypt():
    password=code.get()
    if password=="1234567157":   
        root2=Toplevel(root)    
        root2.title("DECRYPTION")
        root2.geometry("400x250+650+200")
        root2.configure(bg="#34EC37")

        message=text1.get(1.0,END)     
        decode_message=message.encode("ascii")     
        base64_bytes=base64.b64decode(decode_message)    
        decrypt=base64_bytes.decode("ascii")     
        
        Label(root2,text="DECRYPT",font=("arial",15,"bold"),fg="white",bg="#34EC37").place(x=10,y=3)
        text2=Text(root2,font=("Calibri",15,"bold"),bg="white")
        text2.place(x=10,y=40,width=370,height=170)
        text2.insert(END,decrypt)
    elif password=="":
        messagebox.showerror("Decryption","Enter Password")    
    else:
        messagebox.showerror("Decryption","Invalid Password")

def encrypt(): 
    password=code.get()
    if password=="1234567157":    
        root1=Toplevel(root)     
        root1.title("ENCRYPTION")
        root1.geometry("400x250+650+200")
        root1.configure(bg="#FF5733")

        message=text1.get(1.0,END)    
        encode_message=message.encode("ascii")    
        base64_bytes=base64.b64encode(encode_message)    
        encrypt=base64_bytes.decode("ascii")      

        Label(root1,text="ENCRYPT",font=("arial",15,"bold"),fg="white",bg="#FF5733").place(x=10,y=3)
        text2=Text(root1,font=("Calibri",15,"bold"),bg="white")
        text2.place(x=10,y=40,width=370,height=170)
        text2.insert(END,encrypt)
    elif password=="":
        messagebox.showerror("Encryption","Enter Password")    
    else:
        messagebox.showerror("Encryption","Invalid Password")
        

def main():
    global root
    global code
    global text1

    root=Tk()
    root.geometry("430x425+150+150")
    img = ImageTk.PhotoImage(Image.open("key.jpg"))   
    root.iconphoto(False,img)        
    root.title("SecureMessage")

    Label(text="Enter text for encryption and decryption",fg="black",font=("Calibri",15,"bold")).place(x=15,y=10)
    text1=Text(font=("Calibri",15),bg="white")
    text1.place(x=15,y=50,width=370,height=100)

    Label(text="Enter secrete key for encryption and decryption",fg="black",font=("Calibri",15,"bold")).place(x=15,y=170)
    code=StringVar()
    Entry(textvariable=code,width=37,font=("Calibri",15),show="*").place(x=10,y=210,height=35)   

    def reset():
        code.set("")  
        text1.delete(1.0,END)   

    Button(text="ENCRYPT",height=1,width=15,bg="#FF5733",fg="white",font=("Calibri",15,"bold"),command=encrypt).place(x=10,y=270)
    Button(text="DECRYPT",height=1,width=15,bg="#26CE33",fg="white",font=("Calibri",15,"bold"),command=decrypt).place(x=210,y=270)
    Button(text="RESET",height=1,width=35,bg="blue",fg="white",font=("Calibri",15,"bold"),command=reset).place(x=10,y=335)

    root.mainloop()

main()    
