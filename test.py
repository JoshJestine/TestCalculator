'''from tkinter import *'''
'''from simple_colors import *
# normal and colored text
print('Normal:', blue('Welcome Finxters!'))
# print italic and colored text
print('italic: ', green('Welcome Finxter!', 'italic'))
# print italic and underlined and colored text
print('Italic and Underlined: ', red('Welcome Finxter!', ['italic', 'underlined']))'''

'''from tkinter.ttk import *

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


======================================================================='''

import tkinter as tk
from PIL import Image

root = tk.Tk()
file="dog.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(anim)

gif_label = tk.Label(root,image="")
gif_label.pack()

start = tk.Button(root,text="start",command=lambda :animation(count))
start.pack()

stop = tk.Button(root,text="stop",command=stop_animation)
stop.pack()

root.mainloop()