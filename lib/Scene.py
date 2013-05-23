# -*- coding: utf-8 -*-

import pygame
import const

class Scene:
    def __init__(self, next_scene = None):
        self.__next_scene = next_scene

    def loop(self, dt):
        self.__event(pygame.event)
        self._update(dt)
        self._draw(dt)

    def start(self, display, manager):
        self.display = display
        self.manager = manager
        self._start()
        self.__end = False

    # Эту функцию стоит определит в потомке если в
    # сцене нужно что-то создать, например наш логотип.
    def _start(self):
        pass

    # Эта функция которая не должна вызываться вне этого класса,
    # ну и вы конечно поняли зачем нужно __.
    def __event(self, event):
        if len(event.get(pygame.QUIT)) > 0:
            self.__end = True
            self.set_next_scene(None)
            return

        self._event(event)

        # event.get() эквивалентен pygame.event.get()
        # передавая параметр в get мы говорим что именно
        # нас интересует из событий.
        for e in event.get(const.END_SCENE):
            if e.type == const.END_SCENE:
                self.__end = True

    # Эту функцию придется переопределить в потомке
    def _draw(self, dt):
        pass

    # и эту тоже
    def _event(self, event):
        pass

    # как и эту.
    def _update(self, dt):
        pass

    def next(self):
        return self.__next_scene

    def is_end(self):
        return self.__end

    def the_end(self):
        pygame.event.post(pygame.event.Event(const.END_SCENE))

    def set_next_scene(self, scene):
        self.__next_scene = scene
