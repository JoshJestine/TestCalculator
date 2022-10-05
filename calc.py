import tkinter as tk
from tkinter import *
import time

print ("Welcome to Josh's Calculator");
print ("----------------------------");

root = Tk()
root.geometry = ("200x50")
root.config(bg='grey')

"""main = tk()
ourMessage = 'Welcome to the Calculator which is a scam'
messageVar = Message(main, text= ourMessage)"""

canvas = Tk()
canvas.title("Digital Clock")
canvas.geometry("350x200")
canvas.resizable(1,1)
label = Label(canvas, font=("Courier", 30, 'bold'), bg="blue", fg="white", bd =30)
label.grid(row =0, column=1)
def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   label.config(text=text_input)
   label.after(200, digitalclock)
digitalclock()
canvas.mainloop()

calc = tk.Tk()
calc.title("Numbers Daddy")

buttons = [
'7',  '8',  '9',  '*',  'C',
'4',  '5',  '6',  '/',  'Neg',
'1',  '2',  '3',  '-',  '$',
'0',  '.',  '=',  '+',  '@' ]

row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(calc, text = i, width = 7, height = 7, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = tk.Entry(calc, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)

def click_event(key):

    if key == '=':
        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")
			
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "   Error, use only valid chars")
				
    elif key == 'C':
        display.delete(0, tk.END)
				
    elif key == '$':
        display.delete(0, tk.END)
        display.insert(tk.END, "$$$$C.$R.$E.$A.$M.$$$$")
				
    elif key == '@':
        display.delete(0, tk.END)
        display.insert(tk.END, "joshhhhh")		

    elif key == 'neg':
        if '=' in display.get():
            display.delete(0, tk.END)
        try:
            if display.get()[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
        except IndexError:
            pass

    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)

calc.mainloop()