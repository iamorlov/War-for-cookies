# -*- coding: utf-8 -*-
'''
Created on 15 черв. 2013

@author: antimoskal
'''

import pygame, sys, Window
#from Window import *

class Events(Window):
  
    def __init__(self):
#        self.window = Window()
        pass
        
    def get_event(self):#,flag):
        for self.event in pygame.event.get():
            if self.event.type == MOUSEBUTTONDOWN:
                if self.event.button == 1:
                    click_coords = self.event.pos
                    self.Get_map_coords(click_coords)
                    self.Get_minimap_coords(click_coords)
            if self.event.type == QUIT:
                sys.exit()
            if self.event.type == KEYDOWN:
                if self.event.key == K_F5:
                    self.event_scan_keyes()
    
    def get_map_coords(self,click_coords):
        self.Load_part_of_map()
        #self.window.Load_part_of_map()            
        if ((click_coords[0] > 20) and (click_coords[1] > 0) and (click_coords[0] < 720) and (click_coords[1] < 700)):
            self.x_coord = (click_coords[0]-20)//self.big_step
            self.y_coord = (click_coords[1])//self.big_step
#            self.change_cell(self.y_coord+self.y_coord_start,self.x_coord+self.x_coord_start,  self.cell_type, 0, 0)
            
#            first_texture = self.textures[self.cell_type].get_rect()
#            first_texture.center=(35+self.x_coord*self.big_step,14+self.y_coord*self.big_step)
#            self.display.blit(self.textures[self.cell_type],first_texture)   
            cell = Rect((self.x_coord*self.big_step+20, self.y_coord*self.big_step),(self.big_step,self.big_step))

#            print self.cell_type
            pygame.draw.rect(self.display,(0,0,0),cell,2)
            #self.window.Maps_grid()
            self.Maps_grid()
            pygame.display.flip()
    
    def get_minimap_coords(self,click_coords):
        if ((click_coords[0] > 800) and (click_coords[1] > 0) and (click_coords[0] < 1100) and (click_coords[1] < 300)):
            self.minimap_x = (click_coords[0]-800)//self.step_p
            self.minimap_y = (click_coords[1])//self.step_p
            self.window.Load_part_of_map()
            cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*14,self.step_p*14))
            self.load_cells_list()
            self.Minimap()
            pygame.draw.rect(self.display,(0,0,0),cell,2)
            #self.window.Maps_grid()
            self.Maps_grid()         
###