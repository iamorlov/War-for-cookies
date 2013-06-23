# -*- coding: utf-8 -*-
'''
Created on 15 черв. 2013

@author: antimoskal
'''
import pygame,re
import sys, Window

class Events():
  
    def __init__(self):
        pygame.init()
        pass
    
    def get_map_coords(self,click_coords,step):        
            x_coord = (click_coords[0]-20)//step
            y_coord = (click_coords[1])//step
            return x_coord, y_coord
    
    
    def get_type_coords(self,click_coords):
        if ((click_coords[0] > 500) and (click_coords[1] > 660) and (click_coords[0] < 920) and (click_coords[1] < 720)):
            x_coord = (click_coords[0]-500)//60
            return x_coord, 0

      
    
    def move_coords(self):
        if self.event.key ==pygame.K_DOWN:
            return ['move_army', 0, 1]
        
        if self.event.key ==pygame.K_UP:
            return ['move_army', 0, -1]
        
        if self.event.key ==pygame.K_LEFT:
            return ['move_army', 1, 0]
        
        if self.event.key ==pygame.K_RIGHT:
            return ['move_army', -1, 0]
    
    def mousebuttondown_terms(self, stage, click_coords,big_step,step_p):
        if stage == 0:
            if ((click_coords[0] > 20) and (click_coords[1] > 0) and (click_coords[0] < 1220) and (click_coords[1] < 660)):        
                x, y = self.get_map_coords(click_coords,big_step)
                return ['map_coords', stage, x, y]
            elif ((click_coords[0] > 500) and (click_coords[1] > 660) and (click_coords[0] < 920) and (click_coords[1] < 720)):
                type_cell, fraction = self.get_type_coords(click_coords)
                return ['type_cell',stage, type_cell, fraction]
            else:
                return None

    def keydown_terms(self,stage):
        if stage == 0:
            if self.event.key == pygame.K_F5:
                stage = 1
                return ['save_mode', stage]
            if self.event.key == pygame.K_F7:
                stage = 2
                return ['load_mode', stage]
        if (stage == 1) or (stage == 2):
            if (stage == 1):
                mode = 'save_mode'
            if (stage == 2):
                mode = 'load_mode'
            if self.event.key == pygame.K_ESCAPE:
                stage = 0
                return [mode, stage, '', 'cancel']
            elif self.event.key == pygame.K_RETURN:
                stage = 0
                return [mode, stage, '', 'save']
            elif self.event.key == pygame.K_BACKSPACE:
                return [mode, stage, '', 'backspace']
            else:
                name_key =(re.search('[a-z]',pygame.key.name(self.event.key)))
                if name_key != None:
                    text = (name_key).group(0) 
                    return [mode, stage, text, 'continue']
                else:
                    return [mode, stage, '', 'continue']
        if (stage == 3):
            return self.move_coords() 
        
    def get_event(self,stage,big_step,step_p):#,flag):
        for self.event in pygame.event.get():
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if self.event.button == 1:
                    click_coords = self.event.pos
                    return self.mousebuttondown_terms(stage, click_coords, big_step, step_p)
            if self.event.type == pygame.QUIT:
                sys.exit()
            if self.event.type == pygame.KEYDOWN:
                return self.keydown_terms(stage)
                    #self.event_scan_keyes()