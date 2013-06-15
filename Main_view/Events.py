# -*- coding: utf-8 -*-
'''
Created on 15 черв. 2013

@author: antimoskal
'''
from pygame import *
import sys, Window

class Events():
  
    def __init__(self):
#        self.window = Window()
        pass
        
    def get_event(self,big_step,step_p):#,flag):
        for self.event in pygame.event.get():
            if self.event.type == MOUSEBUTTONDOWN:
                if self.event.button == 1:
                    click_coords = self.event.pos
                    self.Get_map_coords(click_coords,big_step)
                    self.Get_minimap_coords(click_coords,step_p)
            if self.event.type == QUIT:
                sys.exit()
            if self.event.type == KEYDOWN:
                if self.event.key == K_F5:
                    self.event_scan_keyes()
    
    def get_map_coords(self,click_coords,step):        
        if ((click_coords[0] > 20) and (click_coords[1] > 0) and (click_coords[0] < 720) and (click_coords[1] < 700)):
            x_coord = (click_coords[0]-20)//step
            y_coord = (click_coords[1])//step
            return x_coord, y_coord
        else:
            return 0, 0
    
    def get_minimap_coords(self,click_coords,step):
        if ((click_coords[0] > 800) and (click_coords[1] > 0) and (click_coords[0] < 1100) and (click_coords[1] < 300)):
            minimap_x = (click_coords[0]-800)//step
            minimap_y = (click_coords[1])//step
            return minimap_x, minimap_y
        else:
            return 0, 0