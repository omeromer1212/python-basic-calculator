from tkinter import *
from tkinter import messagebox
screen = Tk()
screen.geometry("300x200")
screen.title("Calculator")
operation = ""
firstnumberentry = Entry(font="Helvetica 14")
firstnumberentry.place(x=0,y=10)
selectoperationlabel = Label(font="Helvetica 16")
selectoperationlabel.place(x=0,y=40)
secondnumberentry = Entry(font="Helvetica 14")
secondnumberentry.place(x=0,y=80)
def plusBtnCOMMAND():
    firstnumber = int(firstnumberentry.get())
    secondnumber = int(secondnumberentry.get())
    global number
    number = firstnumber + secondnumber
    selectoperationlabel["text"] = "+"
def minusBtnCOMMAND():
    firstnumber = int(firstnumberentry.get())
    secondnumber = int(secondnumberentry.get())
    global number
    number = firstnumber - secondnumber
    selectoperationlabel["text"] = "-"
def multiplyBtnCOMMAND():
    firstnumber = int(firstnumberentry.get())
    secondnumber = int(secondnumberentry.get())
    global number
    number = firstnumber * secondnumber
    selectoperationlabel["text"] = "x"
def divideBtnCOMMAND():
    firstnumber = int(firstnumberentry.get())
    secondnumber = int(secondnumberentry.get())
    global number
    number = firstnumber / secondnumber
    selectoperationlabel["text"] = "/"
plusBtn = Button(text="+",font="Helvetica 14",command=plusBtnCOMMAND)
plusBtn.place(x=0,y=160)
minusBtn = Button(text="-",font="Helvetica 15",command=minusBtnCOMMAND)
minusBtn.place(x=30,y=160)
multiplyBtn = Button(text="x",font="Helvetica 14",command=multiplyBtnCOMMAND)
multiplyBtn.place(x=55,y=160)
divideBtn = Button(text="/",font="Helvetica 14",command=divideBtnCOMMAND)
divideBtn.place(x=85,y=160)
def resultShow():
    messagebox.showinfo("Result",f"Result is {str(number)} \n(Select the desired option again after changing any number to result to be correct if result is wrong)")
    if selectoperationlabel["text"] == "/" and int(firstnumberentry.get()) == 1 and int(secondnumberentry.get()) == 0:
        messagebox.showerror("Error","Cannot divide by zero")
calculatorResultShow = Button(text="Calculate!",font="Helvetica 14",command=resultShow)
calculatorResultShow.place(x=110,y=160)
screen.mainloop()