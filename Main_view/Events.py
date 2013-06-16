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
    
    def get_minimap_coords(self,click_coords,step):
            minimap_x = (click_coords[0]-800)//step
            minimap_y = (click_coords[1])//step
            return minimap_x, minimap_y
    
    def mousebuttondown_terms(self, stage, click_coords,big_step,step_p):
        if stage == 0:
            if ((click_coords[0] > 20) and (click_coords[1] > 0) and (click_coords[0] < 720) and (click_coords[1] < 700)):        
                x, y = self.get_map_coords(click_coords,big_step)
                return ['map_coords', stage, x, y]
            elif ((click_coords[0] > 800) and (click_coords[1] > 0) and (click_coords[0] < 1100) and (click_coords[1] < 300)):
                x, y = self.get_minimap_coords(click_coords,step_p)
                return ['minimap_coords',stage,x,y]
            else:
                return None

    def keydown_terms(self,stage):
        if stage == 0:
            if self.event.key == pygame.K_F5:
                stage = 1
                return ['save_mode', stage]
        if stage == 1:
            if self.event.key == pygame.K_ESCAPE:
                stage = 0
                return ['save_mode', stage, '', 'cancel']
            elif self.event.key == pygame.K_RETURN:
                stage = 0
                return ['save_mode', stage, '', 'save']
            elif self.event.key == pygame.K_BACKSPACE:
                return ['save_mode', stage, '', 'backspace']
            else:
                name_key =(re.search('[a-z]',pygame.key.name(self.event.key)))
                if name_key != None:
                    text = (name_key).group(0) 
                    return ['save_mode', stage, text, 'continue']
                else:
                    return ['save_mode', stage, '', 'continue']
        
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