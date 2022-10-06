#QRCode_Generator
#Author = Pathfinder
#Simple QrCode Generator in Python

import tkinter
import pyqrcode
import shutil
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
 
'''# System call
os.system("")
 
#colored text codes
class colors:
    BLACK = '\033[30m'
    DRED = '\033[31m'
    DGREEN = '\033[32m'
    DYELLOW = '\033[33m'
    DBLUE = '\033[34m'
    DPINK = '\033[35m'
    HRED = '\033[41m'
    HGREEN = '\033[42m'
    HYELLOW = '\033[43m'
    HBLUE = '\033[44m'
    HPINK = '\033[45m'
    RESET = '\033[0m'
 
print(colors.DRED + "This is an Simple QRCode Generator!")
 
#input string which represents the QR code
S = input(colors.DBLUE + "Paste Link for QRCode generation here: ")

#gen QRCode
url = pyqrcode.create(S)
 
#choose name for QRCode
N = input(colors.DBLUE + "Choose Name for QRCode: ")
 
#choose file format
print(colors.DRED + "What file format should your QRCode have?")
F = int(input(colors.DBLUE + "Press 1 for SVG or Press 2 for PNG: "))
 
#create QRCode
if F == 1:
    url.svg("{}.svg".format(N), scale=8)
elif F == 2:
    url.png("{}.png".format(N), scale=8)
else:
    print(colors.DPINK + "incorrect Input!")
    print(colors.DGREEN + "exiting...")
    exit(1)
 
#save location
SV = input(colors.DBLUE + "Save this File to a specific Location? (Y/N)")
 
if SV == "Y" and F == 1:
    SP = input(colors.DBLUE + "State Save Location here: ")
    shutil.move("{}.svg".format(N), '{}'.format(SP)) #move file to save location
    print(colors.DRED + "QRCode Generated and moved to {}".format(SP))
    print("exiting...")
elif SV == "Y" and F == 2:
    SP = input(colors.DBLUE + "State Save Location here: ")
    shutil.move("{}.png".format(N), '{}'.format(SP)) #move file to save location
    print(colors.DRED + "QRCode Generated and moved to {}".format(SP))
    print(colors.DGREEN + "exiting...")
elif SV == "N":
    print(colors.DRED + "QRCode Generated")
    print(colors.DGREEN + "exiting...")
    exit(1)
else:
    exit(1)'''
 
 
root = Tk()
root.title("Simple QR-Coder Generator")
root.geometry("350x250")
root.resizable(width=True, height=True)
 
def print_Input():
    LinkInp = Link.get()
    return LinkInp
 
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
 
Link = StringVar()
Link_entry = ttk.Entry(mainframe, width=10, textvariable=Link).grid(column=2, row=1, sticky=(W, E))
 
Name = StringVar()
Name_entry = ttk.Entry(mainframe, width=10, textvariable=Name).grid(column=2, row=2, sticky=(W, E))
 
Format = StringVar()
Format = ttk.Combobox(mainframe, textvariable=Format)
Format.grid(column=2, row=3, sticky=(W, E))
Format['values'] = ('PNG', 'SVG')
 
SaveLoc = StringVar()
SaveLoc_entry = ttk.Entry(mainframe, width=10, textvariable=SaveLoc).grid(column=2, row=4, sticky=(W, E))
 
s = ttk.Style()
s.configure('Danger.TFrame', background='black', borderwidth=5, relief='raised', )
ttk.Frame(mainframe, width=150, height=150, style='Danger.TFrame').grid(column=1)
 
'''path = 'youtube.png'
img = ImageTk.PhotoImage(Image.open(path))
panel = ttk.Label(mainframe, image=img)
panel.grid(column= 1, row=5, sticky=(W, E))'''
 
ttk.Button(mainframe, text="Show QR-Code", command=print_Input).grid(column=2, row=5, sticky=W)
 
ttk.Label(mainframe, text="Insert Link for QR-Code here: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Choose a name for the QR-Code File:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Choose a QR-Code File-format: ").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="State a specific Save Location: ").grid(column=1, row=4, sticky=W)
 
root.mainloop()
 