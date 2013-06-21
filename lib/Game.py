# -*- coding: utf-8 -*-

import pygame
from ResManager import ResManager

class Game:
    # ширина и высота окна,
    # цвет которым будет залит нарисованный экран,
    # максимальный fps
    def __init__(self,
                 width   = 1280,
                 height  = 720,
                 color   = (255,255,255),
                 fps     = 40,
                 scene   = None,
                 manager = ResManager()):
        pygame.init()

        self.set_display(width, height)

        self.fps       = fps
        self.__manager = manager
        self.scene     = scene

       # self.__display.fill(color)
        pygame.display.flip()

    # Создаем окно
    def set_display(self, width, height):
        self.__display = pygame.display.set_mode((width, height))

    def set_caption(self, title = None, icon = None):
        if title == None:
            pygame.display.set_caption("game")
        else:
            pygame.display.set_caption(title)

        if icon != None:
            pygame.display.set_icon(self.__manager.get_image(icon))

    def game_loop(self):
        # Если сцены нет, то все заканчивается.
        while self.scene != None:
            clock = pygame.time.Clock()
            dt    = 0

            # Инициализируем сцену, даем ей холст для рисования и ResManager.
            self.scene.start(self.__display, self.__manager)

            while not self.scene.is_end():
                # говорим сколько времени прошло, события получаются
                # стандартным для pygame образом через pygame.event
                self.scene.loop(dt)

                pygame.display.flip()

                dt = clock.tick(self.fps)

            # Сцена знает что будет после ее завершения.
            self.scene = self.scene.next()
