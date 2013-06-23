# -*- coding: utf-8 -*-
import pygame, sys
from Core import *
from lib import ResManager
from Resources import *
from Graphical_logic import *
from Events import *

class Window(Core):
     
    def __init__(self,type):
        pygame.init()
        self.empty_map(type)
        self.type = 0
        self.resources = Resources()
        self.graphical_logic = Graphical_logic()
        self.w_event = Events()
        self.minimap_x =0
        self.minimap_y =0
        self.count = 0
        self.days = 0
        self.cell_type = 0
        self.fraction = 0 
        self.stage = 0
        self.save_load_name = ''
        
    def Main_Window(self):
        self.display = pygame.display.set_mode((1280,720))
        manager = ResManager()
        pygame.display.set_icon(manager.get_image('icon.png'))
        pygame.display.set_caption("Map Editor")
        
        self.display.fill((220,220,250))
        pygame.display.flip()
        i = 0
        
    def Maps_grid(self):
        self.big_step = 28
        self.big_steps =25
        for i in range(self.big_steps):
            for j in range(self.big_steps):
                cell = Rect((20+self.big_step*i,self.big_step*j),(self.big_step,self.big_step))
                pygame.draw.rect(self.display,(0,0,0),cell,1)
        pygame.display.flip()# лол, костЫль

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
        cell = Rect((800,0),(300,300))
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        pygame.display.flip()
        
    def load_cells_list(self):
        self.cells_list = self.load_minimap_cells()

    def type_of_grids(self):       
        textures = self.resources.textures()
        colours = self.resources.colours()
        for i in range(3):
            for j in range(3):            
                first_texture = textures[i+j*3].get_rect()
                first_texture.center=(25+850+50*i,25+350+50*j)
                self.display.blit(textures[i+j*3],first_texture) 

        for i in range(3):
            for j in range(3):
                cell = Rect((850+50*i,350+50*j),(50,50))
                pygame.draw.rect(self.display,(0,0,0),cell,1)
        
        cell = Rect((875,500),(50,50))           
        first_texture = textures[9].get_rect()
        first_texture.center=(25+875,25+500)
        self.display.blit(textures[9],first_texture)
        pygame.draw.rect(self.display,(0,0,0),cell,1)
        
        cell = Rect((925,500),(50,50))            
        first_texture = textures[10].get_rect()
        first_texture.center=(25+925,25+500)
        self.display.blit(textures[10],first_texture)
        pygame.draw.rect(self.display,(0,0,0),cell,1)  
        pygame.display.update()
                
    def Minimap(self):
        colour = self.resources.colours()
        for i in range(self.steps):
            for j in range(self.steps):
                cell = Rect((800+self.step_p*i,self.step_p*j),(self.step_p,self.step_p))
                cell_type = self.cells_list[i*self.steps+j][2]
                pygame.draw.rect(self.display,colour[cell_type],cell,0)
        pygame.display.flip()
        self.Minimaps_grid()

    def moving_army(self):
        pass

    def reload_window(self,x,y):
        self.Maps_grid()
        self.Minimaps_grid()
        self.Minimap()
        self.Load_part_of_map(x,y)
        pygame.display.flip()
                
    def Load_part_of_map(self,x,y):
        textures = self.resources.textures()
        cells_list = self.load_cells(x, y)
        print len(cells_list)
        for i in range(11):
            textures[i]= pygame.transform.scale(textures[i],(28,28)) 
        for i in range(self.big_steps):
            for j in range(self.big_steps):
                cell_type = cells_list[i*self.big_steps+j][2]
                fraction  = cells_list[i*self.big_steps+j][3]
                if (cell_type >6) and (cell_type<12) or (fraction!=0):
                    x = cells_list[i*self.big_steps+j][0]
                    y = cells_list[i*self.big_steps+j][1]
                    local_list = self.load_cells_for_transparent_textures(x, y)
                    result_type = self.graphical_logic.get_type_background_textures(x, y, local_list)
                    first_texture = textures[result_type].get_rect()
                    first_texture.center=(35+self.big_step*i,14+self.big_step*j)
                    self.display.blit(textures[result_type],first_texture) 
                if (fraction > 0) and (cell_type == 9):
                    first_texture = textures[cell_type+fraction-1].get_rect()
                    first_texture.center=(35+self.big_step*i,14+self.big_step*j)
                    self.display.blit(textures[cell_type+fraction-1],first_texture)
                else:
                    first_texture = textures[cell_type].get_rect()
                    first_texture.center=(35+self.big_step*i,14+self.big_step*j)
                    self.display.blit(textures[cell_type],first_texture)               
        cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*25,self.step_p*25))
        self.Minimap()
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        self.Maps_grid()
        pygame.display.flip()

    def event_handler(self):
        event = self.w_event.get_event(self.stage, self.big_step, self.step_p)
        if (event != None):
            print self.stage
            if self.stage == 0:
                if (event[0]=='map_coords'):
                    self.action_to_map_coords(event[2],event[3])
                    self.stage = event[1]
                elif (event[0]=='minimap_coords'):
                    self.action_to_minimap_coords(event[2],event[3])
                    self.stage = event[1]
                    self.last_x = event[2]
                    self.last_y = event[3]
                elif (event[0]=='type_cell'):
                    self.stage = event[1]
                    self.type = event[2]
                    self.fraction = event[3]
                
                elif (event[0]=='save_mode'):
                    self.stage = event[1]
            if self.stage == 1:
                self.action_for_save(self.save_load_name)
                if len(event) > 2:
                    self.stage = event[1]
                    if event[3] == 'continue':
                        if len(self.save_load_name) <10:
                            self.save_load_name += event[2]
                            self.action_for_save(self.save_load_name)
                    if event[3] == 'backspace':
                        if len(self.save_load_name)>0:
                            self.save_load_name = self.save_load_name[:-1]
                            self.action_for_save(self.save_load_name)
                    if event[3] == 'save':
                        if self.save_load_name >2:
                            self.save_file(self.save_load_name)
                            self.save_load_name = ''
                            try:
                                self.reload_window(self.last_x,self.last_y)
                            except AttributeError:
                                self.reload_window(0,0)
                    if event[3] == 'cancel':
                        self.save_load_name = ''
                        try:
                            self.reload_window(self.last_x,self.last_y)
                        except AttributeError:
                            self.reload_window(0,0)

                    print self.save_load_name

                

    def action_to_map_coords(self,x,y):
        textures = self.resources.textures()
        cells_list = self.load_cells(x, y)
        for i in range(11):
            textures[i]= pygame.transform.scale(textures[i],(28,28)) 
        self.change_cell(cells_list[0][1]+y,cells_list[0][0]+x,self.type, self.fraction, 0)
        if self.fraction > 0:
            textures = pygame.transform.scale(textures[self.type+self.fraction-1],(28,28))
            first_texture = textures.get_rect()
            first_texture.center=(35+x*self.big_step,14+y*self.big_step)
            self.display.blit(textures,first_texture)
        else:
            textures = pygame.transform.scale(textures[self.type],(28,28))
            first_texture = textures.get_rect()
            first_texture.center=(35+x*self.big_step,14+y*self.big_step)
            self.display.blit(textures,first_texture)  
        #pygame.draw.rect(self.display,(0,0,0),cell,2)
        self.Maps_grid()
        pygame.display.flip()        

    def action_to_minimap_coords(self,x,y):
        self.Load_part_of_map(x,y)
        cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*25,self.step_p*25))
        self.load_cells_list()
        self.Minimap()
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        self.Maps_grid()
    
    def action_for_save(self,text):
        cell = Rect((360,260),(300,200))
        pygame.draw.rect(self.display,(204,204,204),cell,0)
        cell = Rect((385,280),(250,50))
        pygame.draw.rect(self.display,(255,255,204),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        filename = pygame.font.SysFont("Times New Roman", 20, bold=False, italic=True)
        font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
        font2 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)        
        item = u'Press enter for save'
        item2 = u'Press ESC for exit'
        font1 = font1.render(item,0,(20,20,20))
        self.display.blit(font1,(385,360))
        font2 = font2.render(item2,0,(20,20,20))
        self.display.blit(font2,(385,410))
        filename = filename.render(text,0,(20,20,20))
        self.display.blit(filename,(455,290))
        pygame.display.update()
            #self.Minimap()        
# 28x28, 25x25 cells
    def Rewrite_cell(self):
        self.event_handler()

    def Run(self):
        self.Main_Window()
        self.load_cells_list()
        self.Maps_grid()
        self.Minimaps_grid()
        self.Minimap()
        self.Load_part_of_map(0,0)
        self.type_of_grids()
        while True:
            self.Rewrite_cell()

