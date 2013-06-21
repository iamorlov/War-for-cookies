# -*- coding: utf-8 -*-
'''
Created on 16 черв. 2013

@author: antimoskal
'''
import pygame
from lib import ResManager

class Resources():
    
    def __init__(self):
        self.manager = ResManager()
        
    def textures(self):
        textures = []
        texture = self.manager.get_terrain("grass.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("sand.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("dirt.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("water.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("tree.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("rock.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("lava.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("farm.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("mine.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = self.manager.get_terrain("base_blue.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)        
        texture = self.manager.get_terrain("base_red.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        return textures
    
    def colours(self):
        colour = []
        for i in range(11):
            if i == 0:
                colour.append((0,204,0))
            elif i == 1:
                colour.append((255,204,0))
            elif i == 2:
                colour.append((153,102,51))
            elif i == 3:
                colour.append((51,51,255))
            elif i == 4:
                colour.append((51,102,51))
            elif i == 5:
                colour.append((204,204,153))
            elif i == 6:
                colour.append((204,204,102))
            elif i == 7:
                colour.append((225,225,102))
            elif i == 8:
                colour.append((0,0,0))
            elif i == 9:
                colour.append((255,51,0))
            elif i == 10:
                colour.append((51,0,255))
        return colour

    def arrows(self):
        textures = []
        for i in range(4):
            texture = self.manager.get_image("free-go"+str(i+1)+".png")
            texture = pygame.transform.scale(texture,(50,50))
            textures.append(texture)        
        for i in range(4):
            texture = self.manager.get_image("enemy-go"+str(i+1)+".png")
            texture = pygame.transform.scale(texture,(50,50))
            textures.append(texture)
        return textures
    
    def textures_for_army(self):
        textures = []
        fraction = ['neutral','red','blue']
        type_units=['','_ak47','_m4a','_rpg','_tank','_artillery']
        for i in range(len(fraction)):
            for j in range(len(type_units)):
                texture = self.manager.get_units(fraction[i]+type_units[j]+".png")
                texture = pygame.transform.scale(texture,(50,50))
                textures.append(texture)  
        return textures