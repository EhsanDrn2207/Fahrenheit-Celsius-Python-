import tkinter as tk
from tkinter import ttk

# F = (1.8*c) + 32

root = tk.Tk()

result_var = tk.StringVar()
#creating label for celsius
celsius_lbl = tk.Label(
    master=root,
    text= 'Celsius: ',
    width=15,
    height=3,
    fg='green',
)
#creating label for fahrenheit
fahrenheit_lbl = tk.Label(
    master=root,
    text='Fahrenheit: ',
    width=15,
    height=3,
    fg='green', 
)
#griding our lebals
celsius_lbl.grid(row=0, column=0)
fahrenheit_lbl.grid(row=1, column=0)
#creating an entry for celsius
celsius_ent = tk.Entry(
    master=root,
    width=60,
    fg='blue',
)
#gridig our entry
celsius_ent.grid(row=0, column=1)
#a empty space
space_lbl = tk.Label(
    master=root,
    text='  ',
)
space_lbl.grid(row=0, column=2)

def cels_to_fahren(*args):
    
    result_var = celsius_ent.get()
    try:
        answer = float(result_var)
        answer = (1.8 * answer) + 32
        result_lbl['text'] = str(answer)
    except:
        if result_var != '':
            result_lbl['text'] = ('You should enter a number.')
        else:
            result_lbl['text'] = ('Input is empty....')

#procces button for calculing
procces_btn = ttk.Button(
    master=root,
    width=10,
    text='Calc',
    command=cels_to_fahren,
)
#griding calculation button
procces_btn.grid(row=0, column=3, sticky=('e'))
root.bind('<Return>', cels_to_fahren)

result_lbl = tk.Label(
    master=root,
    text='000',
    fg='red',
    width=60,
    height=3,
)

quit_btn = ttk.Button(
    master=root,
    text='Quit',
    width=10,
    command=quit
)

quit_btn.grid(row=1, column=3, sticky='e')
root.bind('q', quit)

result_lbl.grid(row=1, column=1)
root.mainloop()