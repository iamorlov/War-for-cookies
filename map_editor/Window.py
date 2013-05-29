# -*- coding: utf-8 -*-
import pygame, sys
from Core import *
from ResManager import *

class Window(Core):
    def __init__(self):
        pygame.init()
        self.cell_type = 0
        self.minimap_x =0
        self.minimap_y =0
        
    def Main_Window(self):
        self.display = pygame.display.set_mode((1200,740))
        manager = ResManager()
        pygame.display.set_icon(manager.get_image('icon.png'))
        pygame.display.set_caption("Map Editor")
        a = manager.get_image('logo.png')
        self.empty_map(1)
        self.display.fill((250,250,250))
        pygame.display.flip()
        i = 0
    
    def Entry_type(self):
        cell = Rect((20,20),(700,700))
        pygame.draw.rect(self.display,(0,204,0),cell,0)
        pygame.display.flip()
        
    
    def Maps_grid(self):
        self.big_step = 28
        self.big_steps =25
        for i in range(self.big_steps):
            for j in range(self.big_steps):
                cell = Rect((20+self.big_step*i,20+self.big_step*j),(self.big_step,self.big_step))
                pygame.draw.rect(self.display,(0,0,0),cell,1)
        pygame.display.flip()

    def Minimaps_grid(self):
        if self.map_type == 0:  
           self.step_p = 6
           self.steps = 50
        elif self.map_type == 1:
            self.step_p = 3
            self.steps = 100
        elif self.map_type == 2:
            self.step_p = 2
            self.steps = 140
        cell = Rect((800,20),(300,300))
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        pygame.display.flip()

        
    def colours(self):
        self.colour = []
        for i in range(11):
            if i == 0:
                self.colour.append((0,204,0))
            elif i == 1:
                self.colour.append((255,204,0))
            elif i == 2:
                self.colour.append((153,102,51))
            elif i == 3:
                self.colour.append((51,51,255))
            elif i == 4:
                self.colour.append((51,102,51))
            elif i == 5:
                self.colour.append((204,204,153))
            elif i == 6:
                self.colour.append((204,204,102))
            elif i == 7:
                self.colour.append((225,225,102))
            elif i == 8:
                self.colour.append((0,0,0))
            elif i == 9:
                self.colour.append((255,51,0))
            elif i == 10:
                self.colour.append((51,0,255))

    
    def Type_of_grids(self):       
        # Ололо, я індус
        self.colours()
        for i in range(3):
            for j in range(3):             
                cell = Rect((850+50*i,370+50*j),(50,50))
                pygame.draw.rect(self.display,self.colour[i+j*3],cell,0)
        for i in range(3):
            for j in range(3):
                cell = Rect((850+50*i,370+50*j),(50,50))
                pygame.draw.rect(self.display,(0,0,0),cell,1)
        cell = Rect((875,520),(50,50))
        ## червоний 
        pygame.draw.rect(self.display,(255,51,0),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,1)
        cell = Rect((925,520),(50,50))
        ## cиній
        pygame.draw.rect(self.display,(51,0,255),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,1)
        pygame.display.flip()
        self.load_cells(5, 30)
    

                    
    def Get_cell_type(self,click_coords):
        if ((click_coords[0] > 850) and (click_coords[1] > 370) and (click_coords[0] < 1050) and (click_coords[1] < 520)):
            x_coord = (click_coords[0]-850)//50
            y_coord = (click_coords[1]-270)//50
            self.cell_type = x_coord+y_coord*3
            print self.cell_type                        
            print 'first zone'
        if ((click_coords[0] > 875) and (click_coords[1] > 520) and (click_coords[0] < 975) and (click_coords[1] < 570)):
            x_coord = (click_coords[0]-875)//50
            y_coord = (click_coords[1]-520)//50
            self.cell_type = x_coord+y_coord+9
            print self.cell_type   
            print 'second zone'

    def Get_minimap_coords(self,click_coords):                 
        if ((click_coords[0] > 800) and (click_coords[1] > 20) and (click_coords[0] < 1100) and (click_coords[1] < 320)):
            self.minimap_x = (click_coords[0]-800)//self.step_p
            self.minimap_y = (click_coords[1]-20)//self.step_p
            print str(self.minimap_x)+' '+str(self.minimap_y)

    def Get_map_coords(self,click_coords):                
        if ((click_coords[0] > 20) and (click_coords[1] > 20) and (click_coords[0] < 720) and (click_coords[1] < 720)):
            self.x_coord = (click_coords[0]-20)//self.big_step
            self.y_coord = (click_coords[1]-20)//self.big_step
            print str(self.x_coord)+' '+str(self.y_coord)
                        #
                        #cell = Rect((20+self.big_step*self.x_coord,20+self.big_step*self.y_coord),(self.big_step,self.big_step))
                        #pygame.draw.rect(self.display,self.colour[self.cell_type],cell,0)
                        #self.Maps_grid()
                        #pygame.display.flip()
    
    def Events(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_coords = event.pos
                    self.Get_cell_type(click_coords)
                    self.Get_map_coords(click_coords)
                    self.Get_minimap_coords(click_coords)
                    
                    
                    
    def Load_part_of_map(self):
        cells_list = self.load_cells(self.minimap_x, self.minimap_y)
        print str(self.x_coord_start)+'  '+str(self.y_coord_start)
# 28x28, 25x25 cells
    def Rewrite_cell(self):
        self.Events()
        self.Load_part_of_map()
        # + self.load_cells(x, y)
        #self.change_cell(self.x_coord, self.y_coord, self.cell_type, 0, 0)
        
