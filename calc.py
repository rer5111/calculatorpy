from tkinter import *
from tkinter import ttk
import math

def calculate(num):
    global output, buffer, nums, ops, calculation
    outputbuffer = ""
    if num == "C":  # there is nothing
        buffer = ""
        nums = []
        ops = []
    elif num == "CE":   # there is no buffer
        buffer = ""
    elif num == "del":
        buffer = str(buffer)[:-1]    # i actually used the knowledge i gained (yes strings are just fancy lists)
    elif num in ["%", "/x", "√", "^2", "+/-"]:  # these operators instantly perform actions
        if buffer == "":
            buffer = 0
        if num == "%":
            buffer = float(buffer)/100
        elif num == "/x":
            try:
                buffer = 1/float(buffer)
            except ZeroDivisionError:
                outputbuffer = "Cannot divide by 0"
                buffer = ""
        elif num == "√":
            buffer = math.sqrt(float(buffer))
        elif num == "^2":
            buffer = float(buffer)**2
        elif num == "+/-":
            buffer = float(buffer)*-1
    elif num in ["*", "-", "+", "/"]:    # these operators need a second number to perfom an action
        if buffer != "":
            if not float(buffer) % 1:   # me when the 5.0 is actually just 5
                buffer = float(buffer)
                buffer = int(buffer)
            nums.append(buffer)
            ops.append(num)
            buffer = ""

    elif num != "=": # ALMOST everything else
        if str(buffer) == "" and num == ".":
            buffer = "0"
        buffer = str(buffer) + str(num)
        if buffer == "00":
            buffer = "0"
    else: # yeah its calculation time
        if buffer != "":
            if not float(buffer) % 1:   # me when I've written this code 15 lines ago
                buffer = float(buffer)
                buffer = int(buffer)
            nums.append(buffer)
            buffer = ""
            calculation = ""
            for i, n in enumerate(nums):
                if i <= len(ops)-1:
                    calculation += str(n) + ops[i]
                else:
                    calculation += str(n)
            ops = []
            nums = []
            buffer = "buffer=" + calculation
            local_vars = locals()
            try:
                exec(buffer, globals(), local_vars) # this code is absolutely horrible and you should never do this
                buffer = local_vars["buffer"]
            except ZeroDivisionError:
                outputbuffer = "Cannot divide by 0"
                buffer = ""
    try:
        if float(buffer) % 1 == 0:  # haha you're an integer now
            buffer = int(buffer)
    except ValueError:
        pass
    for i, numm in enumerate(nums): # enumerate is so cool and i even got to use it
        outputbuffer += str(numm)
        outputbuffer += ops[i]
    output["text"] = outputbuffer + str(buffer)

buffer = ""
nums = []
ops = []

screen = Tk(className="Calculator")
screen.geometry("400x330")
frm = ttk.Frame(screen, padding=10)
frm.grid(row=1)
output = ttk.Label(screen, border=0, padding=10, text="")
output.grid(column=0, row=0)

ttk.Button(frm, text="%", command=lambda: calculate("%"), padding=10).grid(column=0, row=1)
ttk.Button(frm, text="C", command=lambda: calculate("C"), padding=10).grid(column=1, row=1)
ttk.Button(frm, text="CE", command=lambda: calculate("CE"), padding=10).grid(column=2, row=1)
ttk.Button(frm, text="del", command=lambda: calculate("del"), padding=10).grid(column=3, row=1)
ttk.Button(frm, text="1/x", command=lambda: calculate("/x"), padding=10).grid(column=0, row=2)
ttk.Button(frm, text="x^2", command=lambda: calculate("^2"), padding=10).grid(column=1, row=2)
ttk.Button(frm, text="2√x", command=lambda: calculate("√"), padding=10).grid(column=2, row=2)
ttk.Button(frm, text="/", command=lambda: calculate("/"), padding=10).grid(column=3, row=2)
ttk.Button(frm, text="1", command=lambda: calculate(1), padding=10).grid(column=0, row=3)
ttk.Button(frm, text="2", command=lambda: calculate(2), padding=10).grid(column=1, row=3)
ttk.Button(frm, text="3", command=lambda: calculate(3), padding=10).grid(column=2, row=3)
ttk.Button(frm, text="x", command=lambda: calculate("*"), padding=10).grid(column=3, row=3)
ttk.Button(frm, text="4", command=lambda: calculate(4), padding=10).grid(column=0, row=4)
ttk.Button(frm, text="5", command=lambda: calculate(5), padding=10).grid(column=1, row=4)
ttk.Button(frm, text="6", command=lambda: calculate(6), padding=10).grid(column=2, row=4)
ttk.Button(frm, text="-", command=lambda: calculate("-"), padding=10).grid(column=3, row=4)
ttk.Button(frm, text="7", command=lambda: calculate(7), padding=10).grid(column=0, row=5)
ttk.Button(frm, text="8", command=lambda: calculate(8), padding=10).grid(column=1, row=5)
ttk.Button(frm, text="9", command=lambda: calculate(9), padding=10).grid(column=2, row=5)
ttk.Button(frm, text="+", command=lambda: calculate("+"), padding=10).grid(column=3, row=5)
ttk.Button(frm, text="+/-", command=lambda: calculate("+/-"), padding=10).grid(column=0, row=6)
ttk.Button(frm, text="0", command=lambda: calculate(0), padding=10).grid(column=1, row=6)
ttk.Button(frm, text=".", command=lambda: calculate("."), padding=10).grid(column=2, row=6)
ttk.Button(frm, text="=", command=lambda: calculate("="), padding=10).grid(column=3, row=6)
screen.mainloop()