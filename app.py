## tkinter documentation ...


import tkinter


def calculate():
    num1 = int(entry1.get())

    operator = entry2.get()

    num2 = int(entry3.get())

    if operator == "+":

        calc = num1 + num2

    elif operator == "-":

        calc = num1 - num2

    elif operator == "*":

        calc = num1 * num2

    elif operator == "/":

        calc = num1 / num2

    else:

        calc = "Error"

    label.config(text=str(calc))


## create empty window

screen = tkinter.Tk()

screen.geometry("600x100")

screen.config(padx=20, pady=20)

## create input

entry1 = tkinter.Entry()

entry1.config(width=20, font=("default", 20))

entry1.grid(row=0, column=0, padx=5)

entry2 = tkinter.Entry()

entry2.config(width=20)

entry2.grid(row=0, column=1, padx=5)

entry3 = tkinter.Entry()

entry3.config(width=20)

entry3.grid(row=0, column=2, padx=5)

## create button | command => sho funkcija da izvrsi

button = tkinter.Button(text="Calculate", command=calculate)

button.grid(row=0, column=3)

## create label

label = tkinter.Label(text="0")

label.grid(row=1, column=0)

screen.mainloop()