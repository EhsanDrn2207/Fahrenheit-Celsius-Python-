import tkinter as tk
from tkinter import ttk

#crating our root
window = tk.Tk()
#changing our title
window.title('Ehsan.D')

#crating a varition for entry's text
fahrenheit_var = tk.StringVar()

#crating a label for showing the result of operation
lbl_result = tk.Label(
    master= window,
    text= 'Enter your number',
)

#Converting farhenheit to celsius
def convert_farhenheit_to_celsius(*args):
    fahrenheit_input = fahrenheit_var.get()       
    try:
        fahrenheit_value = float(fahrenheit_input)
        lbl_result['text'] = (fahrenheit_value - 32) / 1.8
    except ValueError:
        if fahrenheit_input == '':
            lbl_result['text'] = "Input is empty..."
        else:
            lbl_result['text'] = "You should enter a number."

#Implementing function with Enter
window.bind('<Return>', convert_farhenheit_to_celsius)          

#creating fahrenheit label
lbl_fahrenhiet = tk.Label( # label
    master=window,
    text= 'Fahrenheit:'
)

#creating entry for temperature
ent_fahrenhiet = ttk.Entry( # Entery
    master= window,
    width= 50,
    textvariable= fahrenheit_var,
)

#creating calcution button
btn_calc = ttk.Button( # button
    master= window,
    text= 'Calc',
    command= convert_farhenheit_to_celsius, # Executing the function
)


lbl_fahrenhiet.grid(row=0, column=0, padx=10, pady=10)
ent_fahrenhiet.grid(row=0, column=1)
btn_calc.grid(row=0, column=2, padx=10, pady=10)

#crating celsius label
lbl_celsius = tk.Label( # label
    master= window,
    text= 'Celsius:'
)

lbl_celsius.grid(row=1, column=0, pady=(10, 20))
lbl_result.grid(row=1, column=1, pady=(10, 20))
window.mainloop()