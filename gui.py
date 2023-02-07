import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.title("REIIE User Interface")
window.geometry("1700x1500")
mf = tk.Frame(window, width = 300, height = 300)
mf.pack(fill=tk.BOTH, expand = 1)
mycanv = tk.Canvas(mf, width = 300, height = 300)
mycanv.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
myscroll = tk.Scrollbar(mf, orient = tk.VERTICAL, command = mycanv.yview)
myscroll.pack(side = tk.LEFT, fill=tk.Y)
mycanv.config(yscrollcommand=myscroll.set)
mycanv.bind('<Configure>', lambda e: mycanv.config(scrollregion = mycanv.bbox("all")))
secondframe = tk.Frame(mycanv)
mycanv.create_window((0,0), window = secondframe, anchor = "nw")

rt = 10 
individualLampStrength = 0.01
oxidantstrength = 0.001

img0 = Image.open("p1.png")
img= img0.resize((600,500), Image.ANTIALIAS)
ph = ImageTk.PhotoImage(img)
label = tk.Label(secondframe, image = ph)
label.image=ph
label.pack()
global lamp1
global lamp1state
global lamp2
global lamp2state
global lamp3
global lamp3state
global lamp4
global lamp4state
global lamp5
global lamp5state
global solenoid1
global solenoid2
global solenoid1state
global solenoid2state
global usedoxidantvalue
global oxidantvalue
global feedback
global e1
global w1 
global w2
global w3
global P
lamp1 = tk.Label(secondframe, text = "L1: OFF", bg = "red",font = ('Helvetica', 15), relief = "raised")
lamp1.pack()
lamp1state=False
lamp2 = tk.Label(secondframe, text = "L2: OFF", bg = "red", font = ('Helvetica', 15), relief = "raised")
lamp2.pack()
lamp2state=False
lamp3 = tk.Label(secondframe, text = "L3: OFF", bg = "red", font = ('Helvetica', 15), relief = "raised")
lamp3.pack()
lamp3state=False
lamp4 = tk.Label(secondframe, text = "L4: OFF", bg = "red", font = ('Helvetica', 15), relief = "raised")
lamp4.pack()
lamp4state=False
lamp5 = tk.Label(secondframe, text = "L5: OFF", bg = "red", font = ('Helvetica', 15), relief = "raised")
lamp5.pack()
lamp5state=False

solenoid1 = tk.Label(secondframe, text = "SV1: ON", bg = "green", font = ('Helvetica', 15), relief = "raised")
solenoid1.pack()
solenoid1state = True
solenoid2 = tk.Label(secondframe, text = "SV2: OFF", bg = "red", font = ('Helvetica', 15), relief = "raised")
solenoid2.pack()
solenoid2state = False

def getnewsensorvalue():
    sensorvalue = random.SystemRandom().uniform(1,2.5)
    return sensorvalue
def getnewtreatedvalue():
    treatedvalue = random.SystemRandom().uniform(0,1.25)
    return treatedvalue

sensorvalue = getnewsensorvalue()
treatedvalue = getnewtreatedvalue()
oxidantvalue = 150
usedoxidantvalue=0
while(sensorvalue<treatedvalue):
    sensorvalue = getnewsensorvalue()

treatedval = tk.Label(secondframe, text = "Sensor Reading of Treated (desired): "+str(treatedvalue))
treatedval.pack()
sensorval = tk.Label(secondframe, text = "Sensor Reading of Untreated: "+str(sensorvalue))
sensorval.pack()
unusedoxidval = tk.Label(secondframe, text = "Unused Oxidant Amount: "+ str(oxidantvalue))
unusedoxidval.pack()
usedoxidval = tk.Label(secondframe, text = "Used Oxidant Amount: "+str(usedoxidantvalue))
usedoxidval.pack()
P = oxidantvalue
state = tk.Label(secondframe, text = "")
state.pack()

