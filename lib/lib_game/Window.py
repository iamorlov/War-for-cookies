# -*- coding: utf-8 -*-
import pygame, sys
from Core import Core
from lib import ResManager
from Resources import *
from Graphical_logic import *
from Events import *

class Window():
     
    def __init__(self,map_name):
        pygame.init()
        self.core = Core()
        
        self.file = 'ingame_temp'#заміна self.file в Core.py
        #self.map_type - треба замінити в Core.py
        #self.x_coord_start self.x_coord_end - замінити в Core.py
        
        self.resources = Resources()
        self.graphical_logic = Graphical_logic()
        self.w_event = Events()
        self.minimap_x =0
        self.minimap_y =0
        self.count = 0
        self.days = 0
        self.fraction = 1 # першими ходять червоні
        self.map_name = map_name
        self.stage = 0
        self.save_load_name = ''
        
    def Main_Window(self):
        self.display = pygame.display.set_mode((1280,720))
        manager = ResManager()
        pygame.display.set_icon(manager.get_image('icon.png'))
        pygame.display.set_caption("War for cookies")
        self.map_type = self.core.load_file(self.map_name,self.file)
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
        self.cells_list = self.core.load_minimap_cells(self.file)

    def Minimap(self):
        colour = self.resources.colours()
        for i in range(self.steps):
            for j in range(self.steps):
                cell = Rect((800+self.step_p*i,self.step_p*j),(self.step_p,self.step_p))
                cell_type = self.cells_list[i*self.steps+j][2]
                pygame.draw.rect(self.display,colour[cell_type],cell,0)
        pygame.display.flip()
        self.Minimaps_grid()
        
    def game_buttons(self):
        x = 1150
        y = 0
        colour = self.resources.colours()
        for i in range(4):
            cell = Rect((x,y),(130,175))
            pygame.draw.rect(self.display,colour[i],cell,0)
            pygame.draw.rect(self.display,(0,0,0),cell,1)
            y+=175
        pygame.display.update()

    def reload_window(self,x,y):
        self.Maps_grid()
        self.Minimaps_grid()
        self.Minimap()
        self.Load_part_of_map(x,y)
        self.game_buttons()
        pygame.display.flip()
                
    def Load_part_of_map(self,x,y):
        textures = self.resources.textures()
        textures_army = self.resources.textures_for_army()
        cells_list,x_coord_start,y_coord_start= self.core.load_cells(x,y,self.file)
        for i in range(self.big_steps):
            for j in range(self.big_steps):
                cell_type = cells_list[i*self.big_steps+j][2]
                fraction  = cells_list[i*self.big_steps+j][3]
                army = cells_list[i*self.big_steps+j][4]
                if (cell_type >6) and (cell_type<12) or ((fraction!=0) and (army == 0)):
                    x = cells_list[i*self.big_steps+j][0]
                    y = cells_list[i*self.big_steps+j][1]
                    local_list = self.core.load_cells_for_transparent_textures(x, y,self.file)
                    result_type = self.graphical_logic.get_type_background_textures(x, y, local_list)
                    first_texture = textures[result_type].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(textures[result_type],first_texture) 
                if (fraction > 0) and (cell_type == 9):
                    first_texture = textures[cell_type+fraction-1].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(textures[cell_type+fraction-1],first_texture)
                elif((cell_type<3) and (army > 0)):
                    first_texture = textures[cell_type].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(textures_army[fraction*5+1],first_texture)
                else:
                    first_texture = textures[cell_type].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(textures[cell_type],first_texture)               
        cell = Rect((800+x_coord_start*self.step_p,0+y_coord_start*self.step_p),(self.step_p*14,self.step_p*14))
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

                elif (event[0]=='minimap_coords'):
                    self.action_to_minimap_coords(event[2],event[3])
                    self.stage = event[1]
                    self.last_x = event[2]
                    self.last_y = event[3]
                elif (event[0]=='save_mode'):
                    self.stage = event[1]
                elif (event[0]=='end_of_army_steps'):
                    print 'end_of_army_steps'
                elif (event[0]=='base_mode'):
                    self.stage = event[1]
                elif (event[0]=='end_of_players_steps'):
                    if self.fraction == 1:
                        self.fraction = 2
                    elif self.fraction == 2:
                        self.fraction = 1
                        self.days +=1
                    days = 'Day '+str(self.days+1)
                    fraction = str(self.fraction)
                    cell = Rect((800,650),(300,50))
                    pygame.draw.rect(self.display,(220,220,250),cell,0)
                    font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
                    font2 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)        
                    font1 = font1.render(days,0,(20,20,20))
                    self.display.blit(font1,(825,675))
                    font2 = font2.render(fraction,0,(20,20,20))
                    self.display.blit(font2,(975,675))
                    pygame.display.update()                    
                    
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
                            self.core.save_file(self.save_load_name,self.file)
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

            if self.stage == 3:
                if (event[0] == 'move_army'):
                    self.moving_army(event[1],event[2])
                elif (event[0] == 'end_of_army_steps'):
                    self.stage = event[1]
                    

                

    def action_to_map_coords(self,x,y):
#        self.Load_part_of_map(x,y)
        cell = self.core.load_cell(y,x,self.file)
        if ((cell[3] == self.fraction) and (cell[4]>0)):
            self.stage = 3
            self.army_coords = [y,x]

    def moving_army(self,x,y):
        cell = self.core.load_cell(self.army_coords[0],self.army_coords[1],self.file)
        print cell
        if cell[4]!=0:
            self.id_army = cell[4]
        print 'army '+str(self.id_army)
        self.core.change_cell(cell[0],cell[1],cell[2],0,0,self.file)
        if ((self.army_coords[0]+x>-1) and (self.army_coords[1]+y>-1)):
            cell = self.core.load_cell(self.army_coords[0]+x,self.army_coords[1]+y,self.file)
            print cell
            if (((cell[2]>=0) and (cell[2]<3)) and (cell[4] == 0)):
                self.core.change_cell(self.army_coords[0]+x,self.army_coords[1]+y,cell[2],self.fraction,self.id_army,self.file)
                self.army_coords[0] += x
                self.army_coords[1] += y
                try:
                    self.reload_window(self.last_x,self.last_y)
                except AttributeError:
                    self.reload_window(0,0)
            else:
                print 'error'
                
            
    def action_to_minimap_coords(self,x,y):
        self.Load_part_of_map(x,y)
        cells_list,x_coord_start,y_coord_start = self.core.load_cells(x, y, self.file)
        cell = Rect((800+x_coord_start*self.step_p,0+y_coord_start*self.step_p),(self.step_p*14,self.step_p*14))
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
        self.game_buttons()
        self.Minimaps_grid()
        self.Minimap()
        self.Load_part_of_map(0,0)
        while True:
            self.Rewrite_cell()

