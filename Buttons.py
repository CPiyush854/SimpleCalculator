from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look I clicked the button!")
    myLabel.pack()
    
myButton = Button(root, text = "Click Me!", command = myClick, fg="red", bg= "green")
myButton.pack()


root.mainloop()