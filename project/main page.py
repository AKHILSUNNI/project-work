import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as font
import os

top = Tk()
top.geometry("800x500")

myFont = font.Font(size=10)
def click():
    messagebox.showinfo("Hello", "Green Button clicked")
img=Image.open("./ss4.jpg")
nimage=img.resize((800,500))
photo = ImageTk.PhotoImage(nimage)
img_label = Label(top,image=photo)
img_label.pack()

def tts():
    os.system('text-to-speech.py')
def sts():
    os.system('speech-to-sign.py')
a = Button(top, text="Gesture controlled virtual mouse", fg="black", bg="#637CED", activeforeground="black", activebackground="#87b9fa", pady=15,width=30)
b = Button(top, text="Text-to-speech conversion",fg="black", bg="#637CED", activeforeground="black", activebackground="#87b9fa", pady=15,width=30, command=tts)
# adding click function to the below button
c = Button(top, text="Sign language generation",fg="black", bg="#637CED", command=sts, activeforeground = "black", activebackground="#87b9fa", pady=15,width=30)
d = Button(top, text="Sign language reognition",fg="black", bg="#637CED", activeforeground="black", activebackground="#87b9fa", pady=15,width=30)
a['font'] = myFont
b['font'] = myFont
c['font'] = myFont
d['font'] = myFont

a.place(x=50,y=150)
b.place(x=500,y=150)
c.place(x=50,y=300)
d.place(x=500,y=300)
top.resizable(width=False, height=False)
top.mainloop()