from tkinter import Tk, Frame, BOTH, Menu, Label, SUNKEN, X, BOTTOM
import tkinter as tk
#def menucallback(event):
#    print(root.call(event.widget, "index", "active"))
#
#root = tk.Tk()

# create menu

class Application(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        parent.configure(bg = "black")
        self.pack(fill = BOTH,expand=True)
        self.parent = parent
        
        self.parent.geometry("400x400")
        
        self.var = tk.StringVar()
        self.var.set("1")
        self.entries = ["1","2","3"]
        self.option = tk.OptionMenu(self.parent,self.var,*self.entries)
        self.option.pack()
        
        self.option.bind("<<MenuSelect>>",self.test_label)
        
        self.var_label = tk.StringVar()
        self.var_label.set("this is a test")
        
        self.label = tk.Label(self.parent,textvariable=self.var_label)
        self.label.pack()
        
    def test_label(self,event=None):
        t = event
        if self.parent.call(event.widget,"index","active") == 0:
            self.var_label.set("option 1")
        elif self.parent.call(event.widget,"index","active") == 1:
            self.var_label.set("option 2")
        print(self.var_label)

#menubar = tk.Menu(root)
#menu1 = tk.Menu(menubar, tearoff=1)
#menu1.add_command(label="Button 1")
#menu1.add_command(label="Button 2")
#menubar.add_cascade(label="Menu 1", menu=menu1)
#
#menu2 = tk.Menu(menubar, tearoff=1)
#menu2.add_command(label="Button 6")
#menu2.add_command(label="Button 7")
#
#menubar.add_cascade(label="Menu 2", menu=menu2)
#
#t = menu1.winfo_children()
#tk.Tk.config(root, menu=menubar)
#
## bind to function
#menubar.bind("<<MenuSelect>>", menucallback)
root =Tk()
Application(root)
root.mainloop()

