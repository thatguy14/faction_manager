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
        
        
        
        