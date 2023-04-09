
import numpy as np
import pyaudio
import cv2
import os
import PIL
from PIL import ImageTk
import PIL.Image
import speech_recognition as sr
import pyttsx3
from itertools import count
import string
from tkinter import *
import time
try:
    import Tkinter as tk
except:
    import tkinter as tk
import numpy as np
r = sr.Recognizer()
image_x, image_y = 64,64
window=Tk()
message = Label(window, text="" ,bg="#DDEEF1"  ,fg="black"  ,width=47  ,height=12, activebackground = "yellow" ,font=('Helvetica', 20 , ' bold ')) 
message.place(x=150, y=170)
def check_sim(i,file_map):
       for item in file_map:
              for word in file_map[item]:
                     if(i==word):
                            return 1,item
       return -1,""


alpha_dest="./alphabet/"

def func(a):
       all_frames=[]
       final= PIL.Image.new('RGB', (380, 260))
       words=a.split()
       for i in words:
              for j in i:
                     print(j)
                     im = PIL.Image.open(alpha_dest+str(j).lower()+"_small.gif")
                     frameCnt = im.n_frames
                     for frame_cnt in range(frameCnt):
                            im.seek(frame_cnt)
                            im.save("tmp.png")
                            img = cv2.imread("tmp.png")
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            img = cv2.resize(img, (380,260))
                            im_arr = PIL.Image.fromarray(img)
                            for itr in range(15):
                                   all_frames.append(im_arr)
       final.save("out.gif", save_all=True, append_images=all_frames, duration=100, loop=0)
       return all_frames      

img_counter = 0
img_text=''
cnt=0
gif_frames=[]
inputtxt=None
label = tk.Label(window, text="Voice to Sign", font=("Verdana", 12))
label.pack(pady=10,padx=10)
gif_box = tk.Label(window)
def gif_stream():
       global cnt
       global gif_frames
       if(cnt==len(gif_frames)):
              return
       img = gif_frames[cnt]
       cnt+=1
       imgtk = ImageTk.PhotoImage(image=img)
       gif_box.imgtk = imgtk
       gif_box.configure(image=imgtk)
       gif_box.after(50, gif_stream)
def hear_voice():
       inputtxt.delete("1.0", "end-1c")
       with sr.Microphone() as source2:
              audio2 = r.listen(source2,timeout=3, phrase_time_limit=3)
              text_output = r.recognize_google(audio2)
              text_output =  text_output.lower()
              inputtxt.insert(END,text_output)
              
def Take_input():
       INPUT = inputtxt.get("1.0", "end-1c")
       print(INPUT)
       global gif_frames
       gif_frames=func(INPUT)
       global cnt
       cnt=0
       gif_stream()
       gif_box.place(x=350,y=200)
       INPUT=None
message = Label(window, text="Speech/Text to Sign language" ,bg="#8D9AF3"  ,fg="#A10390"  ,width=40  ,height=3,font=('Helvetica', 35, 'italic bold '))
message.place(x=60, y=0)
lbl2 = Label(window, text="Enter text :",width=20  ,fg="white"  ,bg="#435F9F"    ,height=2 ,font=('Helvetica', 20 , ' bold ')) 
lbl2.place(x=150, y=490)
inputtxt = tk.Text(window,height=1,width=35 ,bg="white" ,fg="black",font=('Helvetica', 20 , ' bold '))
inputtxt.place(x=390, y=505)
picspeech = Button(window, text="Record Audio",fg="#8D2292"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '),command=lambda: hear_voice())
picspeech.place(x=1000, y=270)
textspeech = Button(window, text="Convert",fg="#8D2292"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '),command = lambda:Take_input())
textspeech.place(x=1000, y=370)
quitWindow = Button(window, text="Quit", command=window.destroy  ,fg="#8D2292"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
quitWindow.place(x=1000, y=600)

window.geometry('1280x732')
window.mainloop()