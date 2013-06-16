# -*- coding: utf-8 -*-
import pygame, sys
from Core import *
from ResManager import *
from Resources import *
from Graphical_logic import *
from Events import *

class Window(Core):
     
    def __init__(self,map_name):
        pygame.init()
        self.resources = Resources()
        self.graphical_logic = Graphical_logic()
        self.w_event = Events()
        print 'lol'
        self.minimap_x =0
        self.minimap_y =0
        self.count = 0
        self.days = 0
        self.fraction = 1 # першими ходять червоні
        self.map_name = map_name
        self.flag = 0
        
    def Main_Window(self):
        self.display = pygame.display.set_mode((1280,720))
        manager = ResManager()
        pygame.display.set_icon(manager.get_image('icon.png'))
        pygame.display.set_caption("War for cookies")
        self.load_file(self.map_name)
        self.display.fill((220,220,250))
        pygame.display.flip()
        i = 0
        
    def Maps_grid(self):
        self.big_step = 50
        self.big_steps =14
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
           
#    def event_scan_keyes(self):
#        pygame.event.clear()
#        self.window_for_save()
#        for event in pygame.event.get():
#            print type(event)
#            print event.type
#            if event.type == KEYDOWN:
#                print event.type
#                print type(event.key)
#                name_key =(re.search('[a-z]',pygame.key.name(event.key)))
#                if name_key != None:
#                    text = (name_key).group(0)
#                    print text
#                    return text
#                else:
#                    return ''
#            else:
#                print 'lol'
#                return 'lol'
#        pygame.display.update()
#        pygame.event.clear()                      
    
#    def window_for_save(self):
#        pygame.event.clear()
#        cell = Rect((360,260),(300,200))
#        pygame.draw.rect(self.display,(204,204,204),cell,0)
#        cell = Rect((385,280),(250,50))
#        pygame.draw.rect(self.display,(255,255,204),cell,0)
#        pygame.draw.rect(self.display,(0,0,0),cell,2)
#        #text = pygame.font.SysFont(name, size, bold, italic)
#        font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
#        font2 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)        
#        item = u'Press enter for save'
#        item2 = u'Press ESC for exit'
#        font1 = font1.render(item,0,(20,20,20))
#        self.display.blit(font1,(385,360))
#        font2 = font2.render(item2,0,(20,20,20))
#        self.display.blit(font2,(385,410))
#        text = ''
#        pygame.display.update()

#    def Reload_window(self):
#        self.Maps_grid()
#        self.Minimaps_grid()
#        self.Minimap()
#        self.Type_of_grids()
#        pygame.display.flip()
                
#    def Save_map(self,event):
#        if event.type == KEYDOWN:
#            if event.key == K_F5:
#                self.       

    def Load_part_of_map(self,x,y):
        textures = self.resources.textures()
        cells_list = self.load_cells(x, y)
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
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(textures[result_type],first_texture) 
                if (fraction > 0) and (cell_type == 9):
                    first_texture = textures[cell_type+fraction-1].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(textures[cell_type+fraction-1],first_texture)
                else:
                    first_texture = textures[cell_type].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(textures[cell_type],first_texture)               
        cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*14,self.step_p*14))
        self.Minimap()
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        self.Maps_grid()
        pygame.display.flip()

    def event_handler(self):
        event = self.w_event.get_event(self.big_step, self.step_p)
        if (event != None):
            if (event[0]=='map_coords'):
                print event
                self.action_to_map_coords(event[1],event[2])
            elif (event[0]=='minimap_coords'):
                print event
                self.action_to_minimap_coords(event[1],event[2])

    def action_to_map_coords(self,x,y):
#        self.Load_part_of_map(x,y)                
        cell = Rect((x*self.big_step+20, y*self.big_step),(self.big_step,self.big_step))
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        self.Maps_grid()
        pygame.display.flip()        

    def action_to_minimap_coords(self,x,y):
        self.Load_part_of_map(x,y)
        cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*14,self.step_p*14))
        self.load_cells_list()
        self.Minimap()
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        self.Maps_grid()
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
        while True:
            self.Rewrite_cell()

