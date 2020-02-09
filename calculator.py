"""A simple calculator made in Tkinter."""
from functools import partial
from tkinter import Label, Tk, Button, Frame, messagebox

# Version 2.1, The Speed and Docs Update

ROOT = Tk()

ROOT.geometry("400x450")
ROOT.title("Calculator 2.0, by Jodhi")
ROOT.resizable(False, False)
ROOT.config(bg="black")


DISPLAY = Label(ROOT, width=57, height=5)


class Calculator:
    """A class is used so that we do not have to use a global statement in each function."""

    calculation = ""

    @classmethod
    def update(cls):
        """Update the calculator display."""
        DISPLAY.configure(text=cls.calculation)

    @classmethod
    def add_char(cls, char):
        """Template command for simple buttons."""
        cls.calculation += char
        cls.update()

    @classmethod
    def brackets(cls):
        """Add brackets."""
        if cls.calculation.count("(") == cls.calculation.count(")") + 1:
            cls.calculation += ")"
        else:
            cls.calculation += "("
        cls.update()

    @classmethod
    def backspace(cls):
        """Remove the last character from the display."""
        cls.calculation = cls.calculation[:-1]
        cls.update()

    @classmethod
    def clear(cls):
        """Clear the calculator display."""
        cls.calculation = ""
        cls.update()

    @classmethod
    def equal(cls):
        """Evaluate the answer to the calculation.

        If the answer is larger than 57 digits, it is saved to a results file
        Any trailing .0 is removed from simple divisions
        """
        try:
            cls.calculation = str(eval(cls.calculation))
            if cls.calculation.endswith(".0"):
                cls.calculation = cls.calculation[:-2]
            if len(cls.calculation) > 57:
                file = open("result.txt", "a+")
                file.write(cls.calculation + "\n \n")
                cls.clear()
                messagebox.showinfo("Saved Result", "The result was saved in 'result.txt' and the"
                                                    " calculator display was cleared.")
                file.close()
            cls.update()
        except ZeroDivisionError:
            messagebox.showerror("Zero Division Error", "Cookie monster.")
        except SyntaxError:
            messagebox.showerror("Error", "You did something wrong.")
        except OverflowError:
            messagebox.showerror("Overflow Error", "That's too small man.")
        except TypeError:
            messagebox.showerror("Type Error", "We don't do algebra here.")

    @classmethod
    def dot(cls):
        """Add a decimal point."""
        if cls.calculation[:-1] != ".":
            cls.calculation += "."
            cls.update()


BUTTON_FRAME = Frame(ROOT)

# The following buttons can be held down
NUM1 = Button(BUTTON_FRAME, text="1", command=partial(Calculator.add_char, "1"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM2 = Button(BUTTON_FRAME, text="2", command=partial(Calculator.add_char, "2"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM3 = Button(BUTTON_FRAME, text="3", command=partial(Calculator.add_char, "3"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM4 = Button(BUTTON_FRAME, text="4", command=partial(Calculator.add_char, "4"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM5 = Button(BUTTON_FRAME, text="5", command=partial(Calculator.add_char, "5"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM6 = Button(BUTTON_FRAME, text="6", command=partial(Calculator.add_char, "6"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM7 = Button(BUTTON_FRAME, text="7", command=partial(Calculator.add_char, "7"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM8 = Button(BUTTON_FRAME, text="8", command=partial(Calculator.add_char, "8"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM9 = Button(BUTTON_FRAME, text="9", command=partial(Calculator.add_char, "9"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
NUM0 = Button(BUTTON_FRAME, text="0", command=partial(Calculator.add_char, "0"), fg="white",
              bg="gray", width=9, height=4, repeatdelay=100, repeatinterval=100)
BACK = Button(BUTTON_FRAME, text=" <-", command=Calculator.backspace, fg="black", bg="gray",
              width=9, height=4, repeatdelay=100, repeatinterval=100)

ADD = Button(BUTTON_FRAME, text="+", command=partial(Calculator.add_char, "+"), fg="black",
             bg="gray", width=9, height=4)
MINUS = Button(BUTTON_FRAME, text="-", command=partial(Calculator.add_char, "-"), fg="black",
               bg="gray", width=9, height=4)
DIVIDE = Button(BUTTON_FRAME, text=" ÷ ", command=partial(Calculator.add_char, "/"), fg="black",
                bg="gray", width=9, height=4)
MULT = Button(BUTTON_FRAME, text=" × ", command=partial(Calculator.add_char, "*"), fg="black",
              bg="gray", width=9, height=4)
EQUALS = Button(BUTTON_FRAME, text=" = ", fg="black", bg="red", command=Calculator.equal,
                width=9, height=4)

XY_BUTTON = Button(BUTTON_FRAME, text="xª", command=partial(Calculator.add_char, "**"),
                   fg="black", bg="gray", width=9, height=4)
BRACKETS_BUTTON = Button(BUTTON_FRAME, text="()", command=Calculator.brackets,
                         width=9, height=4, fg="black", bg="gray")
DOT_BUTTON = Button(BUTTON_FRAME, text=".", command=Calculator.dot, fg="white", bg="gray",
                    width=9, height=4)
CLEAR_BUTTON = Button(BUTTON_FRAME, text="C", command=Calculator.clear, fg="red", bg="gray",
                      width=9, height=4)

CLEAR_BUTTON.grid(row=1, column=1)
BRACKETS_BUTTON.grid(row=1, column=2)
XY_BUTTON.grid(row=1, column=3)
DIVIDE.grid(row=1, column=4)
NUM7.grid(row=2, column=1)
NUM8.grid(row=2, column=2)
NUM9.grid(row=2, column=3)
MULT.grid(row=2, column=4)
NUM4.grid(row=3, column=1)
NUM5.grid(row=3, column=2)
NUM6.grid(row=3, column=3)
MINUS.grid(row=3, column=4)
NUM1.grid(row=4, column=1)
NUM2.grid(row=4, column=2)
NUM3.grid(row=4, column=3)
ADD.grid(row=4, column=4)
BACK.grid(row=5, column=1)
NUM0.grid(row=5, column=2)
DOT_BUTTON.grid(row=5, column=3)
EQUALS.grid(row=5, column=4)

DISPLAY.pack()
BUTTON_FRAME.pack()

ROOT.mainloop()
