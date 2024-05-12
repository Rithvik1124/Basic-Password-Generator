#importing modules- tkinter, random, pyperclip

from tkinter import *
from random import *
from tkinter import messagebox
import pyperclip


#Creating a default window
root=Tk()
root.configure(bg='#3d3b3b')
root.title('Password Generator')
root.geometry('400x400')
#Adding title
title=Label(root,text='Password Generator',bg='#3d3b3b',fg='#26fca6',font=('Fixedsys',20,'bold','underline'))
title.pack()

#Creating Variables, true/false values for checkbuttons
pass_var=StringVar()
lo=None
up=None
num=None
sym=None
var1=BooleanVar()
var1.set(0)
var2=BooleanVar()
var2.set(0)
var3=BooleanVar()
var3.set(0)
var4=BooleanVar()
var4.set(0)
ent_var=IntVar()
ent_var.set(1)

#FUNCTIONS

#Function for checking if uppercase checkbuttin is selected
def select_rad1():
    global up
    if  var1.get():  
        up=True
    elif var1.get()==False:
        up=False

#Function for checking if lowercase checkbuttin is selected
def select_rad2():
    global lo
    if  var2.get():  
        lo=True
    elif var2.get()==False:
        lo=False
#Function for checking if numbers checkbuttin is selected
def select_rad3():
    global num
    if  var3.get():  
        num=True
    elif var3.get()==False:
        num=False

#Function for checking if symbols checkbuttin is selected
def select_rad4():
    global sym
    if  var4.get():  
        sym=True
    elif var4.get()==False:
        sym=False
        
#Password generating function
def gen_pass():
    global lo,up,num,sym
    MAX_LEN = ent_var.get()
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z'] 
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<'] 
  
    COMBINED_LIST = []
    temp_pass = ''
    temp_lo=lo
    temp_sym=sym
    temp_up=up
    temp_num=num
    
    for i in range(4):
        if lo is True:
            COMBINED_LIST+=LOCASE_CHARACTERS
            lo=False
        elif up:
            COMBINED_LIST+=UPCASE_CHARACTERS
            up=False
        elif num:
            COMBINED_LIST+=DIGITS
            num=False
        elif sym:
            COMBINED_LIST+=SYMBOLS
            sym=False
    lo=temp_lo
    sym=temp_sym
    up=temp_up
    num=temp_num
    
    try:
        for x in range(MAX_LEN):
            temp_pass+=choice(COMBINED_LIST) 
        password=temp_pass
    
        pass_var.set(password)
            
            
    except Exception as ex:
        print(ex)
        messagebox.showwarning(title='Error!', message='Please choose atleast one character type!')

#Copy button function
def copy():
    pyperclip.copy(pass_var.get())
    messagebox.showinfo(title='Password Copied!!', message='Password has been copied')

#Entry for outputting password
pass_ent=Entry(root,textvariable=pass_var,width=30,bg='#c4bebe',fg='#000000',font=('Fixedsys',15,'bold'))

#Subtitles (Characters,length)
tt1=Label(root,text='Characters',font=('Fixedsys',15,'bold','underline'),bg='#3d3b3b',fg='#26fca6').place(x=20,y=160)
tt2=Label(root,text='Length',font=('Fixedsys',15,'bold','underline'),bg='#3d3b3b',fg='#26fca6').place(x=200,y=160)

#Spinbox for selecting length of password
ent=Spinbox(root,textvariable=ent_var,from_=1,to=50,width=10,bg='#c4bebe',fg='#000000',font=('Fixedsys',15,'bold'))


#Checkbuttons for selecting variance of characters in password
rad1=Checkbutton(root,text='ABC',variable=var1,onvalue=1,offvalue=0,command=select_rad1,bg='#696666',fg='#26fca6',font=('Fixedsys',15,'bold'))
rad2=Checkbutton(root,text='abc',variable=var2,onvalue=1,offvalue=0,command=select_rad2,bg='#696666',fg='#26fca6',font=('Fixedsys',15,'bold'))
rad3=Checkbutton(root,text='123',variable=var3,onvalue=1,offvalue=0,command=select_rad3,bg='#696666',fg='#26fca6',font=('Fixedsys',15,'bold'))
rad4=Checkbutton(root,text='~@#',variable=var4,onvalue=1,offvalue=0,command=select_rad4,bg='#696666',fg='#26fca6',font=('Fixedsys',15,'bold'))

#Creating password
create=Button(root,text='Create Password',font=('Fixedsys',15,'bold'),width=25,command=lambda:gen_pass(),bg='#696666',fg='#26fca6')

#Copy Button
copy_but=Button(root,text='Copy',command=lambda:copy(),bg='#696666',fg='#26fca6',font=('Fixedsys',12,'bold'))


#Placing widgets using coordinates
pass_ent.place(x=30,y=50)
rad1.place(x=20,y=200)
rad2.place(x=20,y=250)
rad3.place(x=100,y=200)
rad4.place(x=100,y=250)
ent.place(x=200,y=200)
create.place(x=50,y=330)
copy_but.place(x=160,y=90)



#Closing default window
root.mainloop()
