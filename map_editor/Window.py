# -*- coding: utf-8 -*-
import pygame, sys
from Core import *
from ResManager import *

class Window(Core):
    def __init__(self):
        pygame.init()
        
    def Main_Window(self):
        self.display = pygame.display.set_mode((1200,740))
        manager = ResManager()
        pygame.display.set_icon(manager.get_image('icon.png'))
        pygame.display.set_caption("Map Editor")
        a = manager.get_image('logo.png')
        self.empty_map(0)
        self.display.fill((250,250,250))
        pygame.display.flip()
        i = 0
    
    def Maps_grid(self):
        if self.map_type == 0:  
           step_p = 14
           steps = 50
        elif self.map_type == 1:
            step_p = 7
            steps = 100
        elif self.map_type == 2:
            step_p = 5
            steps = 140
        for i in range(steps):
            for j in range(steps):
                cell = Rect((20+step_p*i,20+step_p*j),(step_p,step_p))
                pygame.draw.rect(self.display,(0,0,0),cell,1)
        pygame.display.flip()
        
    def Type_of_grids(self):       
        # Ололо, я індус
        for i in range(3):
            for j in range(3):
                if i+j == 0:
                    colour = (0,204,0)
                elif i+j == 1:
                    colour = (255,204,0)
                elif i+j == 2:
                    colour = (153,102,51)
                elif i+j == 3:
                    colour = (51,51,255)
                elif i+j == 4:
                    colour = (51,102,51)
                elif i+j == 5:
                    colour = (204,204,153)
                elif i+j == 6:
                    colour = (204,204,102)
                elif i+j == 7:
                    colour = (225,225,102)
                elif i+j == 8:
                    colour = (0,0,0)              
                cell = Rect((850+50*i,270+50*j),(50,50))
                pygame.draw.rect(self.display,colour,cell,0)
                
        for i in range(3):
            for j in range(3):
                cell = Rect((850+50*i,270+50*j),(50,50))
                pygame.draw.rect(self.display,(0,0,0),cell,1)
        cell = Rect((875,420),(50,50))
        ## червоний 
        pygame.draw.rect(self.display,(255,51,0),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,1)
        cell = Rect((925,420),(50,50))
        ## cиній
        pygame.draw.rect(self.display,(51,0,255),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,1)
        pygame.display.flip()
    
    def Mouse_events(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_coords = event.pos
                    if ((click_coords[0] > 850) and (click_coords[1] > 270) and (click_coords[0] < 1050) and (click_coords[1] < 420)):
                        x_coord = (click_coords[0]-850)//50
                        y_coord = (click_coords[1]-270)//50
                        cell_type = x_coord+y_coord+1
                        print cell_type                        
                        print 'first zone'
                    if ((click_coords[0] > 875) and (click_coords[1] > 420) and (click_coords[0] < 975) and (click_coords[1] < 470)):
                        x_coord = (click_coords[0]-875)//50
                        y_coord = (click_coords[1]-420)//50
                        cell_type = x_coord+y_coord+10
                        print cell_type   
                        print 'second zone'

            #print event.type
        pygame.display.flip()