from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import Toplevel
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
import time

bankingroot=Tk()
bankingroot.grab_set()
bankingroot.config(bg='blue2')
bankingroot.geometry('1510x770+0+10')
bankingroot.title('Signed In')
bankingroot.resizable(False, False)

########################################################################## Sign-In-Labels
#DEPOSITAMOUNT5.WITHDRAWAMOUNTFROMBANK6.WITHDRAWWITHOUTD.cINATM7.BALANCEENQUIRY8.DeleteAccount9.LOGOUT

headlabel = Label(bankingroot, text='      Please Choose Your Choice      ', width=30,font=('arial', 22, 'italic bold'), bg='blue2')
headlabel.pack(side=TOP, expand=True)

Depositbutton = Button(bankingroot, text=' 1.Deposit ', width=24, font=('arial', 12, 'italic bold'),bg='powder blue', bd=6)
Depositbutton.pack(side=TOP, expand=True)

withdrawlbutton = Button(bankingroot, text=' 2.Withdrawl ', width=24, font=('arial', 12, 'italic bold'), bg='powder blue', bd=6)
withdrawlbutton.pack(side=TOP, expand=True)

withdrawlfromatmbutton = Button(bankingroot, text='3.Withdrawl From Atm With Out D.C', width=30, font=('arial', 10, 'italic bold'),bg='powder blue', bd=6)
withdrawlfromatmbutton.pack(side=TOP, expand=True)

balanceEnquirybutton = Button(bankingroot, text=' 4.Balance Enquiry ', width=24, font=('arial', 12, 'italic bold'),bg='powder blue', bd=6)
balanceEnquirybutton.pack(side=TOP, expand=True)

deleteAccountbutton = Button(bankingroot, text=' 5.Delete Account ', width=24, font=('arial', 12, 'italic bold'),bg='powder blue', bd=6)
deleteAccountbutton.pack(side=TOP, expand=True)

logoutbutton = Button(bankingroot, text=' 6.Log Out ', width=24, font=('arial', 12, 'italic bold'),bg='powder blue', bd=6)
logoutbutton.pack(side=TOP, expand=True)

bankingroot.mainloop()