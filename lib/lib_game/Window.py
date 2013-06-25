# -*- coding: utf-8 -*-
import pygame, sys
from Core import Core
from ResManager import ResManager
from Resources import *
from Graphical_logic import *
from Events import *
from Event_Handler import Event_Handler


class Window():
     
    def __init__(self,map_name):
        pygame.init()
        self.core = Core()
        self.mode = Event_Handler()
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
        self.fractions = [[1, 1, 0, 0, 3, 1],[2, 1, 0, 0, 0, 0]]
        
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
            self.steps = 150
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
        textures = self.resources.textures_for_menu()
        for i in range(4):
            first_textures =textures[i].get_rect()
            first_textures.center=(1215,90+180*i)
            self.display.blit(textures[i],first_textures)  
        pygame.display.update()

    def reload_window(self,x,y):
        self.Maps_grid()
        self.Minimaps_grid()
        self.Minimap()
        self.Load_part_of_map(x,y)
        self.game_buttons()
        pygame.display.flip()
    
    def status_army(self,id_army):
        cell = Rect((900,350),(225,400))
        pygame.draw.rect(self.display,(220,220,250),cell,0)
        textures_default = self.resources.textures_for_army()
        fraction = self.fraction
        textures = []
        list_army = self.core.load_army(self.file, id_army)
        for i in range(5):
            textures.append(textures_default[fraction*5+fraction+i+1])
            first_texture = textures[i].get_rect()
            first_texture.center=(932,370+64*i)
            self.display.blit(textures[i],first_texture)
            try:
                font1 = pygame.font.SysFont("Monospace", 40, bold=True, italic=False)
                item = str(list_army[i+1])
                font1 = font1.render(item,0,(20,20,20))
                self.display.blit(font1,(964,350+64*i))
            except TypeError:         
                pass
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
                    self.display.blit(textures[cell_type],first_texture)      
                    first_texture = textures[cell_type].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(textures_army[fraction*5+fraction],first_texture)
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
            if self.stage == 0:
                try:
                    self.stage,self.last_x,self.last_y,self.fraction,self.days,self.army_coords,self.id_army,self.x_start,self.y_start \
                    = self.mode.stage_0(event, self.fraction, self.days, self.action_to_map_coords, self.action_to_minimap_coords,self.last_x,self.last_y,self.file,self.x_start,self.y_start)
                except AttributeError:
                    self.status_army(0)
                    self.stage,self.last_x,self.last_y,self.fraction,self.days,self.army_coords,self.id_army,self.x_start,self.y_start \
                    = self.mode.stage_0(event, self.fraction, self.days, self.action_to_map_coords, self.action_to_minimap_coords,0,0,self.file,0,0)           

                days = 'Day '+str(self.days+1)
                fraction_out = str(self.fraction)
                cell = Rect((800,650),(300,50))
                pygame.draw.rect(self.display,(220,220,250),cell,0)
                font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
                font2 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)        
                font1 = font1.render(days,0,(20,20,20))
                self.display.blit(font1,(825,675))
                font2 = font2.render(fraction_out,0,(20,20,20))
                self.display.blit(font2,(975,675))
                pygame.display.update()    
            if self.stage == 1:
                self.action_for_save(self.save_load_name)
                if len(event) > 2:
                    try:
                        self.stage,self.save_load_name = self.mode.stage_1(event, self.save_load_name, self.file, self.action_for_save, self.reload_window, self.last_x, self.last_y)
                    except AttributeError:
                        self.stage,self.save_load_name = self.mode.stage_1(event, self.save_load_name, self.file, self.action_for_save, self.reload_window, 0,0)
                    print self.save_load_name

            if self.stage == 2:
                self.action_for_load(self.save_load_name)
                if len(event) > 2:
                    try:
                        self.stage,self.save_load_name = self.mode.stage_2(event, self.save_load_name, self.file, self.action_for_load, self.reload_window, self.last_x, self.last_y)
                    except AttributeError:
                        self.stage,self.save_load_name = self.mode.stage_2(event, self.save_load_name, self.file, self.action_for_load, self.reload_window, 0,0)
                    print self.save_load_name

            if self.stage == 3:
                self.stage,self.last_x,self.last_y,self.armies_list = self.mode.stage_3(event, self.stage, self.moving_army,self.file,self.id_army,self.last_x,self.last_y)

            if self.stage == 4:
                pass
            
            if self.stage == 5:
                pass

            if self.stage == 6:
                self.battle_dialog_window()
                self.stage = self.mode.stage_6(event, self.battle_dialog_window,self.stage,self.reload_window,self.last_x,self.last_y)

            if self.stage == 7:
                pass
            
            if self.stage == 8:
                pass

    def action_to_map_coords(self,x,y,last_x,last_y):
