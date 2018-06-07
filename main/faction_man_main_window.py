# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:53:25 2018

@author: Matthew
"""

#As far as I understand it, the idea is that you have the parent window (mainwindow) and you have the children. For the children, you need to pass in the TopLevel object in order to be able to assign the subsequent options in the second window.
import tkinter as tk
import faction as fac

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Create Faction Window", 
                                command=self.create_faction_window)
        self.button.grid(row=0,column=0)

    def create_faction_window(self):
        self.faction_win = fac.faction_gui()
        

    

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()