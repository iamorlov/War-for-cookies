# -*- coding: utf-8 -*-
import pygame, sys,resources, battle, Core,events
class Battle_window():
    def __init__(self, x,y, current_name):# Где начался бой
        pygame.init()
        self.w_event = events.Events()
        self.fraction = attacker # першими ходять атакуючі
        battle_cell=core.load_cell(x,y,current_name)
        self.b_map_name = battle_cell[2]
        self.battle = battle.Battle()
        self.resources = resources.Resources()
        self.file = current_name
        self.indent_x=100
        self.indent_y=50
        
    def load_cells_list(self):
        self.cells_list = self.core.load_battle_cells(self.file)
        
    def b_window(self):
        self.display = pygame.display.set_mode((1280,720))
        manager = ResManager()
        pygame.display.set_icon(manager.get_image('icon.png'))
        pygame.display.set_caption('Battle')
        self.map_type = self.core.load_file(self.b_map_name,self.file)
        self.display.fill((220,220,250))
        pygame.display.flip()
        
        
    def Maps_grid(self):
        self.big_step = 50#величина клетки в пикселях
        self.big_steps_x = 20#кол-во клеток по ширине
        self.big_steps_y = 11#по высоте
        pygame.display.flip()
        
    def load_battle_map(self,x,y):
        textures = self.resources.textures()
        textures_army = self.resources.textures_for_army()#перепахать на юнитов
        units=[]
        load_battle_cells(current_name)
        for i in range(self.big_steps_x):
            for j in range(self.big_steps_y):
                cell_type = self.cells_list[i*self.big_steps+j][2]
                unit=self.cells_list[i*self.big_steps+j][3])
                if(unit > 0):
                    first_texture = textures[cell_type].get_rect()
                    first_texture.center=(self.indent_x+self.big_step*i, self.indent_y+self.big_step*j)
                    self.display.blit(textures_army[fraction*5+fraction][unit],first_texture)
                else:
                    first_texture = textures[cell_type].get_rect()
                    first_texture.center=(self.indent_x+self.big_step*i,self.indent_y+self.big_step*j)
                    self.display.blit(textures[cell_type],first_texture)               
        self.Maps_grid()
        pygame.display.flip()