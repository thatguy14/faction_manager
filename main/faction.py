# -*- coding: utf-8 -*-
"""
Created on Sat May 26 15:24:53 2018

@author: Matthew
"""
"""
TODO

- Think about how assets should be added and removed
- How are faccreds, income, and upkeep calcd

"""

 
from collections import OrderedDict
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import csv

class faction_gui(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Faction Sheet v1")
        self.geometry("400x500")
        self.option_add("*Font",("Arial",14))
        
        #This sets up the ability to resize the window and delegates each column to be equal with each other, 
        #see https://stackoverflow.com/questions/37870982/why-is-tkinter-optionmenu-changing-the-size-of-its-parent?rq=1
        self.grid_columnconfigure(0,weight=1,uniform="column")
        self.grid_columnconfigure(1,weight=1,uniform="column")
        self.grid_columnconfigure(2,weight=1,uniform="column")
        
        #This is the beginning of the menu bar
        self.menubar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menubar,tearoff = 0)
        
        self.menubar.add_cascade(label="File",menu=self.file_menu)
        
        self.config(menu = self.menubar)
        #This is the end of the menubar
        
        #This data frame contains all the input information
        #self.name_frame = tk.Frame(self,width =400,height=500,background="black")
        #self.name_frame.grid()
        
        self.faction_name = tk.Label(self,text="Faction Name: ")
        self.faction_name.grid(row=0,column=0,sticky="w")
        
        self.faction_name_entry = tk.Entry(self)
        self.faction_name_entry.grid(row=1,column=0,sticky="w",columnspan=1)
                
        self.description = tk.Label(self,text="Description: ")
        self.description.grid(row=2,column=0,sticky="w")
        
        
        self.description_box = ScrolledText(self,height=5)
        self.description_box.grid(row=3,column=0,sticky="w",columnspan = 3)
        
        ##
        #
        self.tag_label = tk.Label(self,text="Tags:")
        self.tag_label.grid(row=4,column=0,sticky='w',columnspan=4)
        
        #add drop down menu for tags
        self.get_faction_tags()
        self.tag1 = tk.StringVar(self)
        self.tag1.set(self.faction_tags_entries[0])
#        self.tag2 = tk.StringVar(self)
#        self.tag2.set(self.faction_tags_entries[1])
        
        self.list_of_tags = []
        self.string_of_tags = tk.StringVar()
        self.print_tags()
        
        self.tag_list_label = tk.Label(self,textvariable=self.string_of_tags)
        
        
        self.option_tag1 = tk.OptionMenu(self,self.tag1,*self.faction_tags_entries,command=self.add_tag)
        self.option_tag1.config(width=20,pady=6)
        self.option_tag1.grid(row=5,column=0,sticky="w",columnspan=2)
        self.tag_list_label.grid(row=6,column=0,sticky="w",columnspan=3)
        self.remove_tag_button = tk.Button(self, text="Remove Tag", command=self.remove_tag)
        
        self.remove_tag_button.grid(row=5,column=2,sticky='w')
        
        ##
        ##
        #The force, cunning, and wealth attributes
        self.faction_fcw_label_overall = tk.Label(self,text='Faction Attributes')
        self.faction_fcw_label_overall.grid(row=7,column=0,columnspan=2,sticky='w')
        self.faction_fcw_label_force = tk.Label(self,text="Force")
        self.faction_fcw_label_force.grid(row=8,column=0)
        self.faction_fcw_label_force_spinbox = tk.Spinbox(self,from_=0, to=8,width=5)
        self.faction_fcw_label_force_spinbox.grid(row=9,column=0)
        
        self.faction_fcw_label_cunning = tk.Label(self,text="Cunning")
        self.faction_fcw_label_cunning .grid(row=8,column=1)
        self.faction_fcw_label_cunning_spinbox = tk.Spinbox(self,from_=0, to=8,width=5)
        self.faction_fcw_label_cunning_spinbox.grid(row=9,column=1)
        
        self.faction_fcw_label_wealth = tk.Label(self,text="Wealth")
        self.faction_fcw_label_wealth.grid(row=8,column=2)
        self.faction_fcw_label_wealth_spinbox = tk.Spinbox(self,from_=0, to=8,width=5)
        self.faction_fcw_label_wealth_spinbox.grid(row=9,column=2)
        ##
        
    def get_faction_tags(self):
        self.faction_tags = OrderedDict()
    #How to access tags
    #print(new_faction_gui.faction_tags)
    #print(type(new_faction_gui.faction_tags['Colonists'][0]))
        with open('tags.csv','rt') as tab_file:
            csvread = csv.reader(tab_file,delimiter=',')
            for row in csvread:
                self.faction_tags[row[0]] = row[1:]
        
        self.faction_tags_entries = list(self.faction_tags.keys())
    
    def add_tag(self,t):
        if t not in self.list_of_tags:
            self.list_of_tags.append(t)
            self.print_tags()
        
        
    def print_tags(self):
        curr_string = ""
        if len(self.list_of_tags) == 0:
            curr_string = "There are no tags"
            self.string_of_tags.set(curr_string)
        elif len(self.list_of_tags) == 1:
            curr_string = self.list_of_tags[0]
            self.string_of_tags.set(curr_string)
        else:
            curr_string = [", ".join(self.list_of_tags)]
            self.string_of_tags.set(curr_string[0])
    
    def remove_tag(self):
        curr_entry_remove = self.tag1.get()
        
        if curr_entry_remove in self.list_of_tags:
            self.list_of_tags.remove(curr_entry_remove)
            self.print_tags()
        else:
            print("Not in the list")
    

