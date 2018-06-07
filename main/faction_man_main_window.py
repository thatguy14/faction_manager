# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:53:25 2018

@author: Matthew
"""

#As far as I understand it, the idea is that you have the parent window (mainwindow) and you have the children. For the children, you need to pass in the TopLevel object in order to be able to assign the subsequent options in the second window.
import tkinter as tk

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Create new window", 
                                command=self.create_window)
        self.button.pack(side="top")

    def create_window(self):
        self.app = second_window()
        
class second_window(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("800x400")
        self.frame = tk.Frame(self)
        self.label = tk.Label(self,text="Label")
        self.label.pack()
        self.frame.pack()
    

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()