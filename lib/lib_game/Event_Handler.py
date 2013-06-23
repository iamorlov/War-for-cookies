# -*- coding: utf-8 -*-
from pygame import *
from Core import Core
from Graphical_logic import Graphical_logic


'''
Created on 22 черв. 2013

@author: antimoskal
'''

class Event_Handler():

    def __init__(self):
        self.core = Core()
        self.graphical_logic = Graphical_logic()

    def stage_0(self,event,fraction,days,action_to_map_coords,action_to_minimap_coords,last_x,last_y,filename):
        if (event[0]=='map_coords'):
            stage, army_coords,id_army = action_to_map_coords(event[2],event[3],last_x,last_y)
        elif (event[0]=='minimap_coords'):
            action_to_minimap_coords(event[2],event[3])
            stage = event[1]
            last_x = event[2]
            last_y = event[3]
        elif (event[0]=='save_mode'):
            stage = event[1]
        elif (event[0]=='load_mode'):
            stage = event[1]
        elif (event[0]=='end_of_army_steps'):
            print 'end_of_army_steps'
        elif (event[0]=='base_mode'):
            stage = event[1]
        elif (event[0]=='end_of_players_steps'):
            if fraction == 1:
                self.graphical_logic.change_all_armies_steps_for_fraction(fraction, filename)                
                fraction = 2
            elif fraction == 2:
                self.graphical_logic.change_all_armies_steps_for_fraction(fraction, filename)
                fraction = 1
                days +=1  
        try:
            str(stage)
        except UnboundLocalError:
            stage = 0
        try:
            return stage,last_x,last_y,fraction,days, army_coords,id_army
        except UnboundLocalError:
            return stage,last_x,last_y,fraction,days, 0,0
        
    def stage_1(self,event,name_for_saving,filename,action_for_save,reload_window,last_x,last_y):
        action_for_save(name_for_saving)
        print 'Lol = '+str(len(event))
        stage = event[1]
        if event[3] == 'continue':
            if len(name_for_saving) <10:
                name_for_saving += event[2]
                action_for_save(name_for_saving)
        if event[3] == 'backspace':
            if len(name_for_saving)>0:
                name_for_saving = name_for_saving[:-1]
                action_for_save(name_for_saving)
        if event[3] == 'save':
            if name_for_saving >2:
                self.core.save_file(name_for_saving,filename)
                name_for_saving = ''
                try:
                    reload_window(last_x,last_y)
                except AttributeError:
                    reload_window(0,0)
        if event[3] == 'cancel':
            name_for_saving = ''
            try:
                reload_window(last_x,last_y)
            except AttributeError:
                reload_window(0,0)
        return stage, name_for_saving
    
    def stage_2(self,event,name_for_loading,filename,action_for_load,reload_window,last_x,last_y):
        action_for_load(name_for_loading)
        print 'Lol = '+str(len(event))
        stage = event[1]
        if event[3] == 'continue':
            if len(name_for_loading) <10:
                name_for_loading += event[2]
                action_for_load(name_for_loading)
        if event[3] == 'backspace':
            if len(name_for_loading)>0:
                name_for_loading = name_for_loading[:-1]
                action_for_load(name_for_loading)
        if event[3] == 'save':
            if name_for_loading >2:
                self.core.load_file(name_for_loading,filename)
                name_for_loading = ''
                try:
                    reload_window(last_x,last_y)
                except AttributeError:
                    reload_window(0,0)
        if event[3] == 'cancel':
            name_for_loading = ''
            try:
                reload_window(last_x,last_y)
            except AttributeError:
                reload_window(0,0)
        return stage, name_for_loading
    
    def stage_3(self,event,stage,moving_army,filename,id_army):
        if (event[0] == 'move_army'):
            current_steps = self.graphical_logic.get_current_steps(id_army, filename)
            if current_steps > 0:
                move, stage = moving_army(event[1],event[2])
                if move == True:
                    self.graphical_logic.change_current_steps(id_army, filename, current_steps, -1)

        elif (event[0] == 'end_of_army_steps'):
            stage = event[1]
        return stage
    
    
    def stage_6(self,event,battle_dialog,stage):
        print event
        if event[0] == 'battle_mode':
            stage = event[1]
            print stage
            return stage
        else:
            stage = 6
            return stage
                
'''            

            if self.stage == 3:
                if (event[0] == 'move_army'):
                    self.moving_army(event[1],event[2])
                elif (event[0] == 'end_of_army_steps'):
                    self.stage = event[1]
'''                        