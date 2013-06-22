# -*- coding: utf-8 -*-
from pygame import *
from Core import Core

'''
Created on 22 черв. 2013

@author: antimoskal
'''

class Event_Handler():

    def __init__(self):
        self.core = Core()

    def stage_0(self,event,fraction,days,action_to_map_coords,action_to_minimap_coords,last_x,last_y,):
        if (event[0]=='map_coords'):
            stage, army_coords = action_to_map_coords(event[2],event[3])
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
                fraction = 2
            elif fraction == 2:
                fraction = 1
                days +=1
            days = 'Day '+str(days+1)
            fraction_out = str(fraction)
            cell = Rect((800,650),(300,50))
            pygame.draw.rect(self.display,(220,220,250),cell,0)
            font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
            font2 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)        
            font1 = font1.render(days,0,(20,20,20))
            self.display.blit(font1,(825,675))
            font2 = font2.render(fraction_out,0,(20,20,20))
            self.display.blit(font2,(975,675))
            pygame.display.update()  
        try:
            str(stage)
        except UnboundLocalError:
            stage = 0
        try:
            return stage,last_x,last_y,fraction,days, army_coords
        except UnboundLocalError:
            return stage,last_x,last_y,fraction,days, 0
        
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
'''            

            if self.stage == 3:
                if (event[0] == 'move_army'):
                    self.moving_army(event[1],event[2])
                elif (event[0] == 'end_of_army_steps'):
                    self.stage = event[1]
'''                        