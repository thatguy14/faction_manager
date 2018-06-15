#https://stackoverflow.com/questions/19794069/tkinter-gui-update-choices-of-an-option-menu-depending-on-a-choice-from-another

from tkinter import Tk, Frame, BOTH, Menu, Label, SUNKEN, X, BOTTOM
import tkinter as tk
#def menucallback(event):
#    print(root.call(event.widget, "index", "active"))
#
'''
TODO:
    If I were to do the following the add a delay the hover:
        
        1. Get x,y coordinates of mouse from current event
        2. Begin polling:
            a. Begin a counter
            b. Check if the user has moved their mouse:
                i. If they have exit the function
                ii. Otherwise
            c. Repeat until some time as passed
        3. if the above succeeds then display tooltip
'''

import re
class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")
        self.parent = parent
        self.parent.geometry("400x100")
        vals = ["1","2","3","4","5","6","7"]
        var = tk.StringVar()
        var.set("1")
        self.option = tk.OptionMenu(root,var,*vals)
        self.option.pack()
        self.t = self.option.children["menu"]
        tk.Menu
        #Do I need to unbind
        #t.bind("<<MenuSelect>>", self.test_func)
        self.t.bind("<<MenuSelect>>", self.test_func)
        #tk.Widget.
    def test_func(self,event = None):
        print("screen size",event.widget.winfo_screenheight())
        print("position",self.parent.winfo_geometry())
        num_height = int(re.findall(r'\d+',self.parent.winfo_geometry())[-1])
        print(num_height,type(num_height))
        print(self.option.winfo_rooty())
        #r = self.t.winfo_children()
#        print("-------")
#        print("Optionmenu children",self.option.winfo_children())
#        tt = self.option.winfo_children()
#        ttt = tt[0]
#        print("optionmenu children, list",ttt)
#        print("optionmenu childrem, length",len(tt))
#        print("menu_x",ttt.winfo_x())
#        print("event_pos", event.x,event.y)
#        print("geometry",event.widget.winfo_geometry())
#        print("viewable",event.widget.winfo_viewable())
#        print("parent", event.widget.winfo_parent())
#        print(r)
        print(self.t.winfo_children())
        #print(len(r))
        print("x,y position",event.widget.winfo_x(),event.widget.winfo_y())
        print("x,y root position",event.widget.winfo_rootx(),event.widget.winfo_rooty())
        #if self.parent.call(event.widget,"index","active") == 0:
            #print(self.t)
root = tk.Tk()
Application(root)
root.mainloop()

