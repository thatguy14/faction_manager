#https://stackoverflow.com/questions/19794069/tkinter-gui-update-choices-of-an-option-menu-depending-on-a-choice-from-another

from tkinter import Tk, Frame, BOTH, Menu, Label, SUNKEN, X, BOTTOM
import tkinter as tk
#def menucallback(event):
#    print(root.call(event.widget, "index", "active"))
#

class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")
        self.parent = parent
        vals = ["1","2","3"]
        var = tk.StringVar()
        var.set("1")
        option = tk.OptionMenu(root,var,*vals)
        option.pack()
        t = option.children["menu"]
        
        #Do I need to unbind
        #t.bind("<<MenuSelect>>", self.test_func)
        t.bind("<Enter>", self.test_func)

    def test_func(self,event = None):
        if self.parent.call(event.widget,"index","active") == 0:
            print("test")
root = tk.Tk()
Application(root)
root.mainloop()

