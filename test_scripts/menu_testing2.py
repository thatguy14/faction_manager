# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 07:39:22 2018

@author: Matthew
http://code.activestate.com/lists/python-tkinter-discuss/2475/
"""

from tkinter import *
#import tkFont
tk = Tk()

def statusbarUpdate( event=None ):
   print(tk.call(event.widget, "index", "active"))
   print(event.widget.index('active'))

menubar=Menu(tk)
tk.config(menu=menubar)
popup = Menu( menubar )
menubar.add_cascade(label="MyMenu", menu=popup)
popup.bind( '<<MenuSelect>>', statusbarUpdate )
popup.add_command(label="Option 1")
popup.add_command(label="Option 2")
popup.add_command(label="Option 3")
tk.mainloop()