###########################################################################--------------login database validity-----------
def login():
    email=emailval.get()
    password=passwordval.get()

    try:
        if(email=='' or password==""):
            messagebox.showerror("Error", "All Fields Are Required", parent=loginroot)

        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Vikhil', database='saionlinebanking1')
                mycursor = con.cursor()
                mycursor.execute('select * from data1 where Email=%s and Password=%s',(email,password))
                row = mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=loginroot)
                else:
                    messagebox.showinfo("Success","Welcome,You Have Successfully Signed in",parent=loginroot)
                    loginroot.destroy()
                    import banking
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=loginroot)
    except Exception as es:
        messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=loginroot)

#################################################################################################
from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import Toplevel
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
import time
import datetime
loginroot=Tk()
loginroot.title('Login')
#root.config(bg='gold2')
loginroot.geometry('1510x770+0+10')
#root.iconbitmap('bank.icon')  #To set the icon
loginroot.resizable(False,False)    #To set the window size default

#########################################################---------------Left label------------
leftlabel=Label(loginroot,bg='#08A3D2',bd=0)
leftlabel.place(x=0,y=0,relheight=1,width=600)

#######################################################---------------Right label-----------
rightlabel=Label(loginroot,bg='#f05b63',bd=0)
rightlabel.place(x=600,y=0,relheight=1,relwidth=1)

#######################################################---------------Login frame-----------
loginframe=Frame(loginroot,bg='white',bd=0)
loginframe.place(x=250,y=100,height=500,width=800)

########################################################--------------signin labels------------
titlelabel = Label(loginframe, text='SIGNIN HERE', font=('times new roman',25,'bold'),bg='white', fg='#08A3D2')
titlelabel.place(x=250, y=50)

emaillabel = Label(loginframe, text='EMAIL ADDRESS', font=('times new roman',18,'bold'),bg='white', fg='gray')
emaillabel.place(x=250, y=150)

passwordlabel = Label(loginframe, text='PASSWORD', font=('times new roman',18,'bold'),bg='white', fg='gray')
passwordlabel.place(x=250, y=250)

########################################################-----------signin entry--------------
emailval=StringVar()
passwordval=StringVar()

emailentry = Entry(loginframe, font=('times new roman',15),bg='light gray',textvariable=emailval)
emailentry.place(x=250, y=180,width=350,height=35)

passwordentry = Entry(loginframe, font=('times new roman',15),bg='light gray',textvariable=passwordval)
passwordentry.place(x=250, y=280,width=350,height=35)

loginbutton = Button(loginframe, text='Signin',cursor='hand2', font=('times new roman',20,'bold'),bg='green',bd=0,fg='white',command=login)
loginbutton.place(x=250, y=360,width=180,height=40)

#####################################################-----Register Button----------------
def registerwindow():
    loginroot.destroy()
    import reg
Registernewaccountbutton = Button(loginframe,cursor='hand2', text='Register new Account?', font=('times new roman',14),bg='white',bd=0,fg='green',command=registerwindow)
Registernewaccountbutton.place(x=250, y=320)


#####################################################-----Forget password Button----------------

forgetpassword = Button(loginframe,cursor='hand2', text='Forget Password', font=('times new roman',14),bg='white',bd=0,fg='red')
forgetpassword.place(x=450, y=320)

#######################################################---------------left frame-----------
leftframe=Frame(loginroot,bd=0,bg='black')
leftframe.place(x=90,y=120,height=450,width=350)

framelabel = Label(leftframe, text='The Security Of Your ', font=('times new roman',18,'italic bold'),bg='black', fg='white')
framelabel.place(x=80, y=150)

framelabel = Label(leftframe, text='Account is Our First Priority ', font=('times new roman',18,'italic bold'),bg='black', fg='white')
framelabel.place(x=40, y=180)

################################################################################
loginroot.mainloop()


