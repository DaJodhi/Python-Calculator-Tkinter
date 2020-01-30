from tkinter import *
import tkinter.messagebox as box

root = Tk()

calculation = ""
root.geometry("400x450+570+220")
root.title("Calculator, by Jodhi")
root.resizable(False, False)
root.config(bg="black")

display = Label(root, width=57, height=5)


def update():
    global calculation
    display.configure(text=calculation)


def add_calc1():
    global calculation
    calculation += "1"
    update()


def add_calc2():
    global calculation
    calculation += "2"
    update()


def add_calc3():
    global calculation
    calculation += "3"
    update()


def add_calc4():
    global calculation
    calculation += "4"
    update()


def add_calc5():
    global calculation
    calculation += "5"
    update()


def add_calc6():
    global calculation
    calculation += "6"
    update()


def add_calc7():
    global calculation
    calculation += "7"
    update()


def add_calc8():
    global calculation
    calculation += "8"
    update()


def add_calc9():
    global calculation
    calculation += "9"
    update()


def add_calc0():
    global calculation
    calculation += "0"
    update()


def add():
    global calculation
    calculation += "+"
    update()


def minus():
    global calculation
    calculation += "-"
    update()


def divide():
    global calculation
    calculation += "/"
    update()


def mult():
    global calculation
    calculation += "*"
    update()


def brackets():
    global calculation
    if calculation.count("(") == calculation.count(")") + 1:
        calculation += ")"
    elif calculation.count(")") == calculation.count("(") + 1:
        calculation += "("
    update()


def backspace():
    global calculation
    calculation = calculation[:-1]
    update()


def equal():
    global calculation
    try:
        if len(calculation) > 57:
            file = open("result.txt", "a+")
            calculation = str(eval(calculation))
            if calculation.endswith(".0"):
                calculation = calculation[:-2]
            file.write(calculation + "\n \n")
            file.close()
        if calculation.endswith(".0"):
            calculation = calculation[:-2]
        update()
    except ZeroDivisionError:
        box.showerror("Zero Division Error", "Cookie monster.")
    except SyntaxError:
        box.showerror("Error", "You did something wrong.")
    except OverflowError:
        box.showerror("Overflow Error", "That's too small man.")


def clear():
    global calculation
    calculation = ""
    update()


def dot():
    global calculation
    if calculation[:-1] == ".":
        calculation += ""
    else:
        calculation += "."
    update()


def xy():
    global calculation
    calculation += "**"
    update()


buttonFrame = Frame(root)


num1 = Button(buttonFrame, text="1", command=add_calc1, fg="white", bg="gray", width=9, height=4)
num2 = Button(buttonFrame, text="2", command=add_calc2, fg="white", bg="gray", width=9, height=4)
num3 = Button(buttonFrame, text="3", command=add_calc3, fg="white", bg="gray", width=9, height=4)
num4 = Button(buttonFrame, text="4", command=add_calc4, fg="white", bg="gray", width=9, height=4)
num5 = Button(buttonFrame, text="5", command=add_calc5, fg="white", bg="gray", width=9, height=4)
num6 = Button(buttonFrame, text="6", command=add_calc6, fg="white", bg="gray", width=9, height=4)
num7 = Button(buttonFrame, text="7", command=add_calc7, fg="white", bg="gray", width=9, height=4)
num8 = Button(buttonFrame, text="8", command=add_calc8, fg="white", bg="gray", width=9, height=4)
num9 = Button(buttonFrame, text="9", command=add_calc9, fg="white", bg="gray", width=9, height=4)
num0 = Button(buttonFrame, text="0", command=add_calc0, fg="white", bg="gray", width=9, height=4)

add = Button(buttonFrame, text="+", command=add, fg="black", bg="gray", width=9, height=4)
minus = Button(buttonFrame, text="-", command=minus, fg="black", bg="gray", width=9, height=4)
divide = Button(buttonFrame, text=" ÷ ", command=divide, fg="black", bg="gray", width=9, height=4)
mult = Button(buttonFrame, text=" × ", command=mult, fg="black", bg="gray", width=9, height=4)
back = Button(buttonFrame, text=" <-", command=backspace, fg="black", bg="gray", width=9, height=4)

equals = Button(buttonFrame, text=" = ", fg="black", bg="red", command=equal, width=9, height=4)

brackets_button = Button(buttonFrame, text="()", command=brackets, width=9, height=4, fg="black", bg="gray")
dot_button = Button(buttonFrame, text=".", command=dot, fg="white", bg="gray", width=9, height=4)
clear_button = Button(buttonFrame, text="C", command=clear, fg="red", bg="gray", width=9, height=4)
xy_button = Button(buttonFrame, text="xª", command=xy, fg="black", bg="gray", width=9, height=4)

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
