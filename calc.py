from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def buttonAdd(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def buttonClear():
    e.delete(0, END)
    
def add():
    firstNum = e.get()
    global fNum 
    global math
    math = "addition"
    fNum = int(firstNum)
    e.delete(0, END)
    
def subtract():
    firstNum = e.get()
    global fNum 
    global math
    math = "subtraction"
    fNum = int(firstNum)
    e.delete(0, END)

def multiply():
    firstNum = e.get()
    global fNum 
    global math
    math = "multiplication"
    fNum = int(firstNum)
    e.delete(0, END)

def divide():
    firstNum = e.get()
    global fNum 
    global math
    math = "division"
    fNum = int(firstNum)
    e.delete(0, END)


def buttonEqual():
    secondNum = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, fNum + int(secondNum))
    if math == "subtraction":
        e.insert(0, fNum - int(secondNum))
    if math == "multiplication":
        e.insert(0, fNum * int(secondNum))
    if math == "division":
        e.insert(0, fNum / int(secondNum))
    
button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: buttonAdd(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: buttonAdd(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: buttonAdd(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: buttonAdd(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: buttonAdd(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: buttonAdd(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: buttonAdd(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: buttonAdd(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: buttonAdd(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: buttonAdd(0))
addButton = Button(root, text ="+", padx = 39, pady = 20, command = add)
subButton = Button(root, text ="-", padx = 41, pady = 20, command = subtract)
multiButton = Button(root, text ="*", padx = 40, pady = 20, command = multiply)
divButton = Button(root, text ="/", padx = 41, pady = 20, command = divide)
equalsButton = Button(root, text ="=", padx = 91, pady = 20, command = buttonEqual)
clearButton = Button(root, text = "Clear", padx = 79, pady = 20, command = buttonClear)

button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)
button0.grid(row = 4, column = 0)
addButton.grid(row = 5, column = 0)
subButton.grid(row = 6, column = 0)
multiButton.grid(row = 6, column = 1)
divButton.grid(row = 6, column = 2)
equalsButton.grid(row = 5, column = 1, columnspan = 2)
clearButton.grid(row = 4, column = 1, columnspan = 2 )


root.mainloop()