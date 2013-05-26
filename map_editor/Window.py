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
    
    def Entry_type(self):
        cell = Rect((20,20),(700,700))
        pygame.draw.rect(self.display,(0,204,0),cell,0)
        pygame.display.flip()
        
    
    def Maps_grid(self):
        if self.map_type == 0:  
           self.step_p = 14
           self.steps = 50
        elif self.map_type == 1:
            self.step_p = 7
            self.steps = 100
        elif self.map_type == 2:
            self.step_p = 5
            self.steps = 140
        for i in range(self.steps):
            for j in range(self.steps):
                cell = Rect((20+self.step_p*i,20+self.step_p*j),(self.step_p,self.step_p))
                pygame.draw.rect(self.display,(0,0,0),cell,1)
        pygame.display.flip()
        
    def colours(self):
        self.colour = []
        for i in range(3):
            for j in range(3):
                if i+j == 0:
                    self.colour.append((0,204,0))
                elif i+j == 1:
                    self.colour.append((255,204,0))
                elif i+j == 2:
                    self.colour.append((153,102,51))
                elif i+j == 3:
                    self.colour.append((51,51,255))
                elif i+j == 4:
                    self.colour.append((51,102,51))
                elif i+j == 5:
                    self.colour.append((204,204,153))
                elif i+j == 6:
                    self.colour.append((204,204,102))
                elif i+j == 7:
                    self.colour.append((225,225,102))
                elif i+j == 8:
                    self.colour.append((0,0,0))
        print self.colour[2]   
    
    def Type_of_grids(self):       
        # Ололо, я індус
        self.colours()
        for i in range(3):
            for j in range(3):             
                cell = Rect((850+50*i,270+50*j),(50,50))
                pygame.draw.rect(self.display,self.colour[i+j],cell,0)
                
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
    
    def Get_cell_type(self):
        self.cell_type = 12
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_coords = event.pos
                    if ((click_coords[0] > 850) and (click_coords[1] > 270) and (click_coords[0] < 1050) and (click_coords[1] < 420)):
                        x_coord = (click_coords[0]-850)//50
                        y_coord = (click_coords[1]-270)//50
                        self.cell_type = x_coord+y_coord+1
                        print self.cell_type                        
                        print 'first zone'
                    if ((click_coords[0] > 875) and (click_coords[1] > 420) and (click_coords[0] < 975) and (click_coords[1] < 470)):
                        x_coord = (click_coords[0]-875)//50
                        y_coord = (click_coords[1]-420)//50
                        self.cell_type = x_coord+y_coord+10
                        print self.cell_type   
                        print 'second zone'
        pygame.display.flip()
        pygame.event.clear()
        
    def Rewrite_cell(self):
        self.Get_cell_type() ## Але, кто нибуть, найдите как запилить окончание перехвата событий!!!!!!!!!!!!
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_coords = event.pos
                    if ((click_coords[0] > 20) and (click_coords[1] > 20) and (click_coords[0] < 750) and (click_coords[1] < 720)):
                        x_coord = (click_coords[0]-20)//self.step_p
                        y_coord = (click_coords[1]-20)//self.step_p
                        print str(x_coord)+' '+str(y_coord)
        pygame.display.flip() 