# -*- coding: utf-8 -*-

import pygame

class Transparent:
    def __init__(self, time = 2000, show = True):
        self.show = show
        self.set_time(time)
        self.run = False

    def update(self, dt):
        if self.run:
            self.add += float(dt) * self.time
            if int(self.add) > 0:
                self.count += int(self.add)
                self.add = self.add - int(self.add)
                if self.count > 255:
                    self.count = 255
                    self.run = False

    def start(self):
        self.count = 0
        self.add = float(0)
        self.run = True

    def is_start(self):
        return self.run

    def stop(self):
        self.run = False

    def set_time(self, time = 2000):
        self.time = float(255)/float(time)

    # Как видите мы изменяем копию спрайта, да и сам спрайт не храним
    def get_sprite(self,sprite):
        sprite_copy = sprite.copy()
        if self.show:
            sprite_copy.fill((0,0,0,255-self.count), None, pygame.BLEND_RGBA_SUB)
        else:
            sprite_copy.fill((0,0,0,self.count), None, pygame.BLEND_RGBA_SUB)
        return sprite_copy

    def toggle(self):
        self.show = not self.show
