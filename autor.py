# -*- coding: utf-8 -*-
import pygame, os, lib
class autor():
    def __init__(self):
        pygame.init()
    def background(self):
       background = pygame.image.load('data/image/autors.png')#Фон!!!!!!!!!!!!!!!!!
       self.screen=pygame.display.set_mode((1200,720))
       self.screen.blit(background, (0,0))
       pygame.display.flip()
    def autor_print(self):
        self.background()
        filename = pygame.font.SysFont("Times New Roman", 20, bold=False, italic=True)
        font1 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
        font2 = pygame.font.SysFont("Monospace", 20, bold=True, italic=False)
        item = u'Press enter for save'
        item = u'Press enter for save'
        item = u'Press enter for save'
        font1 = font1.render(item,0,(225,225,225))
        self.screen.blit(font1,(455,290))
        pygame.display.update()

    
