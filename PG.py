from tkinter import *
import random, string
import pyperclip

graphic = Tk()
graphic.geometry("400x400")
graphic.resizable(0,0)
graphic.title( "PASSWORD GENERATOR")

Label(graphic, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(graphic, text ='SunnyCide', font ='arial 15 bold').pack(side = BOTTOM)

pass_label = Label(graphic, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(graphic, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(graphic, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(graphic , textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(graphic, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

graphic.mainloop()

