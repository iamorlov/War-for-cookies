# -*- coding: utf-8 -*-
import pygame, sys
from Core import *
from ResManager import *

#Після того, як більша частина функціоналу буде працювати
#треба розділити вітку для версії з текстурами та версії з
#з кольорами клітинок замість них
#


class Window(Core): #Люди, користуйтеся цим кодом для виконання завдань по рпз. Я хз поки, чому перше перемалювання вікна йде 3,5 секунд :((((((
    def __init__(self,map_name):
        pygame.init()
        self.minimap_x =0
        self.minimap_y =0
        self.count = 0
        self.days = 0
        self.fraction = 1 # першими ходять червоні
        self.map_name = map_name
        
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
        cell = Rect((800,0),(300,300))
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        pygame.display.flip()
        
    def colours(self): # замінити на текстури #Для вітки без текстур
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
    
    def Textures(self):
        manager = ResManager()
        self.textures = []
        texture = manager.get_image("grass.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("sand.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("dirt.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("water.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("tree.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("rock.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("lava.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("farm.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("mine.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        texture = manager.get_image("base_blue.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)        
        texture = manager.get_image("base_red.png")
        texture = pygame.transform.scale(texture,(50,50))
        self.textures.append(texture)
        pygame.display.flip() 

    def load_cells_list(self):
        self.cells_list = self.load_minimap_cells()

    def Minimap(self):
        self.colours()
        for i in range(self.steps):
            for j in range(self.steps):
                cell = Rect((800+self.step_p*i,self.step_p*j),(self.step_p,self.step_p))
                cell_type = self.cells_list[i*self.steps+j][2]
                pygame.draw.rect(self.display,self.colour[cell_type],cell,0)
        pygame.display.flip()
        self.Minimaps_grid()

    def moving_army(self):
        pass
           
    def Get_minimap_coords(self,click_coords):                 
        if ((click_coords[0] > 800) and (click_coords[1] > 0) and (click_coords[0] < 1100) and (click_coords[1] < 300)):
            self.minimap_x = (click_coords[0]-800)//self.step_p
            self.minimap_y = (click_coords[1])//self.step_p
            self.Load_part_of_map()
            cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*14,self.step_p*14))
            self.load_cells_list()
            self.Minimap()
            pygame.draw.rect(self.display,(0,0,0),cell,2)
            self.Maps_grid()
            #self.Minimap()

    def Get_map_coords(self,click_coords):                
        if ((click_coords[0] > 20) and (click_coords[1] > 0) and (click_coords[0] < 720) and (click_coords[1] < 700)):
            self.x_coord = (click_coords[0]-20)//self.big_step
            self.y_coord = (click_coords[1])//self.big_step
#            self.change_cell(self.y_coord+self.y_coord_start,self.x_coord+self.x_coord_start,  self.cell_type, 0, 0)
            
#            first_texture = self.textures[self.cell_type].get_rect()
#            first_texture.center=(35+self.x_coord*self.big_step,14+self.y_coord*self.big_step)
#            self.display.blit(self.textures[self.cell_type],first_texture)   
#            cell = Rect((self.x_coord*self.big_step+20, self.y_coord*self.big_step),(self.big_step,self.big_step))

#            print self.cell_type
#            pygame.draw.rect(self.display,self.colour[self.cell_type],cell,0)
            self.Maps_grid()
            pygame.display.flip()
###
###
###ЗАВТРА ОБОВ’ЯЗКОВО ДОРОБИТИ!!!!!
###
###
    def event_scan_keyes(self):
        pygame.event.clear()
        for event in pygame.event.get():
            print type(event)
            print event.type
            if event.type == KEYDOWN:
                print event.type
                print type(event.key)
                name_key =(re.search('[a-z]',pygame.key.name(event.key)))
                if name_key != None:
                    text = (name_key).group(0)
                    return text
                else:
                    return ''
            else:
                print 'lol'
                return 'lol'
                
                        
    
    def window_for_save(self):
        pygame.event.clear()
        cell = Rect((360,260),(300,200))
        pygame.draw.rect(self.display,(204,204,204),cell,0)
        cell = Rect((385,280),(250,50))
        pygame.draw.rect(self.display,(255,255,204),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        #text = pygame.font.SysFont(name, size, bold, italic)
        font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
        font2 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)        
        item = u'Press enter for save'
        item2 = u'Press ESC for exit'
        font1 = font1.render(item,0,(20,20,20))
        self.display.blit(font1,(385,360))
        font2 = font2.render(item2,0,(20,20,20))
        self.display.blit(font2,(385,410))
        text = ''

        pygame.display.update()
        print text
        time.sleep(1)
#        event = pygame.event.wait()
#        print pygame.key.name(event.key)
        for i in range (7):
            print type(self.event_scan_keyes())
            text += self.event_scan_keyes()
        pygame.display.update()
        pygame.event.clear()
        print text

    def Reload_window(self):
        self.Maps_grid()
        self.Minimaps_grid()
        self.Minimap()
        self.Type_of_grids()
        pygame.display.flip()
                
#    def Save_map(self,event):
#        if event.type == KEYDOWN:
#            if event.key == K_F5:
#                self.       
    
    def Events(self):
 
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
                    self.window_for_save()
                    
    def Load_part_of_map(self):
        cells_list = self.load_cells(self.minimap_x, self.minimap_y)
        for i in range(self.big_steps):
            for j in range(self.big_steps):
                cell_type = cells_list[i*self.big_steps+j][2]
                fraction  = cells_list[i*self.big_steps+j][3]
                if (cell_type >6) and (cell_type<12):
                    print 'start coords = '+str(i)+' '+str(j)
                    mass_cell_type = []
                    for k in range(3):
                        for z in range(3):
                            print 'coords = '+str(i+k-1)+' '+str((j+z-1))
                            type_cell = cells_list[(i+k-1)+(j+z-1)*self.big_steps][2]# ТУТ БАГ!!!!!!!!!!! ТРЕБА СТВОРИТИ ПРОЦЕДУРУ ДЛЯ ОБРОБКИ ОБЛАСТІ 3х3 на глобальній карті
                            print type_cell
                            if (type_cell !=3) and (type_cell <6):
                                mass_cell_type.append(type_cell)
                    types = [0,0,0,0,0,0]
                    for k in range(0,len(mass_cell_type)):
                        if mass_cell_type[k] == 0:
                            types[0]+=1;
                        elif mass_cell_type[k] == 1:
                            types[1]+=1;
                        elif mass_cell_type[k] == 2:
                            types[2]+=1;
                        elif mass_cell_type[k] == 4:
                            types[3]+=1;
                        elif mass_cell_type[k] == 5:
                            types[4]+=1;
                        elif mass_cell_type[k] == 6:
                            types[5]+=1;
                    max_cells = max(types)
                    for k in range(0,len(types)):
                        if (max_cells == types[k]):
                            if k <3:
                                result_type = k
                            else:
                                result_type = k+1
                    first_texture = self.textures[result_type].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(self.textures[result_type],first_texture) 
                if (fraction > 0) and (cell_type == 9):
                    first_texture = self.textures[cell_type+fraction-1].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(self.textures[cell_type+fraction-1],first_texture)
                else:
                    first_texture = self.textures[cell_type].get_rect()
                    first_texture.center=(45+self.big_step*i,25+self.big_step*j)
                    self.display.blit(self.textures[cell_type],first_texture)               
#                cell = Rect((20+self.big_step*i,self.big_step*j),(self.big_step,self.big_step))
#                
#                pygame.draw.rect(self.display,self.colour[cell_type],cell,0)
                print '  '
        cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*14,self.step_p*14))
        self.Minimap()
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        self.Maps_grid()
        pygame.display.flip()
                
        #print str(self.x_coord_start)+'  '+str(self.y_coord_start)
        #print cells_list
# 28x28, 25x25 cells
    def Rewrite_cell(self):
        self.Events()


    def Run(self):
        start = time.time()
        self.Main_Window()
        finish = time.time()
        print (finish - start)
        
        start = time.time() 
        self.load_cells_list()
        finish = time.time()
        print (finish - start)
        
        start = time.time() 
        self.Maps_grid()
        finish = time.time()
        print (finish - start)
                
        start = time.time() 
        self.Minimaps_grid()
        finish = time.time()
        print (finish - start)
                
        start = time.time() 
        self.Minimap()
        finish = time.time()
        print (finish - start)
        self.Textures()
        start = time.time() 
        self.Load_part_of_map()
        finish = time.time()
        print (finish - start)
        
        print (finish - start)
        while True:
            self.Rewrite_cell()

