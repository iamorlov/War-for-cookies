# -*- coding: utf-8 -*-
'''
Created on 15 черв. 2013

@author: antimoskal
'''
import pygame
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
    
    def mousebuttondown_terms(self,click_coords,big_step,step_p):
        if ((click_coords[0] > 20) and (click_coords[1] > 0) and (click_coords[0] < 720) and (click_coords[1] < 700)):        
            x, y = self.get_map_coords(click_coords,big_step)
            return ['map_coords', x, y]
        elif ((click_coords[0] > 800) and (click_coords[1] > 0) and (click_coords[0] < 1100) and (click_coords[1] < 300)):
            x, y = self.get_minimap_coords(click_coords,step_p)
            return ['minimap_coords',x,y]
        else:
            return None
        
    def get_event(self,big_step,step_p):#,flag):
        for self.event in pygame.event.get():
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if self.event.button == 1:
                    click_coords = self.event.pos
                    return self.mousebuttondown_terms(click_coords, big_step, step_p)
            if self.event.type == pygame.QUIT:
                sys.exit()
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_F5:
                    pass
                    #self.event_scan_keyes()