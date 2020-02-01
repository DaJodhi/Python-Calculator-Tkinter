from tkinter import *
import tkinter.messagebox as box
from functools import partial

# Version 2, The Speed and Docs Update

root = Tk()

calculation = ""
root.geometry("400x450")
root.title("Calculator 2.0, by Jodhi")
root.resizable(False, False)
root.config(bg="black")

# This widget will show the calculation
display = Label(root, width=57, height=5)


# Updates the display every time the calculation  is done
def update():
    global calculation
    display.configure(text=calculation)


# template command for simple buttons
def add_char(x):
    global calculation
    calculation += x
    update()


def brackets():
    global calculation
    if calculation.count("(") == calculation.count(")") + 1:
        calculation += ")"
    else:
        calculation += "("
    update()


# Removes the last character from the display
def backspace():
    global calculation
    calculation = calculation[:-1]
    update()


# Simply clears the calculator display
def clear():
    global calculation
    calculation = ""
    update()


def equal():
    global calculation
    try:
        calculation = str(eval(calculation))
        if calculation.endswith(".0"):
            calculation = calculation[:-2]
        # if the result is too big for the calculator display, it saves the result in a text file and clears the calculator display
        if len(calculation) > 57:
            file = open("result.txt", "a+")
            file.write(calculation + "\n \n")
            clear()
            box.showinfo("Saved Result", "The result of your calculation was saved in 'result.txt' and the calculator display was cleared.")
            file.close()
        update()
    except ZeroDivisionError:
        box.showerror("Zero Division Error", "Cookie monster.")
    except SyntaxError:
        box.showerror("Error", "You did something wrong.")
    except OverflowError:
        box.showerror("Overflow Error", "That's too small man.")
    # This error was encountered when doing something like this: 2(3+4)
    except TypeError:
        box.showerror("Type Error", "We don't do algebra here.")


def dot():
    global calculation
    if calculation[:-1] != ".":
        calculation += "."
        update()


buttonFrame = Frame(root)

# The following buttons can be held down
num1 = Button(buttonFrame, text="1", command=partial(add_char, "1"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num2 = Button(buttonFrame, text="2", command=partial(add_char, "2"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num3 = Button(buttonFrame, text="3", command=partial(add_char, "3"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num4 = Button(buttonFrame, text="4", command=partial(add_char, "4"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num5 = Button(buttonFrame, text="5", command=partial(add_char, "5"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num6 = Button(buttonFrame, text="6", command=partial(add_char, "6"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num7 = Button(buttonFrame, text="7", command=partial(add_char, "7"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num8 = Button(buttonFrame, text="8", command=partial(add_char, "8"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num9 = Button(buttonFrame, text="9", command=partial(add_char, "9"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
num0 = Button(buttonFrame, text="0", command=partial(add_char, "0"), fg="white", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
back = Button(buttonFrame, text=" <-", command=backspace, fg="black", bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)

add = Button(buttonFrame, text="+", command=partial(add_char, "+"), fg="black", bg="gray", width=9, height=4)
minus = Button(buttonFrame, text="-", command=partial(add_char, "-"), fg="black", bg="gray", width=9, height=4)
divide = Button(buttonFrame, text=" ÷ ", command=partial(add_char, "/"), fg="black", bg="gray", width=9, height=4)
mult = Button(buttonFrame, text=" × ", command=partial(add_char, "*"), fg="black", bg="gray", width=9, height=4)
equals = Button(buttonFrame, text=" = ", fg="black", bg="red", command=equal, width=9, height=4)

xy_button = Button(buttonFrame, text="xª", command=partial(add_char, "**"), fg="black", bg="gray", width=9, height=4)
brackets_button = Button(buttonFrame, text="()", command=brackets, width=9, height=4, fg="black", bg="gray")
dot_button = Button(buttonFrame, text=".", command=dot, fg="white", bg="gray", width=9, height=4)
clear_button = Button(buttonFrame, text="C", command=clear, fg="red", bg="gray", width=9, height=4)

clear_button.grid(row=1, column=1)
brackets_button.grid(row=1, column=2)
xy_button.grid(row=1, column=3)
divide.grid(row=1, column=4)
num7.grid(row=2, column=1)
num8.grid(row=2, column=2)
num9.grid(row=2, column=3)
mult.grid(row=2, column=4)
num4.grid(row=3, column=1)
num5.grid(row=3, column=2)
num6.grid(row=3, column=3)
minus.grid(row=3, column=4)
num1.grid(row=4, column=1)
num2.grid(row=4, column=2)
num3.grid(row=4, column=3)
add.grid(row=4, column=4)
back.grid(row=5, column=1)
num0.grid(row=5, column=2)
dot_button.grid(row=5, column=3)
equals.grid(row=5, column=4)

display.pack()
buttonFrame.pack()

root.mainloop()