#        self.Load_part_of_map(x,y)

        cell = self.core.load_cell(y+last_y,x+last_x,self.file)
        if ((cell[3] == self.fraction) and (cell[4]>0)):
            stage = 3
            army_coords = [y+last_y,x+last_x]
            id_army = cell[4]
            self.status_army(id_army)
            return stage, army_coords, id_army
        
        else:
            return 0,0,0


    def moving_army(self,x,y,last_x,last_y):## Диагноз - говнокод 90лвл(2:14 ночи)
        armies_lists = 0
        self.status_army(self.id_army)
        cell = self.core.load_cell(self.army_coords[0],self.army_coords[1],self.file)
        if cell[4]!=0:
            self.id_army = cell[4]
        print 'army '+str(self.id_army)
        self.core.change_cell(cell[0],cell[1],cell[2],0,0,self.file)
        if ((self.army_coords[0]+x>-1) and (self.army_coords[1]+y>-1) and (self.army_coords[1]+y<self.steps) and (self.army_coords[0]+x<self.steps)):
            cell = self.core.load_cell(self.army_coords[0]+x,self.army_coords[1]+y,self.file)
            if (((cell[2]>=0) and (cell[2]<3)) and (cell[4] == 0)):
                self.core.change_cell(self.army_coords[0]+x,self.army_coords[1]+y,cell[2],self.fraction,self.id_army,self.file)
                self.army_coords[0] += x
                self.army_coords[1] += y
                print 'last_x '+str(last_x)+'last_y = '+str(last_y)
                try:
                    if (self.army_coords[1] - self.x_start >6):
                        self.x_start+=5
                        last_x = self.x_start+7
                        if (self.x_start>self.steps-1):
                            self.x_start = self.steps - self.big_steps
                        self.reload_window(last_x,last_y)
                        print 'last_x '+str(last_x)+'last_y = '+str(last_y)
                    elif (self.army_coords[0]- self.y_start >6):
                        self.y_start +=5
                        last_y = self.y_start+7
                        if (self.y_start>self.steps-1):
                            self.y_start = self.steps - self.big_steps
                        print 'Event!'
                        self.reload_window(last_x,last_y)
                        print 'last_x '+str(last_x)+'last_y = '+str(last_y)
                    elif (self.army_coords[1] - self.last_x <-6):
                        self.x_start-=5
                        if (self.x_start<0):
                            self.x_start = 0
                            last_x = self.x_start+7
                        self.reload_window(last_x,last_y)
                        print 'last_x '+str(last_x)+'last_y = '+str(last_y)
                    elif (self.army_coords[0]- self.last_y <-6):
                        self.y_start -=5
                        last_y = self.y_start+7
                        if (self.y_start<0):
                            self.y_start = 0
                        print 'Event!'
                        self.reload_window(last_x,last_y)
                        print 'last_x '+str(last_x)+'last_y = '+str(last_y)
                    else:
                        self.reload_window(last_x,last_y)
                except AttributeError:
                    self.reload_window(0,0)
                    print 'last_x '+str(last_x)+'last_y = '+str(last_y)
                return True,3, last_x,last_y,0
            
            elif ((((cell[2]>=0) and (cell[2]<3)) and(cell[3]!=self.fraction) and (cell[4] != 0))or ((cell[2]==9) and (cell[3]==self.fraction))):
                stage = 6
                armies_lists = []
                armies_lists.append(self.core.load_army(self.file, self.id_army))
                self.core.change_cell(self.army_coords[0],self.army_coords[1],cell[2],self.fraction,self.id_army,self.file)                
                cell = self.core.load_cell(self.army_coords[0]+x,self.army_coords[1]+y,self.file)
                armies_lists.append(self.core.load_army(self.file, cell[4]))
                print(armies_lists)
                return False, stage,last_x,last_y,armies_lists
            elif (((cell[2]>=7) and (cell[2]<9)) and (cell[3] != self.fraction)):
                stage = 3
                lose_fraction  = cell[3]
                print 'Alert'
                if lose_fraction > 0:
                    if cell[2] == 7:
                        frac = self.core.get_fraction_status(self.file, lose_fraction)
                        self.core.change_fraction_status(self.file, lose_fraction, frac[1], frac[2], frac[3], frac[4]-1, frac[5])
                        frac = self.core.get_fraction_status(self.file, self.fraction)
                        self.core.change_fraction_status(self.file, self.fraction, frac[1], frac[2], frac[3], frac[4]+1, frac[5])
                        self.core.change_cell(cell[0], cell[1], 7, self.fraction, 0, self.file)
                    if cell[2] == 8:
                        frac = self.core.get_fraction_status(self.file, lose_fraction)
                        self.core.change_fraction_status(self.file, lose_fraction, frac[1], frac[2], frac[3], frac[4], frac[5]-1)
                        frac = self.core.get_fraction_status(self.file, self.fraction)
                        self.core.change_fraction_status(self.file, self.fraction, frac[1], frac[2], frac[3], frac[4], frac[5]+1)
                        self.core.change_cell(cell[0], cell[1], 8, self.fraction, 0, self.file)                        
                else:
                    if cell[2] == 7:
                        frac = self.core.get_fraction_status(self.file, self.fraction)
                        self.core.change_fraction_status(self.file, self.fraction, frac[1], frac[2], frac[3], frac[4]+1, frac[5])
                        self.core.change_cell(cell[0], cell[1], 7, self.fraction, 0, self.file)
                    if cell[2] == 8:
                        frac = self.core.get_fraction_status(self.file, self.fraction)
                        self.core.change_fraction_status(self.file, self.fraction, frac[1], frac[2], frac[3], frac[4], frac[5]+1)
                        self.core.change_cell(cell[0], cell[1], 8, self.fraction, 0, self.file)
                return False, stage,last_x,last_y,armies_lists
            elif ((cell[3]== self.fraction) and (cell[4]!=0)):
                list_start = self.core.load_army(self.file,self.id_army)
                list_end = self.core.load_army(self.file, cell[4])
                list_resoult = []
                for i in range(len(list_start)-3):
                    if i == 0:
                        list_resoult.append(list_end[i])
                    else:
                        list_resoult.append(list_start[i]+list_end[i])
                list_resoult.append(20)
                list_resoult.append(0)
                list_resoult.append(self.fraction)
                self.core.change_army(self.file, list_resoult[0], list_resoult[1], list_resoult[2], list_resoult[3], list_resoult[4], list_resoult[5], list_resoult[6], list_resoult[7], list_resoult[8])
                self.core.change_army(self.file, self.id_army,0,0,0,0,0,0,0,0)
                cell = self.core.load_cell(self.army_coords[0],self.army_coords[1],self.file)
                self.core.change_cell(self.army_coords[0],self.army_coords[1],cell[2],0,0,self.file)
                self.reload_window(last_x,last_y)