class faction:
    exp_table = OrderedDict([(0,0),(1,1),(2,2),(3,4),(4,6),(5,9),(6,12),(7,16),(8,20)])
    #This contains the entire faction list loaded from the json file. 
    full_faction_list = OrderedDict()
    
    def __init__(self):
        
        #Initialize variables into a dictionary
        self.faction_info = OrderedDict([
                ('description', ""),
                ('homeworld',""),
                ('tags' , []),
                ('goal' , ""),
                ('exp' , 0),
                ('relationship' , "Neutral"),
                ('force_value' , 0),
                ('cunning_value' , 0),
                ('wealth_value' , 0),
                ('curr_HP',0),
                ('Max_HP',0),
                ('income' , 0),
                ('upkeep' , 0),
                ('faccreds' , 0),
                ('assets',OrderedDict([
                        ('Assest_name',""),
                        ('Assest_WCF',[0,0,0]),
                        ('Assest_HP',0),
                        ('Assest_maxHP',0),
                        ('Asset_type',""),
                        ('Assest_attack_info',""),
                        ('Counter',""),
                        ('Asset_location',["",""])
                        ])
                ),
                ('Asset_turn_tracker',OrderedDict([
                        ('Date',[""]),
                        ('Action',"")
                        ])
                )
        ])
    
        self.calc_max_hp()
        
    #Define Getters
    @property
    def description (self): return self.faction_info['description']
        
    @property
    def homeworld (self): return self.faction_info['homeworld']
    
    @property
    def tags (self): return self.faction_info['tags']
    
    @property
    def goal (self): return self.faction_info['goal']
        
    @property
    def exp (self): return self.faction_info['exp']
    
    @property
    def relationship (self): return self.faction_info['relationship']
    
    @property
    def force_value (self): return self.faction_info['force_value']
        
    @property
    def cunning_value (self): return self.faction_info['cunning_value']
    
    @property
    def wealth_value (self): return self.faction_info['wealth_value']
    
    @property
    def curr_HP (self): return self.faction_info['curr_HP']
        
    @property
    def Max_HP (self): return self.faction_info['Max_HP']
    
    @property
    def income (self): return self.faction_info['income']
    
    @property
    def upkeep (self): return self.faction_info['Max_HP']
    
    @property
    def faccreds (self): return self.faction_info['income']
    
    @property
    def assets (self): return self.faction_info['assets']
    
    @property
    def Asset_turn_tracker (self): return self.faction_info['Asset_turn_tracker']
    
    #Define Setters
    @description.setter
    def description (self,desc): 
        self.faction_info['description'] = desc
    
    @homeworld.setter
    def homeworld (self,home): 
        self.faction_info['homeworld'] = home
    
    @tags.setter
    def tags(self, tags): 
        if isinstance(tags,list):
            self.faction_info['goal'] = tags
            return 0
        else:
            return 1
    
    @goal.setter
    def goal (self,new_goal): self.faction_info['goal'] = new_goal
        
    @exp.setter
    def exp (self,new_exp): self.faction_info['exp'] = new_exp
    
    @relationship.setter
    def relationship (self,relat): self.faction_info['relationship'] = relat
    
    @force_value.setter
    def force_value (self,force_val):
        self.faction_info['force_value'] = force_val
        self.Max_HP
        
    @cunning_value.setter
    def cunning_value (self,cunning_val): self.faction_info['cunning_value'] = cunning_val
    
    @wealth_value.setter
    def wealth_value (self,wealth_val): self.faction_info['wealth_value'] = wealth_val
    
    @curr_HP.setter
    def curr_HP (self,curr_new_hp): self.faction_info['curr_HP'] = curr_new_hp
        
    @Max_HP.setter
    def Max_HP (self): self.calc_max_hp
    
    @income.setter
    def income (self,inc): self.faction_info['income'] = inc
    
    @upkeep.setter
    def upkeep (self,up): self.faction_info['upkeep'] = up
    
    @faccreds.setter
    def faccreds (self,creds): self.faction_info['faccreds'] = creds
    
    @assets.setter
    def assets (self,new_assets): return self.faction_info['assets']
    
    @Asset_turn_tracker.setter
    def Asset_turn_tracker (self): return self.faction_info['Asset_turn_tracker']
    
    #Helper functions
    def set_stats(self,which,amount):
        #This is for the W/C/F value bounds
        if amount < 0:
            self.faction_info[which] = 0
        elif amount > 8:
            self.faction_info[which] = 8
        else:
            self.faction_info[which] = amount
    
    def calc_max_hp(self):
        #This sets the max hp accoridng to rukes in page 217. It is equal to 4 + the HP value for w + the HP value for f...etc
        
        f = self.force_value
        w = self.wealth_value
        c = self.cunning_value
        
        f_hp = faction.exp_table[f]
        w_hp = faction.exp_table[w]
        c_hp = faction.exp_table[c]
        
        self.faction_info['Max_HP'] = 4 + f_hp + w_hp + c_hp
        
        
        
        