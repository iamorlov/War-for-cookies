# -*- coding: utf-8 -*-
'''
Created on 16 черв. 2013

@author: antimoskal
'''
import pygame
from ResManager import *

class Resources():
    
    def __init__(self):
        self.manager = ResManager()
        
    def textures(self):
        manager = ResManager()
        textures = []
        texture = manager.get_image("grass.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("sand.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("dirt.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("water.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("tree.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("rock.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("lava.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("farm.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("mine.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)
        texture = manager.get_image("base_blue.png")
        texture = pygame.transform.scale(texture,(50,50))
        textures.append(texture)        
        texture = manager.get_image("base_red.png")
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
