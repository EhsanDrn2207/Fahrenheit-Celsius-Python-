import tkinter as tk
from tkinter import ttk
from tkinter import E, W

root = tk.Tk()
root.title('This is my app')

result = tk.StringVar()
# c = (f - 32) / 1.8
fahrenheit_label = tk.Label(
    master= root,
    text= 'Fahrenheit:',
    width= 10,
    height= 3,
    border= 1,
).grid(row=0, column=0, sticky=(W,))

celsius_label = tk.Label(
    master= root,
    text= 'Celsius',
    width= 10,
    border= 1,
).grid(row=1, column=0, sticky=(W,))

space_label = tk.Label(
    root,
    text="      "
).grid(row=0, column=2)

tempt = ttk.Entry(
    master= root,
    width= 70,
)

space_label = tk.Label(
    root,
    text="      "
).grid(row=0, column=4)

celsius_show = tk.Label(
    master= root,
    width= 20,
)

def calc(*args):
    result = tempt.get()
    try:
        result = float(result)
        result = (result - 32) / 1.8
        celsius_show['text'] = result
        
    except ValueError:
        if result != '':
            celsius_show['text'] = ('You should enter a number.')
        else:
            celsius_show['text'] = ('Input is empty....')

root.bind('<Return>', calc)          
    
calc_button = tk.Button(
    master= root,
    text= "Calc",
    border= 5,
    borderwidth= 2,
    padx= 20,
    fg = 'blue',
    command= calc,
).grid(row=0, column=5)

quit_button = tk.Button(
    master= root,
    text= 'Quit',
    fg= 'red',
    padx= 20,
    command= quit
).grid(row=1, column=5)

tempt.grid(row=0, column=3)
celsius_show.grid(row=1, column=3)

root.mainloop()