def number():
    try:
        int(e1.get())
        if (int(e1.get())%5==0):
            feedback.config(text="")
            UVLamps(1, 0)
            w1.set(e1.get())
            w3.set(10)
        else: 
            feedback.config(text = "Invalid Input. Must be a multiple of 5.")
    except ValueError:
        feedback.config(text = "Invalid Input. Must be an integer, and a nonzero multiple of 5.")
def LampON(n):
    global lamp1, lamp1state, lamp2, lamp2state, lamp3, lamp3state, lamp4, lamp4state, lamp5, lamp5state
    if (n==1):
        lamp1.config( text = "L1: ON", bg = "green")
        lamp1.pack()
        lamp1state =True
    elif (n==2):
        lamp2.config(text = "L2: ON", bg = "green")
        lamp2.pack()
        lamp2state = True
    elif (n==3):
        lamp3.config(text = "L3: ON", bg = "green")
        lamp3.pack()
        lamp3state = True
    elif (n==4):
        lamp4.config(text = "L4: ON", bg = "green")
        lamp4.pack()
        lamp4state = True
    else:
        lamp5.config(text = "L5: ON", bg = "green")
        lamp5.pack()
        lamp5state = True

def LampOFF(n):
    global lamp1, lamp1state, lamp2, lamp2state, lamp3, lamp3state, lamp4, lamp4state, lamp5, lamp5state
    if (n==1):
        lamp1.config(text = "L1: OFF", bg = "red")
        lamp1.pack()
        lamp1state = False
    elif (n==2):
        lamp2.config(text = "L2: OFF",  bg = "red")
        lamp2.pack()
        lamp2state = False
    elif (n==3):
        lamp3.config(text = "L3: OFF",  bg = "red")
        lamp3.pack()
        lamp3state = False
    elif (n==4):
        lamp4.config(text = "L4: OFF",  bg = "red")
        lamp4.pack()
        lamp4state = False
    else:
        lamp5.config(text = "L5: OFF" , bg = "red")
        lamp5.pack()
        lamp5state = False

p1 = tk.Label(secondframe, text = "Enter speed of PP1(increments of 5):")
p1.pack()
e1 = tk.Entry(secondframe)
e1.pack()
w1 = tk.Scale(secondframe, from_=0, to=100,label = "PP1 Speed", length = 500, tickinterval = 5, orient = tk.HORIZONTAL)
w1.pack()
b1 = tk.Button(secondframe, text = "Submit", command = number)
b1.pack()
feedback = tk.Label(secondframe, text = "")
feedback.pack()
p2 = tk.Label(secondframe, text = "Speed of PP2:")
p2.pack()
w2 = tk.Scale(secondframe, from_=0, to=100,label = "PP2 Speed", length = 500, tickinterval = 5, orient = tk.HORIZONTAL)
w2.pack()

p3 = tk.Label(secondframe, text = "Speed of PP3:")
p3.pack()
w3 = tk.Scale(secondframe, from_=0, to=100,label = "PP3 Speed", length = 500, tickinterval = 5, orient = tk.HORIZONTAL)
w3.pack()

def UVLamps(n, currentoxidantamount):
    global solenoid1state, solenoid2state, lamp1state, lamp2state, lamp3state, lamp4state, lamp5state, P
    LampON(n)
    currentlevel=sensorvalue-(rt*1.5*individualLampStrength*n)-currentoxidantamount*oxidantstrength 
    while ((currentlevel-treatedvalue-currentoxidantamount*oxidantstrength>0.1) and (n<=5)):
        n+=1
        LampON(n)
        currentlevel -=rt*1.5*individualLampStrength 
    if (currentlevel-treatedvalue-currentoxidantamount<=0.1):
        successful()
    elif (lamp5state==True and currentoxidantamount<P):
        state.config(text = "UV Treatment Insufficient. Reiterating to find optimal level of required oxidant...")
        state.pack()
        pumping()
    else:
        state.config(text = "Error: System Underdesigned.")
        state.pack()

