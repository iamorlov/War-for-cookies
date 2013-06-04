# -*- coding: utf-8 -*-
import pygame, sys
from Core import *
from ResManager import *

#Після того, як більша частина функціоналу буде працювати
#треба розділити вітку для версії з текстурами та версії з
#з кольорами клітинок замість них
#


class Window(Core): #Люди, користуйтеся цим кодом для виконання завдань по рпз. Я хз поки, чому перше перемалювання вікна йде 3,5 секунд :((((((
    def __init__(self):
        pygame.init()
        self.cell_type = 0
        self.minimap_x =0
        self.minimap_y =0
        self.count = 0
        
    def Main_Window(self):
        self.display = pygame.display.set_mode((1200,720))
        manager = ResManager()
        pygame.display.set_icon(manager.get_image('icon.png'))
        pygame.display.set_caption("Map Editor")
        self.empty_map(0)
        self.display.fill((250,250,250))
        pygame.display.flip()
        i = 0
        
    def Maps_grid(self):
        self.big_step = 28
        self.big_steps =25
        for i in range(self.big_steps):
            for j in range(self.big_steps):
                cell = Rect((20+self.big_step*i,self.big_step*j),(self.big_step,self.big_step))
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
    
    def keyboard_constants(self,type): #повертає символи замість типу подій при натиску на клавішу
        for i in range(26):
            if type == 'K_a':  return 'a'
            elif type == 'K_b':return 'b'
            elif type == 'K_c':return 'c'
            elif type == 'K_d':return 'd'
            elif type == 'K_e':return 'e'
            elif type == 'K_f':return 'f'
            elif type == 'K_g':return 'g'
            elif type == 'K_h':return 'h'
            elif type == 'K_i':return 'i'
            elif type == 'K_j':return 'j'
            elif type == 'K_k':return 'k'
            elif type == 'K_l':return 'l'
            elif type == 'K_m':return 'm'
            elif type == 'K_n':return 'n'
            elif type == 'K_o':return 'o'
            elif type == 'K_p':return 'p'
            elif type == 'K_q':return 'q'
            elif type == 'K_r':return 'r'
            elif type == 'K_s':return 's'
            elif type == 'K_t':return 't'
            elif type == 'K_u':return 'u'
            elif type == 'K_v':return 'v'
            elif type == 'K_w':return 'w'
            elif type == 'K_x':return 'x'
            elif type == 'K_y':return 'y'
            elif type == 'K_z':return 'z'        
                
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
    
    def Type_of_grids(self):       
        # Ололо, я індус
        self.colours()
        for i in range(3):
            for j in range(3):             
                cell = Rect((850+50*i,350+50*j),(50,50))
                pygame.draw.rect(self.display,self.colour[i+j*3],cell,0)
        for i in range(3):
            for j in range(3):
                cell = Rect((850+50*i,350+50*j),(50,50))
                pygame.draw.rect(self.display,(0,0,0),cell,1)
        cell = Rect((875,500),(50,50))
        ## червоний 
        pygame.draw.rect(self.display,(255,51,0),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,1)
        cell = Rect((925,500),(50,50))
        ## cиній
        pygame.draw.rect(self.display,(51,0,255),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,1)
        pygame.display.flip()
        self.load_cells(5, 30)
           
    def Get_cell_type(self,click_coords):
        if ((click_coords[0] > 850) and (click_coords[1] > 350) and (click_coords[0] < 1050) and (click_coords[1] < 500)):
            x_coord = (click_coords[0]-850)//50
            y_coord = (click_coords[1]-350)//50
            self.cell_type = x_coord+y_coord*3

        if ((click_coords[0] > 875) and (click_coords[1] > 500) and (click_coords[0] < 975) and (click_coords[1] < 550)):
            x_coord = (click_coords[0]-875)//50
            y_coord = (click_coords[1]-500)//50
            self.cell_type = x_coord+y_coord+9

    def Get_minimap_coords(self,click_coords):                 
        if ((click_coords[0] > 800) and (click_coords[1] > 0) and (click_coords[0] < 1100) and (click_coords[1] < 300)):
            self.minimap_x = (click_coords[0]-800)//self.step_p
            self.minimap_y = (click_coords[1])//self.step_p
            self.Load_part_of_map()
            cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*25,self.step_p*25))
            self.load_cells_list()
            self.Minimap()
            pygame.draw.rect(self.display,(0,0,0),cell,2)
            self.Maps_grid()
            #self.Minimap()

    def Get_map_coords(self,click_coords):                
        if ((click_coords[0] > 20) and (click_coords[1] > 0) and (click_coords[0] < 720) and (click_coords[1] < 700)):
            self.x_coord = (click_coords[0]-20)//self.big_step
            self.y_coord = (click_coords[1])//self.big_step
            self.change_cell(self.y_coord+self.y_coord_start,self.x_coord+self.x_coord_start,  self.cell_type, 0, 0)
            cell = Rect((self.x_coord*self.big_step+20, self.y_coord*self.big_step),(self.big_step,self.big_step))
            print self.cell_type
            pygame.draw.rect(self.display,self.colour[self.cell_type],cell,0)
            self.Maps_grid()
            pygame.display.flip()
###
###
###ЗАВТРА ОБОВ’ЯЗКОВО ДОРОБИТИ!!!!!
###
###
    def window_for_save(self):
        cell = Rect((360,260),(300,200))
        pygame.draw.rect(self.display,(204,204,204),cell,0)
        
        cell = Rect((385,280),(250,50))
        pygame.draw.rect(self.display,(255,255,204),cell,0)
        pygame.draw.rect(self.display,(0,0,0),cell,2)
        
        #text = pygame.font.SysFont(name, size, bold, italic)
        font      = pygame.font.SysFont("Monospace", 40, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Monospace", 40, bold=True, italic=False)        
        item = u'Press enter for save'
        font.render(item,True,(20,20,20))
        font_bold.render(item,True,(20,20,20))
        
        
        
        pygame.display.flip()

    def Reload_window(self):
        self.display.fill((250,250,250))
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
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_coords = event.pos
                    self.Get_cell_type(click_coords)
                    self.Get_map_coords(click_coords)
                    self.Get_minimap_coords(click_coords)
            if event.type == QUIT:
                sys.exit()

    def Load_part_of_map(self):
        cells_list = self.load_cells(self.minimap_x, self.minimap_y)
        for i in range(self.big_steps):
            for j in range(self.big_steps):
                cell = Rect((20+self.big_step*i,self.big_step*j),(self.big_step,self.big_step))
                cell_type = cells_list[i*self.big_steps+j][2]
                pygame.draw.rect(self.display,self.colour[cell_type],cell,0)
        cell = Rect((800+self.x_coord_start*self.step_p,0+self.y_coord_start*self.step_p),(self.step_p*25,self.step_p*25))
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
        
        start = time.time() 
        self.Load_part_of_map()
        finish = time.time()
        print (finish - start)
        
        start = time.time() 
        self.Type_of_grids()
        finish = time.time()
        print (finish - start)
        self.window_for_save()
        while True:
            self.Rewrite_cell()

