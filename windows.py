#!/usr/bin/python3

import tkinter as tk

def increment():
	counter = lbl.get()
	counter += 1
	lbl.configure(text=counter)
	
def decrement():
	counter = lbl.get()
	counter -= 1
	lbl.configure(text=counter)

window = tk.Tk()
window.geometry('500x700')

counter = 0
lbl = tk.Entry(window,width=10)
lbl.grid(column=0, row=0)
increment = tk.Button(window, text="+", command=increment)
decrement = tk.Button(window, text="-", command=decrement)
increment.grid(column=1, row=0)
decrement.grid(column=2, row=0)

window.mainloop()



