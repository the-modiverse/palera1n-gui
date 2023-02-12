# import system functions
import os
import time
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
# load images in Tkinter python
from PIL import ImageTk, Image
# web
import webbrowser
# sounds
# from pygame import mixer


# frame settings
root = tk.Tk()
frame = tk.Frame(root, width="500", height="250")
frame.pack(fill=BOTH,expand=True)
#tk.Entry(root).pack(fill='x')

# uses current directory to load the image file for the icon
root.iconphoto(False, tk.PhotoImage(file='Resources/palepa1n.png'))

LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""

def detectDevice():
    root.iconphoto(False, tk.PhotoImage(file='Resources/palepa1n.png'))
    messagebox.showinfo("DFU Helper Information", "Look into the terminal window for the DFU Helper.\nAfter the DFU Helper has finished, it will approximately take around 1-2 minutes to restore rootfs.")
    print("Beginning restore rootfs")
    os.system("./Resources/palera1n --force-revert ")
    
def startcheckra1n():

    root.iconphoto(False, tk.PhotoImage(file='Resources/palepa1n.png'))
    messagebox.showinfo("DFU Helper Information", "Look into the terminal window for the dfuhelper.\nAfter the dfuhelper has finished, it will approximately take around 1-2 minutes to jailbreak.")
    
    print("Loading jb script...")
    os.system("./Resources/palera1n ")
    print("Ran jb script.\n")
    #show message to jb
    messagebox.showinfo("palera1n", "Hopefully the jailbreak has been done successfully.\nEnjoy!")
    root.iconphoto(False, tk.PhotoImage(file='settings.gif'))
    

def quitProgram():
    print("Exiting...")
    os.system("exit")
    


root.title('palera1n - v2.0.0')
frame.pack()

#BIG title on program
mainText = Label(root, text="Welcome to palera1n!",font=('Helveticabold', 24))
mainText.place(x=10, y=5)
#label


#label
my_label3 = Label(frame,
                 text = "With <3 from palera1n team")
my_label3.place(x=10, y=220)

my_label4 = Label(frame,
                 text = "Made by: itsnebulalol, mineek, nathan, llsc12, guacaplushy, nyuszika7h, asdfugil, \ndora2ios, elihwyma, 0x7ff, flowerible, Azreal et al.", font=('Helveticabold', 12))
my_label4.place(x=10, y=120)

my_label5 = Label(frame,
                 text = "Thanks to: F121Live, m1stadev, mass1ve-err0r, TheRealKeto, CRKatri, 1Conan, \ntihmstar, xerub, Cryptic, sbingner, Serena, libimobiledevice y nikias.", font=('Helveticabold', 12))
my_label5.place(x=10, y=160)



cButton1 = tk.Button(frame,
                   text="Restore your system",
                   command=detectDevice,
                   state="normal")
cButton1.place(x=10, y=50)

cButton2 = tk.Button(frame,
                   text="Jailbreak rootless",
                   command=startcheckra1n,
                   state="normal")
cButton2.place(x=10, y=80)

img2 = Image.open("Resources/palepa1n.png")
#frame2 = PhotoImage(file=imagefilename, format="gif -index 2")
NewIMGSize2 = img2.resize((100,100), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(NewIMGSize2)
label = Label(frame, image = new_image2)
label.place(x=390, y=0)

#Create a Label to display the link

root.geometry("500x250")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')

root.mainloop()

