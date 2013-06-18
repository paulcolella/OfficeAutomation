##"SMART" OFFICE AUTOMATION CONTROL
##User Interface

from Tkinter import *
import socket
import time


root = Tk()

root.title("Rest Devices Office Automation")
root.geometry("600x800")
root.configure(background = "SteelBlue")

##Controlable Devices:
##In order to add a new office device simply add it to these lists
##then use the interface to add functions of that item
##please also remember to add new items to text

deviceList = ["device1 on", "device1 off", "device2 on", "device2 off", "device3 on", "device3 off"]

##Variables

EntryText1 = StringVar()
EntryText2 = StringVar()
statusReport = StringVar()
Status = StringVar()

##Functions:
##these build up the link between the input data and the brain
##first they will check the validity of the input then they will
##determin which action to take

def connectAndSend(data):
    s = socket.socket()
    host = socket.gethostname()
    port = 7776
    s.connect((host,port))
    s.send(data)
    time.sleep(1)
    s.send("User")
    s.close()

def statUp():
    text3.configure(text = statusReport.get())
    return

def automatic():
    print EntryText1.get()
    print EntryText1.get() + " A"
    if EntryText1.get() in deviceList:
        print EntryText1.get() + " A"
        connectAndSend(EntryText1.get() + " A")
        statusReport.set(EntryText1.get() + " A")
        statUp()
    if EntryText1.get() == "SHUTDOWN":
        print "SHUTTING DOWN"
        connectAndSend("SHUTDOWN")

def manual():
    print EntryText2.get()
    print EntryText2.get() + " M"
    if EntryText1.get() in deviceList:
        print EntryText1.get() + " M"
        connectAndSend(EntryText2.get() + " M")
        statusReport.set(EntryText2.get() + " M")
        statUp()
    if EntryText2.get() == "SHUTDOWN":
        print "SHUTTING DOWN"
        connectAndSend("SHUTDOWN")

        

##Labels, Buttons, and data input
##I realize that this is not as neat as possible, I was undable to
##assign variables such as font on a large scale and was forced to
##repeat for every item

head = Label(root, text = "Rest Devices Office Automation", fg = "White", \
             bg = "SteelBlue", font = ("arial", 30), justify = "left")
text1 = Label(root, text = "The devices currently supported are" \
             " light1, light2, light3, blinds1, blinds2, and bike1. " \
              
             "NOTE: The manual setting will only activate that device" \
             " while the automatic setting will activate the desired" \
             " device as well as its dependent devices. Enter items" \
             " as a tuple ('ITEM', 'ON') or ('ITEM', 'OFF'). On is down for bike/blinds" \
             " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" \
             " AUTOMATIC CONTROL", \
              font = ("arial", 14), wraplength = 600, bg = "SteelBlue", fg = "White")             


entry1 = Entry(root, textvariable = EntryText1, width = 200, \
                   font = "arial", fg = "black", bg = "White", bd = 5)

button1 = Button(root, text = "SUBMIT", fg = "DarkGreen", \
                     bg = "SlateGray", activebackground = "BurlyWood", \
                     font = "arial", command = automatic)

text2 = Label(root, text = " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" \
              "MANUAL CONTROL", font = ("arial", 14), wraplength = 600, \
              bg = "SteelBlue", fg = "White")

entry2 = Entry(root, textvariable = EntryText2, width = 200, \
                   font = "arial", fg = "black", bg = "White", bd = 5)

button2 = Button(root, text = "SUBMIT", fg = "DarkGreen", \
                     bg = "SlateGray", activebackground = "BurlyWood", \
                     font = "arial", command = manual)


text3 = Label(root, text = None, font = ("arial", 30), fg = "White", \
              bg = "SteelBlue")

head.pack()
text1.pack()
entry1.pack()
button1.pack()
text2.pack()
entry2.pack()
button2.pack()
text3.pack()




root.mainloop()