#            elif (((cell[2]>=7)) and (cell[4] == 0)):
#                stage = 5
#                return False, stage,last_x,last_y,armies_lists            
            else:
                return False,3,last_x,self.last_y,armies_lists

    def battle_dialog_window(self):
        textures = self.resources.textures_for_battle_gialog_window()
        first_textures = textures[0].get_rect()
        first_textures.center=(450,350)
        self.display.blit(textures[0],first_textures)
        for i in range(3):
            first_textures = textures[i+1].get_rect()
            first_textures.center=(350+100*i,450)
            self.display.blit(textures[i+1],first_textures)
        font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)       

        pygame.display.flip()
    
    def winrar_window(self,fraction):                
        textures = self.resources.textures_for_battle_gialog_window()
        first_textures = textures[0].get_rect()
        first_textures.center=(450,350)
        font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
        item = u'Fraction '+str()
        font1 = font1.render(item,0,(20,20,20))
        self.display.blit(font1,(385,360)) 
        
    def action_to_minimap_coords(self,x,y): #вернуть стартовые х и у!
        self.Load_part_of_map(x,y)
        cells_list,x_coord_start,y_coord_start = self.core.load_cells(x, y, self.file)
        cell = Rect((800+x_coord_start*self.step_p,0+y_coord_start*self.step_p),(self.step_p*14,self.step_p*14))
        self.load_cells_list()
        self.Minimap()
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        self.Maps_grid()
        return x_coord_start,y_coord_start
    
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
        
    def action_for_load(self,text):
        cell = Rect((360,260),(300,200))
        pygame.draw.rect(self.display,(204,204,204),cell,0)
        cell = Rect((385,280),(250,50))
        pygame.draw.rect(self.display,(255,255,204),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        filename = pygame.font.SysFont("Times New Roman", 20, bold=False, italic=True)
        font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
        font2 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)        
        item = u'Press enter for load'
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

