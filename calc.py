from tkinter import *

root = Tk(screenName="Calculator",
          baseName="calculator", className='Tk', useTk=1)
root.title("Calculator")

numbers = "123456789"
extra = "+-x÷"
value = 0
result = Entry()
result.pack()
result.insert(0, value)

result.get()
numbersFrame = Frame()
extrasFrame = Frame()
for each in numbers:
    button = Button(root,  width=5,
        height=5,
        bg="black",
        fg="white", 
        text=each,
        relief=RAISED,
        master = numbersFrame
        # command=on_button_click
    )
    button.pack()
numbersFrame.pack()
extrasFrame.pack(side=RIGHT)

# Run the Tkinter event loop
root.mainloop()