def successful():
    global solenoid1state, solenoid2state, oxidantvalue, lamp1, lamp1state, lamp2, lamp2state, lamp3, lamp3state, lamp4, lamp4state, lamp5, lamp5state
    solenoid1.config(text = "SV1: OFF", bg = "red")
    solenoid1.pack()
    solenoid1state = False
    solenoid2.config(text = "SV2: ON", bg = "green")
    solenoid2.pack()
    solenoid2state = True
    state.config(text ="REIIE Successful. Transferring to Treated Flask...")
    state.pack()
    if (lamp1state==True and lamp2state==False):  
        img0 = Image.open("l1.png")
        img= img0.resize((600,500), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img)
        label.config(image = ph)
        label.image=ph
        label.pack()
    elif (lamp2state==True and lamp3state==False):
        img0 = Image.open("l2.png")
        img= img0.resize((600,500), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img)
        label.config(image = ph)
        label.image=ph
        label.pack()
    elif (lamp3state==True and lamp4state==False):
        img0 = Image.open("l3.png")
        img= img0.resize((600,500), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img)
        label.config(image = ph)
        label.image=ph
        label.pack()
    elif (lamp4state==True and lamp5state==False):
        img0 = Image.open("l4.png")
        img= img0.resize((600,500), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img)
        label.config(image = ph)
        label.image=ph
        label.pack()
    elif (lamp5state==True):
        img0 = Image.open("l5.png")
        img= img0.resize((600,500), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(img)
        label.config(image = ph)
        label.image=ph
        label.pack()

def pumping():
    global solenoid1state, solenoid2state, oxidantvalue, usedoxidantvalue
    LampOFF(2)
    LampOFF(3)
    LampOFF(4)
    LampOFF(5)
    usedoxidantvalue+=10
    oxidantvalue-=10
    usedoxidval.config(text = "Used Oxidant Amount: "+str(usedoxidantvalue))
    unusedoxidval.config(text="Unused Oxidant Amount: "+ str(oxidantvalue))
    w3.set(usedoxidantvalue)
    UVLamps(1, usedoxidantvalue)

def clearfunc():
    global sensorvalue, oxidantvalue, usedoxidantvalue, solenoid1state, solenoid2state, feedback, e1, w1, w2, w3
    sensorvalue = getnewsensorvalue()
    treatedvalue = getnewtreatedvalue()
    oxidantvalue = 150
    usedoxidantvalue=0
    while(sensorvalue<treatedvalue):
        sensorvalue = getnewsensorvalue()
    LampOFF(1)
    LampOFF(2)
    LampOFF(3)
    LampOFF(4)
    LampOFF(5)
    treatedval.config(text = "Sensor Reading of Treated (desired): "+str(treatedvalue))
    treatedval.pack()
    sensorval.config(text = "Sensor Reading of Untreated: "+str(sensorvalue))
    sensorval.pack()
    unusedoxidval.config(secondframe, text = "Unused Oxidant Amount: 150")
    unusedoxidval.pack()
    usedoxidval.config(secondframe, text = "Used Oxidant Amount: 0")
    usedoxidval.pack()
    state.config(text = "")
    state.pack()
    solenoid1.config(text = "SV1: ON", bg = "green")
    solenoid1.pack()
    solenoid1state = True
    solenoid2.config(text = "SV2: OFF", bg = "red")
    solenoid2.pack()
    solenoid2state = False
    feedback.config(text="")
    w1.set(0)
    e1.delete(0, tk.END)
    feedback = tk.Label(secondframe, text = "")
    feedback.pack()
    w2.set(0)
    w3.set(0)
    img0 = Image.open("p1.png")
    img= img0.resize((600,500), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(img)
    label.config(image = ph)
    label.image=ph

reset = tk.Button(secondframe,text = "Reset Interface", command = clearfunc)
reset.pack(pady=30)


button_quit = tk.Button(secondframe, text = "Exit Interface", command = secondframe.quit)
button_quit.pack(pady=30)


window.mainloop()