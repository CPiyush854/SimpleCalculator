from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg = "white", borderwidth = 10)
e.pack()
e.insert(0, "Enter your name")

def myClick():
    myLabel = Label(root, text = e.get())
    myLabel.pack()
    
myButton = Button(root, text = "Enter your name", command = myClick, fg="red", bg= "green")
myButton.pack()


root.mainloop()