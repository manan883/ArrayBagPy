import main
import tkinter as tk
from tkinter import *
import tkinter.simpledialog
from tkinter.simpledialog import *
import os
from PIL import Image, ImageDraw
root = Tk()
popupval = True
#TODO: add the ability to turn off confirmation boxes from the user with a switch. if its off the popups for things like bag was created will be turned off. errors still are on
#methods to call
def popups():
    global popupval
    if popupval == True:
        popupval = False
        tkinter.messagebox.showinfo(title="Bag",message="Popups have been turned off!")
        # print(popupval)
    elif popupval == False:
        popupval = True
        tkinter.messagebox.showinfo(title="Bag",message="Popups have been turned on!")
        # print(popupval)
def makeNewBag():
    bagN = tkinter.simpledialog.askstring(title="Bag", prompt="Enter the new bags name:",parent=root)
    if main.a.checkIfBagExists(bagN) == True:
        #bag exists return to user error bag already exists
        tkinter.messagebox.showinfo(title="Bag",message="ERROR: Bag already exists!")
    elif bagN == None:
        tkinter.messagebox.showinfo(title="Bag",message="ERROR: Bag name can not be null")
    else:
        #add bag to bags in main
        main.a.newBag(bagN)
        if popupval == True:
            tkinter.messagebox.showinfo(title="Bag",message="Bag: '" + bagN + "' was created")
def deleteBag():
    bagN = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the bag name you want to delete:",parent=root)
    if main.a.checkIfBagExists(bagN) == False:
        tkinter.messagebox.showinfo(title="Bag",message="ERROR: Bag does not exist")
    else:
        main.a.deleteBag(bagN)
        if popupval == True:  
            tkinter.messagebox.showinfo(title="Bag",message="Bag: '" + bagN + "' was deleted")
def listBagNotUser(bagN):
    tkinter.messagebox.showinfo(title="Bag",message="Bag: '" + bagN +"' is listed below\n"+main.a.listBag(bagN))
def addElement():
    bagN = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the bag name:",parent=root)
    if main.a.checkIfBagExists(bagN) == False:
        tkinter.messagebox.showinfo(title="Bag",message="ERROR: Bag does not exist!")
    else:
        e = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the element for bag: '" + bagN + "'")
        main.a.addElement(bagN,e)
        if popupval == True:
            listBagNotUser(bagN)
def listUser():
    bagN = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the bag name:",parent=root)
    if main.a.checkIfBagExists(bagN) == True:
        listBagNotUser(bagN)
    else:
        tkinter.messagebox.showinfo(title="Bag",message="ERROR: Bag does not exist!")
def removePos():
    bagN = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the bag name:",parent=root)
    if main.a.checkIfBagExists(bagN) == False:
        tkinter.messagebox.showerror(title="Bag",message="ERROR: Bag does not exist!")
    else:
        e = tkinter.simpledialog.askstring(title="Bag",prompt= "Bag contents listed \n" + main.a.listBag(bagN) + "\n Enter the element you want to remove",parent=root)
        if main.a.checkIfElementExist(e,bagN) == False:
            tkinter.messagebox.showerror(title="Bag",message="Element: '" + e + "' does not exist in bag: '" + bagN + "'!")
        else:
            main.a.removeE(e,bagN)
        if popupval == True:
            tkinter.messagebox.showinfo(title="Bag",message="Element: '" + e + "' has been removed from bag: '" + bagN +"'")
def unionB():
    bag1 = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the first bags name: ",parent=root)
    bag2 = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the second bags name: ",parent=root)
    newB = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the new bags name: ",parent=root)
    if ((main.a.checkIfBagExists(bag1) == False) or (main.a.checkIfBagExists(bag2) == False)):
        tkinter.messagebox.showerror(title="Bag",message="ERROR: At least one bag does not exist!")
    elif(main.a.checkIfBagExists(newB) == True):
        tkinter.messagebox.showerror(title="Bag",message="ERROR: The new bag already exists")
    else:
        main.a.union(bag1,bag2,newB)
    if popupval == True:
        listBagNotUser(newB)
