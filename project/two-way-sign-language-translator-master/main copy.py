
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
from keras.models import load_model
classifier = load_model('model.h5')
window=Tk()
def give_char():
       import numpy as np
       import keras.utils as image
       test_image = image.load_img('tmp1.png', target_size=(64, 64))
       test_image = image.img_to_array(test_image)
       test_image = np.expand_dims(test_image, axis = 0)
       result = classifier.predict(test_image)
       print(result)
       chars="ABCDEFGHIJKMNOPQRSTUVWXYZ"
       indx=  np.argmax(result[0])
       print(indx)
       return(chars[indx])

def check_sim(i,file_map):
       for item in file_map:
              for word in file_map[item]:
                     if(i==word):
                            return 1,item
       return -1,""

op_dest="./filtered_data/"
alpha_dest="./alphabet/"
dirListing = os.listdir(op_dest)
editFiles = []
for item in dirListing:
       if ".webp" in item:
              editFiles.append(item)

file_map={}
for i in editFiles:
       tmp=i.replace(".webp","")
       #print(tmp)
       tmp=tmp.split()
       file_map[i]=tmp

def func(a):
       all_frames=[]
       final= PIL.Image.new('RGB', (380, 260))
       words=a.split()
       for i in words:
              flag,sim=check_sim(i,file_map)
              if(flag==-1):
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
              else:
                     print(sim)
                     im = PIL.Image.open(op_dest+sim)
                     im.info.pop('background', None)
                     im.save('tmp.gif', 'gif', save_all=True)
                     im = PIL.Image.open("tmp.gif")
                     frameCnt = im.n_frames
                     for frame_cnt in range(frameCnt):
                            im.seek(frame_cnt)
                            im.save("tmp.png")
                            img = cv2.imread("tmp.png")
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            img = cv2.resize(img, (380,260))
                            im_arr = PIL.Image.fromarray(img)
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
       inputtxt.delete("1.0", "end-1c")
       print(INPUT)
       global gif_frames
       gif_frames=func(INPUT)
       global cnt
       cnt=0
       gif_stream()
       gif_box.place(x=400,y=160)
       INPUT=None
l = tk.Label(window,text = "Enter Text or Voice:")
l1 = tk.Label(window,text = "OR")
inputtxt = tk.Text(window, height = 4,width = 25)
voice_button= tk.Button(window,height = 2,width = 20, text="Record Voice",command=lambda: hear_voice())
voice_button.place(x=50,y=180)
Display = tk.Button(window, height = 2,width = 20,text ="Convert",command = lambda:Take_input())
l.place(x=50, y=160)
l1.place(x=115, y=230)
inputtxt.place(x=50, y=250)
Display.pack()

window.geometry("800x750")
window.mainloop()