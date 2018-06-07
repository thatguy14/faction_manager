# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:38:12 2018

@author: Matthew
https://stackoverflow.com/questions/16665155/python-tkinter-label-widget-mouse-over
"""

import tkinter as tk

root = tk.Tk()
mylist = ['a','b','c','d','e']

for i, x in enumerate(mylist):
    label = tk.Label(root, text="Label "+str(i))
    label.grid(row=i+1, column=1)
    label.bind("<Enter>", lambda e, x=x: e.widget.config(text=x))
    label.bind("<Leave>", lambda e, i=i: e.widget.config(text="Label "+str(i)))

root.mainloop()