def intersectB():
    bag1 = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the first bags name: ",parent=root)
    bag2 = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the second bags name: ",parent=root)
    newB = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the new bags name: ",parent=root)
    if ((main.a.checkIfBagExists(bag1) == False) or (main.a.checkIfBagExists(bag2) == False)):
        tkinter.messagebox.showerror(title="Bag",message="ERROR: At least one bag does not exist!")
    elif(main.a.checkIfBagExists(newB) == True):
        tkinter.messagebox.showerror(title="Bag",message="ERROR: The new bag already exists")
    else:
        main.a.intersection(bag1,bag2,newB)
    if popupval == True:
        listBagNotUser(newB)
def differenceB():
    bag1 = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the first bags name: ",parent=root)
    bag2 = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the second bags name: ",parent=root)
    newB = tkinter.simpledialog.askstring(title="Bag",prompt="Enter the new bags name: ",parent=root)
    if ((main.a.checkIfBagExists(bag1) == False) or (main.a.checkIfBagExists(bag2) == False)):
        tkinter.messagebox.showerror(title="Bag",message="ERROR: At least one bag does not exist!")
    elif(main.a.checkIfBagExists(newB) == True):
        tkinter.messagebox.showerror(title="Bag",message="ERROR: The new bag already exists")
    else:
        main.a.difference(bag1,bag2,newB)
    if popupval == True:
        listBagNotUser(newB)
def pageTwo():
    #withdraw previous panel and create a new one using grid. anchor dialog boxes to root, if user hits quit both panels gets destroyed 
    root.withdraw()
    options = tk.Tk()
    options.title("Bag")
    #newbag
    newBag = Button(options,text="Make a new bag",font = ("Times",15),command=makeNewBag)
    newBag.grid(row = 0, column = 1, sticky = W, pady = 20)
    #switch for popups
    onOff = Button(options,text="Turn on/off popups",font=("Times",15),command=popups)
    onOff.grid(row = 1, column = 2, sticky = N)
    def q():
        options.destroy()
        root.destroy()
    #quit
    quit = Button(options,text="Quit",font = ("Times",15),command=q)
    quit.grid(row = 0, column = 2, sticky = E)
    #deletebag
    deleteb = Button(options,text="Delete a bag",font = ("Times",15),command=deleteBag)
    deleteb.grid(row = 1, column = 1, sticky = W, pady = 2)
    #add e to a bag
    adde = Button(options,text="Add an element to a bag",font = ("Times",15),command=addElement)
    adde.grid(row = 2, column = 1, sticky = W, pady = 20)
    #remove e from bag
    removePosition = Button(options,text="Remove an element from a bag",font = ("Times",15),command=removePos)
    removePosition.grid(row = 3, column = 1, sticky = W, pady = 2)
    #list
    listb = Button(options,text="List a bag",font = ("Times",15),command=listUser)
    listb.grid(row = 4, column = 1, sticky = W, pady = 20)
    #union
    union = Button(options,text="Combine 2 bags",font = ("Times",15),command=unionB)
    union.grid(row = 5, column = 1, sticky = W, pady = 2)
    #intersect
    intersect = Button(options,text="Intersect 2 bags",font = ("Times",15),command=intersectB)
    intersect.grid(row = 6, column = 1, sticky = W, pady = 20)
    #difference
    difference = Button(options,text="remove duplicates from 2 bags",font = ("Times",15),command=differenceB)
    difference.grid(row = 7, column = 1, sticky = W, pady = 2)    
    
    
    
    options.mainloop()

def rt():
    print()
    #set up root
    root.title("Bag")
    root.geometry('500x500')
    # add elements to page one
    head = Label(root, text="Welcome to the bag", font = ("Times", 50))
    head.pack()
    explain = Label(root,text="This application will simulate a shopping cart for you with multiple bags if needed",wraplength=300,font = ("Times",25))
    explain.place(relx=0.5, rely=0.5, anchor=CENTER)
    enter = Button(root,text="Enter Application",font = ("Times",15),fg='cyan',command=pageTwo)
    enter.place(relx=0.5, rely=0.8, anchor=CENTER)
    #end page one; page 2 is method pageTwo()

    root.mainloop()

rt()
# print(os.getcwd())
