# -*- coding: utf-8 -*-
import pygame, sys,resources, battle
class Battle_window():
    def __init__(self, attacker, b_map_name):
        pygame.init()
        self.w_event = Events()
        self.fraction = attacker # першими ходять атакуючі
        self.b_map_name = b_map_name
        self.battle = Battle()
        self.resources = Resources()
        
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
        textures_army = self.resources.textures_for_army()
        cells_list,x_coord_start,y_coord_start= self.core.load_cells(x,y,self.file)
        for i in range(self.big_steps_x):
            for j in range(self.big_steps_y):
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