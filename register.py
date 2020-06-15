try:
    ###################################################-----------Login window--------------------
    def loginwindow():
        root.destroy()
        import proo
    ####################################################------------To clear entries----------------
    def clear():
        firstnameentry.delete(0,END)
        lastnameentry.delete(0, END)
        fathernameentry.delete(0,END)
        emailentry.delete(0, END)
        contactentry.delete(0, END)
        Addressentry.delete(0, END)
        answerentry.delete(0, END)
        passwordentry.delete(0, END)
        confirmpasswordentry.delete(0, END)
        comb_quest.current(0)

    ##########################################################--------------------Sign-Up------------

    def signup():
        def signupdb():
            global firstname,lastname,fathername,email,contact,address,answer,password,confirmpassword
            firstname=firstnameval.get()
            lastname=lastnameval.get()
            fathername=fathernameval.get()
            email=emailval.get()
            contact=contactval.get()
            address=addressval.get()
            answer=answerval.get()
            password=passwordval.get()
            confirmpassword=confirmpasswordval.get()

            try:
                if(firstname == "" or lastname == "" or fathername == "" or email == "" or contact == "" or address == "" or comb_quest.get()=='Select' or answer == "" or password == "" or confirmpassword == ""):
                    messagebox.showinfo("Notification", "All Fields Are Required", parent=signuproot)
                elif password!=confirmpassword:
                    messagebox.showerror('Error',"Password & Confirm Password Should Be Same",parent=signuproot)
                elif termsconditionval.get()==0:
                    messagebox.showerror('Error', "Please Agree Our Terms And Conditions", parent=signuproot)
                else:
                    try:
                        con = pymysql.connect(host='localhost', user='root', password='Vikhil',database='saionlinebanking1')
                        mycursor = con.cursor()
                        mycursor.execute('select * from data1 where Email=%s',email)
                        row=mycursor.fetchone()
                        if row!=None:
                            messagebox.showerror('Error', "User Already Exist,Please Try With Another Email", parent=signuproot)
                        else:
                            strr = 'insert into data1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            mycursor.execute(strr,(firstname,lastname,fathername,email,contact,address,comb_quest.get(),answer,password))
                            con.commit()
                            mycursor.close()
                            messagebox.showinfo('Success', "SignUp Successfull", parent=signuproot)
                            clear()
                            root.destroy()
                            import proo
                    except Exception as es:
                        messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=signuproot)

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=signuproot)


        signuproot = Toplevel(master=DataEntryFrame)
        signuproot.grab_set()  # fix the window
        signuproot.title('Signup')
        signuproot.geometry('1420x550+11+130')
        # dbroot.iconbitmap('bank.icon')
        signuproot.resizable(False, False)

    ##################################################--------------SignUp Frames--------------

        #blanklabelframe = Frame(signuproot, bg='#1b2f4f', relief=GROOVE, borderwidth=5)
        #blanklabelframe.place(x=80, y=40, width=400, height=480)

        signupframe=Frame(signuproot,relief=GROOVE,borderwidth=5)
        signupframe.place(x=80,y=40,width=1100,height=480)

    ######################################################################----------SIgnUp Labesl-----------------
        signuphere=Label(signupframe,text="SIGNUP HERE",font=("times new roman",20,"bold"),fg='green')
        signuphere.place(x=50,y=30)

        firstnamelabel = Label(signupframe, text='First Name', font=('times new roman', 15, 'bold'),fg='gray')
        firstnamelabel.place(x=50, y=100)

        lastnamelabel = Label(signupframe, text='Last Name', font=('times new roman', 15, 'bold'), fg='gray')
        lastnamelabel.place(x=370, y=100)

        fathernamelabel = Label(signupframe, text='Father Name', font=('times new roman', 15, 'bold'), fg='gray')
        fathernamelabel.place(x=690, y=100)

        emaillabel = Label(signupframe, text='Email', font=('times new roman', 15, 'bold'), fg='gray')
        emaillabel.place(x=50, y=170)

        contactlabel = Label(signupframe, text='Contact No', font=('times new roman', 15, 'bold'), fg='gray')
        contactlabel.place(x=370, y=170)

        Addresslabel = Label(signupframe, text='Permanent Address', font=('times new roman', 15, 'bold'), fg='gray')
        Addresslabel.place(x=690, y=170)

        combolabel = Label(signupframe, text='Security Question', font=('times new roman', 15, 'bold'), fg='gray')
        combolabel.place(x=50, y=240)

        global comb_quest

        comb_quest=ttk.Combobox(signupframe,font=("times new roman",13),state='readonly',justify=CENTER)
        comb_quest['values']=('Select','Your Pet Name','Your Best Friend Name','Your GF Name','Your Birth Place')
        comb_quest.place(x=50,y=270,width=250)
        comb_quest.current(0)

        answerlabel = Label(signupframe, text='Answer', font=('times new roman', 15, 'bold'), fg='gray')
        answerlabel.place(x=370, y=240)

        passwordlabel = Label(signupframe, text='Password', font=('times new roman', 15, 'bold'), fg='gray')
        passwordlabel.place(x=50, y=310)

        confirmpasswordlabel = Label(signupframe, text='Confirm Password', font=('times new roman', 15, 'bold'), fg='gray')
        confirmpasswordlabel.place(x=370, y=310)

        #---Terms&Conditions----
        termsconditionval = IntVar()

        global termsconditions

        termsconditions=Checkbutton(signupframe,text="I Agree The Terms & Conditions",variable=termsconditionval,onvalue=1,offvalue=0,font=('times new roman',12))
        termsconditions.place(x=50,y=380)

    #######################################################################--------Signup Entry-------------------
        firstnameval=StringVar()
        lastnameval=StringVar()
        fathernameval=StringVar()
        emailval=StringVar()
        contactval=StringVar()
        addressval=StringVar()
        answerval=StringVar()
        passwordval=StringVar()
        confirmpasswordval=StringVar()

        global firstnameentry,lastnameentry,fathernameentry,emailentry,contactentry,Addressentry,answerentry,passwordentry,confirmpasswordentry

        firstnameentry=Entry(signupframe,bg='light gray',font=("times new roman",15),textvariable=firstnameval)
        firstnameentry.place(x=50,y=130,width=250)

        lastnameentry = Entry(signupframe, bg='light gray', font=("times new roman", 15),textvariable=lastnameval)
        lastnameentry.place(x=370, y=130, width=250)

        fathernameentry = Entry(signupframe, bg='light gray', font=("times new roman", 15), textvariable=fathernameval)
        fathernameentry.place(x=690, y=130, width=250)

        emailentry = Entry(signupframe, bg='light gray', font=("times new roman", 15),textvariable=emailval)
        emailentry.place(x=50, y=200, width=250)

        contactentry = Entry(signupframe, bg='light gray', font=("times new roman", 15),textvariable=contactval)
        contactentry.place(x=370, y=200, width=250)

        Addressentry = Entry(signupframe, bg='light gray', font=("times new roman", 15), textvariable=addressval)
        Addressentry.place(x=690, y=200, width=250)

        answerentry = Entry(signupframe, bg='light gray', font=("times new roman", 15),textvariable=answerval)
        answerentry.place(x=370, y=270, width=250)

        passwordentry = Entry(signupframe, bg='light gray', font=("times new roman", 15),textvariable=passwordval)
        passwordentry.place(x=50, y=340, width=250)

        confirmpasswordentry = Entry(signupframe, bg='light gray', font=("times new roman", 15),textvariable=confirmpasswordval)
        confirmpasswordentry.place(x=370, y=340, width=250)

        signupbutton1 = Button(signupframe, text='Sign Up',bg='green',fg='white',bd=0,cursor='hand2', font=("times new roman", 15),command=signupdb)
        signupbutton1.place(x=260, y=420, width=130)

        signuproot.mainloop()
    ########################################################################-------------- Connection of database-------------

    def Connectdb():
        def submitdb():
            global Username, Password,submitdb
            #host=hostval.get()
            #user=userval.get()
            #password=passwordval.get()

            try:
                con=pymysql.connect(host='localhost',user='root',password='Vikhil')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Notification','Data Is Incorrect Please Try Again')
                return
            try:
                strr='create database saionlinebanking1'
                mycursor.execute(strr)

                strr='use saionlinebanking1'
                mycursor.execute(strr)

                strr = 'create table data1(Firstname varchar(50),Lastname varchar(50),Fathername varchar(30),Email varchar(50),Contact_No varchar(50),Permanent_Address varchar(50),Security_Question varchar(30),Secutiry_Answer varchar(50),Password varchar(40))'
                mycursor.execute(strr)

                #messagebox.showinfo('Notification','DataBase Created And Connected Successfully',parent=dbroot)
            except:
                #strr = 'use onlinebanking1'
                #mycursor.execute(strr)
                messagebox.showinfo('Notification','Now You Are Connected To The Database',parent=dbroot)
            dbroot.destroy()


        dbroot=Toplevel()
        dbroot.config(bg='white')
        dbroot.title('Database Connection')
        dbroot.grab_set()  #fix the window
        dbroot.geometry('470x250+1000+20')
        #dbroot.iconbitmap('bank.icon')
        dbroot.resizable(False,False)

    ############################################################---------- Connection db-labels----------

        HostLabel=Label(dbroot,text='Enter Host',bg='white',font=('times',20,'italic bold'),width=12,anchor='w')
        HostLabel.place(x=10,y=10)

        userLabel=Label(dbroot, text='Enter User',bg='white', font=('times', 20, 'italic bold'),width=12,anchor='w')
        userLabel.place(x=10, y=70)

        passwdLabel = Label(dbroot, text='Enter Password',bg='white', font=('times', 20, 'italic bold'), width=12,anchor='w')
        passwdLabel.place(x=10, y=130)

    ###########################################################----------Connectdb Entry-----------
        hostval=StringVar()
        userval=StringVar()
        passwordval=StringVar()

        hostentry=Entry(dbroot,font=("roman",15,'italic bold'),bd=5,bg='#d2d6d2',textvariable=hostval)
        hostentry.place(x=250,y=10)

        userentry=Entry(dbroot,font=("roman",15,'italic bold'),bd=5,bg='#d2d6d2',textvariable=userval)
        userentry.place(x=250,y=70)

        passwdentry=Entry(dbroot,font=("roman",15,'italic bold'),bd=5,bg='#d2d6d2',textvariable=passwordval)
        passwdentry.place(x=250,y=130)

        #_______________Database connection submit-Button-----
        dbsubmitbutton=Button(dbroot,text='Submit',font=("roman",15,'italic bold'),bg='#49b34b',bd=4,width=20,activebackground='blue',command=submitdb)
        dbsubmitbutton.place(x=150,y=190)

        dbroot.mainloop()



    #################################################################----------packages-------------

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
    root=tk.Tk()
    root.title('Online Banking System')
    #root.config(bg='gold2')
    root.geometry('1510x770+0+10')
    #root.iconbitmap('bank.icon')  #To set the icon
    root.resizable(False,False)    #To set the window size default

    #################################################################-------------------------- 1st-DataFrames----------------

    DataEntryFrame=Frame(root,relief=GROOVE,borderwidth=5)
    DataEntryFrame.place(x=10,y=80,width=500,height=600)

    ###############################################################-------------------------1st Frame-Button------------------

    welcomelabel=Label(DataEntryFrame,text='-----------------Welcome------------------',width=30,font=('arial',22,'italic bold'))
    welcomelabel.pack(side=TOP,expand=True)

    signupbutton=Button(DataEntryFrame,text='1.Sign Up',width=24,font=('arial',12,'italic bold'),bg='green',fg='white',bd=6,command=signup)
    signupbutton.pack(side=TOP,expand=True)

    signinbutton=Button(DataEntryFrame,text='2.Sign In',width=24,font=('arial',12,'italic bold'),activebackground='#d4d9ad',bg='black',fg='white',bd=6,command=loginwindow)
    signinbutton.pack(side=TOP,expand=True)

    exitbutton=Button(DataEntryFrame,text='3 . Exit',width=24,font=('arial',12,'italic bold'),bg='#1b2f4f',fg='white',bd=6,command=exit)
    exitbutton.pack(side=TOP,expand=True)

    ########################################################################### -----------------2nd-Dataframe-------------

    ShowDataFrame=Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
    ShowDataFrame.place(x=500,y=80,width=950,height=600)

    ################################################################ Showdata-Frame-Entry

    style=ttk.Style()
    style.configure('Treeview.Heading',font=('times',20,'italic bold'),foreground='blue')
    style.configure('Treeview',font=('times',15,'italic bold'),bg='cyan',foreground='black')

    scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
    scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)

    DatabaseTable=Treeview(ShowDataFrame,columns=('Id','Username','Password','Account No','Account Holder','Father Name','D-O-B','Gender','Mobile No','Mail Id','Nationality','Address','Added Date','Added Time'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=DatabaseTable.xview)
    scroll_y.config(command=DatabaseTable.yview)

    DatabaseTable.heading('Id',text='Id')
    DatabaseTable.heading('Username',text='Username')
    DatabaseTable.heading('Password',text='Password')
    DatabaseTable.heading('Account No',text='Account No')
    DatabaseTable.heading('Account Holder',text='Account Holder')
    DatabaseTable.heading('Father Name',text='Father Name')
    DatabaseTable.heading('D-O-B',text='D-O-B')
    DatabaseTable.heading('Gender',text='Gender')
    DatabaseTable.heading('Mobile No',text='Mobile No')
    DatabaseTable.heading('Mail Id',text='Mail Id')
    DatabaseTable.heading('Nationality',text='Nationality')
    DatabaseTable.heading('Address',text='Address')
    DatabaseTable.heading('Added Date',text='Added Date')
    DatabaseTable.heading('Added Time',text='Added Time')
    DatabaseTable['show']='headings'

    DatabaseTable.column('Id',width=100)
    DatabaseTable.column('Address',width=300)
    DatabaseTable.column('Mail Id',width=300)

    DatabaseTable.pack(fill=BOTH,expand=1)

    ############################################################## ---------------TimeDate--------------
    try:
        def TimeDate():
            Time_Zone=time.strftime("%H:%M:%S")
            Date_Zone=time.strftime("%d/%m/%y")
            Clock.config(text='Date:'+Date_Zone+'\n'+'Time:'+Time_Zone)
            Clock.after(200,TimeDate)
        Clock=Label(root,font=('times',14,'bold'))
        Clock.place(x=0,y=0)
        TimeDate()

        #################################################################-------------RandomColor-------------

        import random
        colors=['red','pink','blue','yellow','green','gold2','red2']
        def SlideNameColor():
            rcolor=random.choice(colors)
            SliderLabel.config(rcolor=rcolor)
            SliderLabel.after(20,SlideNameColor)

        ###############################################################----------------Name-Scrolling--------------

        def SlideNameScrolling():
            global count,text
            if count>=len(SlideName):
                count=0
                text=''
                SliderLabel.config(text=text)
            else:
                text=text+SlideName[count]
                SliderLabel.config(text=text)
                count+=1
            SliderLabel.after(200,SlideNameScrolling)

        ################################################################-------------- Slide-Name------------

        SlideName='Welcome To Sai Online-Banking System'
        count=0
        text=''

        ################################################################-------------- SlideLabel-------------

        SliderLabel=Label(root,text=SlideName,font=('times',25,'italic bold'),width=35)
        SliderLabel.place(x=300,y=0)
        SlideNameScrolling()
        #SlideNameColor()

    except:
        pass



    ###############################################################---------------- Database Connect-button--------------

    connectbutton=Button(root,text='Connect To DataBase',font=('times',14,'italic bold'),relief=RIDGE,borderwidth=4,bd=6,width=17,bg='#1b2f4f',fg='white',activebackground='#06101f',activeforeground='#dce1e8',command=Connectdb)
    connectbutton.place(x=1250,y=0)

    root.mainloop()

except Exception as es:
    messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=root)
