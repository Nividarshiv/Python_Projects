from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mydb import Database

db=Database("employeedetail")

root=Tk()
root.title("Employee Management System")
root.geometry("1600x700+0+50")
root.config(bg="#2c3e50")

name=StringVar()
age=StringVar()
doj=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()

entry_frame=Frame(root,bg="#535c68")
entry_frame.pack(side=TOP,fill=X)    

title=Label(entry_frame,text="Employee Management System",font=("Calibri",25,"bold"),bg="#535c68",fg="yellow")
title.grid(row=0,columnspan=2,padx=50,pady=20)   

lname=Label(entry_frame,text="Name",font=("Calibri",15),bg="#535c68",fg="yellow")
lname.grid(row=1,column=0,padx=10,pady=10,sticky="w")      
tname=Entry(entry_frame,textvariable=name,font=("Calibri",15),width=30)
tname.grid(row=1,column=1,padx=10,pady=10)

lage=Label(entry_frame,text="Age",font=("Calibri",15),bg="#535c68",fg="yellow")
lage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
tage=Entry(entry_frame,textvariable=age,font=("Calibri",15),width=30)
tage.grid(row=1,column=3,padx=10,pady=10)

ldoj=Label(entry_frame,text="Date of Join",font=("Calibri",15),bg="#535c68",fg="yellow")
ldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
tdoj=Entry(entry_frame,textvariable=doj,font=("Calibri",15),width=30)
tdoj.grid(row=2,column=1,padx=10,pady=10)

lemail=Label(entry_frame,text="Email",font=("Calibri",15),bg="#535c68",fg="yellow")
lemail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
temail=Entry(entry_frame,textvariable=email,font=("Calibri",15),width=30)
temail.grid(row=2,column=3,padx=10,pady=10)

lgender=Label(entry_frame,text="Gender",font=("Calibri",15),bg="#535c68",fg="yellow")
lgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entry_frame,font=("Calibri,15"),width=26,textvariable=gender,state="readonly")   
comboGender["values"]=("Male","Female")   #add values to the Combobox
comboGender.grid(row=3,column=1)

lcontact=Label(entry_frame,text="Contact",font=("Calibri",15),bg="#535c68",fg="yellow")
lcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
tcontact=Entry(entry_frame,textvariable=contact,font=("Calibri",15),width=30)
tcontact.grid(row=3,column=3,padx=10,pady=10)

laddress=Label(entry_frame,text="Address",font=("Calibri",15),bg="#535c68",fg="yellow")
laddress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
taddress=Text(entry_frame,width=95,height=3,font=("Calibri",15))
taddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getdata(event):
    select_row=tv.focus() 
    data=tv.item(select_row)   
    global rowvalue
    rowvalue=data['values']    
    name.set(rowvalue[1])
    age.set(rowvalue[2])
    doj.set(rowvalue[3])
    email.set(rowvalue[4])
    gender.set(rowvalue[5])
    contact.set(rowvalue[6])  
    taddress.delete(1.0,END)
    taddress.insert(END,rowvalue[7])

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if tname.get()=="" or tage.get()=="" or tdoj.get()=="" or temail.get()=="" or tcontact.get()=="" or comboGender.get()=="" or taddress.get(1.0,END)=="":
        messagebox.showerror("Error","Please fill all details")
        return
    db.insert(tname.get(),tage.get(),tdoj.get(),temail.get(),comboGender.get(),tcontact.get(),taddress.get(1.0,END))
    messagebox.showinfo("Success","Record Inserted")
    clear_employee()
    displayall()

def update_employee():
    if tname.get()=="" or tage.get()=="" or tdoj.get()=="" or temail.get()=="" or tcontact.get()=="" or comboGender.get()=="" or taddress.get(1.0,END)=="":
        messagebox.showerror("Error","Please fill all details")
        return
    db.update(tname.get(),tage.get(),tdoj.get(),temail.get(),comboGender.get(),tcontact.get(),taddress.get(1.0,END),rowvalue[0])
    messagebox.showinfo("Success","Record Updated")
    clear_employee()
    displayall()

def delete_employee():
    db.remove(rowvalue[0])
    clear_employee()
    displayall()

def clear_employee():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    taddress.delete(1.0,END)

bf=Frame(entry_frame,bg="#535c68")
bf.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
badd=Button(bf,text="Add_Details",command=add_employee,width=15,font=("Calibri",15,"bold"),bg="green",bd=0,fg="yellow").grid(row=0,column=0,padx=10)
bupdate=Button(bf,text="Update_Details",command=update_employee,width=15,font=("Calibri",15,"bold"),bg="blue",bd=0,fg="yellow").grid(row=0,column=1,padx=10)
bdelete=Button(bf,text="Delete_Details",command=delete_employee,width=15,font=("Calibri",15,"bold"),bg="red",bd=0,fg="yellow").grid(row=0,column=2,padx=10)
bclear=Button(bf,text="clear_All",command=clear_employee,width=15,font=("Calibri",15,"bold"),bg="#16a085",bd=0,fg="yellow").grid(row=0,column=3,padx=10)

tf=Frame(root,bg="white")
tf.place(x=0,y=420,width=1600,height=250)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',15),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',15))

tv=ttk.Treeview(tf,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=3)
tv.heading("2",text="NAME")
tv.column("2",width=10)
tv.heading("3",text="AGE")
tv.column("3",width=3)
tv.heading("4",text="DATEOFJOINING")
tv.column("4",width=5)
tv.heading("5",text="EMAIL")
tv.column("5",width=10)
tv.heading("6",text="GENDER")
tv.column("6",width=5)
tv.heading("7",text="CONTACT")
tv.column("7",width=7)
tv.heading("8",text="ADDRESS")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getdata)  #Adding click row event
tv.pack(fill=X)

displayall()
root.mainloop()