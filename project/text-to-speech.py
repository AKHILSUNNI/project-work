from gtts import gTTS         
import PIL                    
import gtts               
import pytesseract           
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USAA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from tkinter import filedialog 
from tkinter import *
from PIL import Image,ImageTk  
import pyperclip
from playsound import playsound
import cv2
import os


window = Tk()
window.geometry('1280x732')
window.resizable(0, 0)
window.title("Image-Text-Speech Conversion")
image=Image.open("ss2.jpg")
photo=ImageTk.PhotoImage(image)
lab=Label(image=photo,bg='#1F3AEF')
lab.pack()


message = Label(window, text="Image-Text-Speech Conversion" ,bg="#8D9AF3"  ,fg="#A10390"  ,width=40  ,height=3,font=('Helvetica', 35, 'italic bold '))
message.place(x=60, y=0)
message = Label(window, text="Note : Text field in only for 'Text-to-Audio' file\n RIGHT CLICK to paste the text copied from 'Pic-to-Text' file" ,bg="#6D7BD6"  ,fg="#000000"  ,width=70  ,height=2,font=('Helvetica', 15, 'italic bold '))
message.place(x=130, y=120)
message = Label(window, text="" ,bg="#DDEEF1"  ,fg="black"  ,width=47  ,height=12, activebackground = "yellow" ,font=('Helvetica', 20 , ' bold ')) 
message.place(x=150, y=170)
lbl2 = Label(window, text="Enter text :",width=20  ,fg="white"  ,bg="#435F9F"    ,height=2 ,font=('Helvetica', 20 , ' bold ')) 
lbl2.place(x=150, y=490)
txt2 = Entry(window,width=35  ,bg="white" ,fg="black",font=('Helvetica', 20 , ' bold '))
txt2.place(x=390, y=505)


def PicTexts():
    vid = cv2.VideoCapture(0)

    while(True):
        
        
        ret, frame = vid.read()

        cv2.imshow('Webcam', frame)
       
        key =cv2.waitKey(1)
        if key==113:
            break
        if key==99:
            cv2.imwrite('images/demo.jpg',frame)

    
    vid.release()
    cv2.destroyAllWindows()
    
    result= pytesseract.image_to_string('images/demo.jpg')  
    res = "***Text copied***\n" + result
    pyperclip.copy(res)
    message.configure(text= res)
    if(result==""):
        res = "Sorry!! Nothing recogonized"
        message.configure(text= res)

def picSpeechs():
    vid = cv2.VideoCapture(0)

    while(True):
        
       
        ret, frame = vid.read()

        
        cv2.imshow('Webcam', frame)
        
        key =cv2.waitKey(1)
        if key==113:
            break
        if key==99:
            cv2.imwrite('images/demo.jpg',frame)

    
    vid.release()
    
    cv2.destroyAllWindows()
    
    result= pytesseract.image_to_string('images/demo.jpg')
    if(result==""):
        res = "Sorry!! Nothing recogonized"
        message.configure(text= res)   
    res= gTTS(result)                
    res.save('audio.mp3')   
    res = "Saved"
    message.configure(text= res)  
    playsound("audio.mp3")
    os.remove("audio.mp3")

def TextSpeechs(): 
    textInp= (txt2.get())
    res= gTTS(textInp)               
    res.save('audio.mp3')    
    res = "Saved"
    message.configure(text= res)  
    playsound("audio.mp3")
    os.remove("audio.mp3")
    


pictext = Button(window, text="Pic-to-Text", command=PicTexts  ,fg="#8D2292"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
pictext.place(x=1000, y=170)
picspeech = Button(window, text="Pic-to-Audio", command=picSpeechs  ,fg="#8D2292"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
picspeech.place(x=1000, y=270)
textspeech = Button(window, text="Text-to-Audio", command=TextSpeechs  ,fg="#8D2292"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
textspeech.place(x=1000, y=370)
quitWindow = Button(window, text="Quit", command=window.destroy  ,fg="#8D2292"  ,bg="white"  ,width=15  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
quitWindow.place(x=1000, y=600)

window.mainloop()