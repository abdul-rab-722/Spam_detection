import tkinter as tk
from tkinter import filedialog
from tkinter import *
from checkspam import check_spam
from PIL import ImageTk, Image

top=tk.Tk()
top.geometry('1000x600')
top.title('Spam Detector')
top.iconbitmap('.\\images\\icons\\sd_icon.ico')
top.configure(background='white')
    
def check(message_text, new_window):
    result=check_spam(message_text.get('1.0', END))
    if result=='spam':  result='Definitely spam!'
    else: result='That\'s not spam'
    result_label=Label(new_window, text=result)
    result_label.configure(background='#ebf9f7', foreground='#05232c', font='arial 14 bold')
    result_label.place(relx=0.73, rely=0.46)

def show_test_button(new_window, message_text):
    test_button=Button(new_window,text="Test me",command=lambda: check(message_text, new_window),padx=10,pady=5)
    test_button.place(relx=0.33,rely=0.83)

def new_test():
    new_window=Toplevel()
    new_window.geometry('900x470')
    new_window.title('Test New Message')
    new_window.iconbitmap('.\\images\\icons\\sd_icon.ico')
    new_window.configure(background='#ebf9f7')
    new_text=Label(new_window,text='Type in a message to check')
    new_text.configure(background='#ebf9f7', foreground='#05232c', font='arial 14 bold')
    new_text.pack(side='top',pady=25)
    message_text=Text(new_window, height=15, width=55)
    message_text.insert(END, 'Put your message here')
    message_text.tag_add(SEL, '1.0', END)
    message_text.focus_set()
    message_text.place(relx=0.13,rely=0.25)
    show_test_button(new_window,message_text)

def show_help():
    help_window=Toplevel()
    help_window.geometry('900x470')
    help_window.title('Help - Spam Detector')
    help_window.iconbitmap('.\\images\\icons\\sd_icon.ico')
    help_window.configure(background='#ebf9f7')
    spam_text=Label(help_window,text='What is Spam?')
    spam_text.configure(background='#ebf9f7', foreground='#05232c', font='arial 14 bold underline')
    spam_text.place(relx=0.06,rely=0.08)
    spam_help_text=Label(help_window, text="Spam is any irrelevant and/or unsolicited message you may receive over the Internet. This is usually sent to a large number of users (in bulk) for different purposes like advertising, phishing, and spreading malware. Spam may even be generated using botnets.", wraplength=800, justify=LEFT)
    spam_help_text.configure(background='#ebf9f7', foreground='#05232c', font='arial')
    spam_help_text.place(relx=0.06,rely=0.18)
    sd_text=Label(help_window,text='What is this Spam Detector?')
    sd_text.configure(background='#ebf9f7', foreground='#05232c', font='arial 14 bold underline')
    sd_text.place(relx=0.06,rely=0.45)
    sd_help_text=Label(help_window, text="This Spam Detector helps you identify whether a message is spam or ham. Just put in a message and it will tell you the results.", wraplength=800, justify=LEFT)
    sd_help_text.configure(background='#ebf9f7', foreground='#05232c', font='arial')
    sd_help_text.place(relx=0.06,rely=0.52)

sd_img=Image.open('.\\images\\others\\Spam Detector.jpg')
sd_img.thumbnail((top.winfo_width(),top.winfo_height()))
sd_img=ImageTk.PhotoImage(sd_img)
sd_label=Label(top,image=sd_img)
sd_label.image=sd_img
sd_label.pack(side='top',expand='yes')

new_button=Button(top,text="Test a message",command=new_test,padx=20,pady=7)
new_button.configure(background='#09B29D',foreground='white',font=('arial',13,'bold'))
new_button.place(relx=0.42,rely=0.84)
help_img=Image.open('.\\images\\icons\\help.png')
help_img.thumbnail((20,20))
help_img=ImageTk.PhotoImage(help_img)
sample=Button(top,command=show_help,padx=10,pady=5, borderwidth=0, cursor='hand2', image=help_img,text="Help", compound='left')
sample.configure(background='#EED3B6',foreground='black',font=('arial',10))
sample.place(relx=0.90,rely=0.06)

top.mainloop()
