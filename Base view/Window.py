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
        self.count = 0
        
    def Main_Window(self):
        self.display = pygame.display.set_mode((1280,700))
        manager = ResManager()
        pygame.display.set_icon(manager.get_image('icon.png'))
        pygame.display.set_caption("Map Editor")
        self.display.fill((200,220,100))
        pygame.display.flip()
        i = 0
    
    def slots_for_base(self):
        manager = ResManager()
        texture = manager.get_image("interface_bg.png")
        for i in range(3):
            first_texture = texture.get_rect()
            first_texture.center=(500,90+160*i)
            self.display.blit(texture,first_texture)
        pygame.display.update()  
               