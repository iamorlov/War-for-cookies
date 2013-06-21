# -*- coding: utf-8 -*-
import os, time, pygame
from pygame.locals import *

class ResManager:
    def __init__(self,
                 data_dir = 'data',
                 image_dir= 'image',
                 sound_dir= 'sound',
                 music_dir= 'music',
                 textures_dir = 'textures',
                 terrain_dir = 'terrain',
                 arrows_dir = 'arrows',
                 units_dir = 'map_units'):
        self.data_dir = data_dir
        self.image_dir = image_dir
        self.sound_dir = sound_dir
        self.music_dir = music_dir
        self.textures_dir = textures_dir
        self.terrain_dir = terrain_dir
        self.arrows_dir = arrows_dir
        self.units_dir = units_dir

    def get_image(self,name):
        fullname = os.path.join(self.data_dir, os.path.join(self.image_dir,name))
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print('Cannot load image; {0}'.format(name))
            raise SystemExit, message
        else:
            image = image.convert_alpha()
            return image
        
    def get_terrain(self,name):
        fullname = os.path.join(self.data_dir, os.path.join(self.textures_dir, os.path.join(self.terrain_dir,name)))
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print('Cannot load image; {0}'.format(name))
            raise SystemExit, message
        else:
            image = image.convert_alpha()
            return image
    
    def get_arrows(self,name):
        fullname = os.path.join(self.data_dir, os.path.join(self.textures_dir, os.path.join(self.arrows_dir,name)))
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print('Cannot load image; {0}'.format(name))
            raise SystemExit, message
        else:
            image = image.convert_alpha()
            return image
        
    def get_units(self,name):
        fullname = os.path.join(self.data_dir, os.path.join(self.units_dir, name))
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print('Cannot load image; {0}'.format(name))
            raise SystemExit, message
        else:
            image = image.convert_alpha()
            return image        