from tkinter import *
'''from simple_colors import *
# normal and colored text
print('Normal:', blue('Welcome Finxters!'))
# print italic and colored text
print('italic: ', green('Welcome Finxter!', 'italic'))
# print italic and underlined and colored text
print('Italic and Underlined: ', red('Welcome Finxter!', ['italic', 'underlined']))'''

from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Clock')

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 30, 'bold'),
			background = 'red',
			foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()