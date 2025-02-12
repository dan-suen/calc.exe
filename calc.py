from tkinter import *
import tkinter.font as font

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

maxValue= 999999999999
value = 0
result_label = Label(root, text=value, font=custom_font, bg="red", height=2)
result_label.grid(row=0, column=0, columnspan=4, padx=5, sticky="e")


numbersFrame = Frame(root, bg="blue")
numbersFrame.grid(row=1, rowspan=4, column=0, columnspan=4)
for box in range(5): 
    numbersFrame.rowconfigure(box, weight=1)
    numbersFrame.columnconfigure(box, weight=1)

for a in range(9):
    button = Button(numbersFrame, bg="black", fg="white", text=a+1, relief=RAISED, font=custom_font, width=box_height)
    button.grid(row=a//3, column=a%3, padx=5, pady=5)

extras = [0, ".", "+/-"]
for b in range(3):
    button = Button(numbersFrame, bg="black", fg="white", text=extras[b], relief=RAISED, font=custom_font, width=box_height)
    button.grid(row=3, column=b, padx=5, pady=5)

for c in range(4):
    numbersFrame.rowconfigure(c, weight=1)

methods = ["+", "-", "×", "÷"]
for c in range(4):
    button = Button(numbersFrame, bg="blue", fg="white", text=methods[c], relief=RAISED, font=custom_font, width=box_height)
    button.grid(row=c, column=3, padx=5, pady=5)
big = ["A/C","="]
for d in range(2):
    button = Button(numbersFrame, bg="blue", fg="white", text=big[d], relief=RAISED, font=custom_font, width=box_height)
    button.grid(row=d*2, column=4, rowspan=2, padx=5, pady=5)


root.mainloop()
