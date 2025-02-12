from tkinter import *
import tkinter.font as font
import re
numberpattern = r"^[-]?[0-9]+$"
methods = ["+", "-", "×", "÷"]
def parse_equation():
    global array, maxValue, numberpattern
    result = int(array[0])
    i = 1
    if (array[1] in methods):
        match array[i]:
            case "+":
                result += int(array[2])
            case "-":
                result -= int(array[2])
            case "×":
                result *= int(array[2])
            case "÷":
                result /= int(array[2])
                if result.is_integer():
                    result = int(result)
        i += 2
    if result > int(maxValue):
        return "ERROR"
    else:
        string_result = str(result)
        if (len(string_result) > len(maxValue)):
            string_result = string_result[0:len(maxValue)]
        return string_result
root = Tk(screenName="Calculator", baseName="calculator", className='Tk', useTk=1)
root.resizable(False, False)

screen_height = root.winfo_screenheight() - 200
width = 800
size = screen_height //10
box_height = (screen_height) //5 
custom_font = font.Font(family="Arial", size=size)

root.geometry(f"{width}x{screen_height}")
root.title("Calculator")

for i in range(5):
    root.rowconfigure(i, weight=3)
for j in range(4):
    root.columnconfigure(j, weight=1)

maxValue= "999999999999"
value = "0"
prev = [None, None]
changed = False
result_label = Label(root, text=value, font=custom_font, bg="red", height=2)
result_label.grid(row=0, column=0, columnspan=4, padx=5, sticky="e")
array = []
def on_number_click(id):
    global value, maxValue, changed
    if (len(value) >= len(maxValue)):
        return
    if(changed == False):
        value = id
        changed = True
    else:
        value += id
    result_label.config(text=value)
numbersFrame = Frame(root, bg="blue")
numbersFrame.grid(row=1, rowspan=4, column=0, columnspan=4)
for box in range(5): 
    numbersFrame.rowconfigure(box, weight=1)
    numbersFrame.columnconfigure(box, weight=1)

for a in range(9):
    button = Button(numbersFrame, bg="black", fg="white", text=a+1, relief=RAISED, font=custom_font, width=box_height)
    button.grid(row=a//3, column=a%3, padx=5, pady=5)
    button.bind("<Button-1>",  lambda event, value=str(a+1): on_number_click(value))

extra = [0, ".", "+/-"]
def add_decimal():
    global value
    value += "."
    result_label.config(text=value)
def invert_sign():
    global value
    value = "-" + value if value[0].isdigit() else value[1:]
    changed = True
    result_label.config(text=value)
for b in range(3):
    button = Button(numbersFrame, bg="black", fg="white", text=extra[b], relief=RAISED, font=custom_font, width=box_height)
    button.grid(row=3, column=b, padx=5, pady=5)
    if (extra[b] == 0):
        button.bind("<Button-1>", lambda event: on_number_click("0"))
    if (extra[b] == "."):
        button.bind("<Button-1>", lambda event: add_decimal())
    if (extra[b] == "+/-"):
        button.bind("<Button-1>", lambda event: invert_sign())
for c in range(4):
    numbersFrame.rowconfigure(c, weight=1)

def on_method_click(id):
    global value, array, methods, prev, changed
    print(array)
    if not array or array[-1] in methods:
        if changed == True:
            array.append(value)
            prev[0] = value 
            value = "0"
            changed = False
        if (len(array) == 3):
            on_equal()
    if array[-1] not in methods:
        if len(array) == 1:
            array.append(id)
            prev[1] = id
        if len(array) == 3:
            value = parse_equation()
            array = [str(value)]
            changed = False
            result_label.config(text=value)
            array.append(id)
            prev[1] = id
for c in range(4):
    button = Button(numbersFrame, bg="blue", fg="white", text=methods[c], relief=RAISED, font=custom_font, width=box_height)
    button.grid(row=c, column=3, padx=5, pady=5)
    button.bind("<Button-1>", lambda event, value=c: on_method_click(methods[value]))
big = ["A/C","="]
def on_clear():
    global value, array, changed
    value = "0"
    array = []
    prev = [None, None]
    changed = False
    result_label.config(text=value)
def on_equal():
    global value, array, changed, prev
    print(array)
    if len(array) < 1:
        return
    if len(array) == 1 and prev[0] and prev[1]:
        array.append(prev[1])
        array.append(prev[0])
        value = parse_equation()
        array = [str(value)]
        # print(" this happened ")
        changed = False
        result_label.config(text=value)
        return
    if len(array) == 2:
        array.append(value)
        prev[0] = value
        value = parse_equation()
        array = [str(value)]
        # print(" this happened ")
        changed = False
        result_label.config(text=value)
for d in range(2):
    button = Button(numbersFrame, bg="blue", fg="white", text=big[d], relief=RAISED, font=custom_font, width=box_height)
    button.grid(row=d*2, column=4, rowspan=2, padx=5, pady=5)
    if (big[d] == "A/C"):
        button.bind("<Button-1>", lambda event: on_clear())
    if (big[d] == "="):
        button.bind("<Button-1>", lambda event: on_equal())



root.mainloop()
