#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time, pygame
from pygame.locals import *

# Этот класс отвечает за загрузку ресурсов.
class ResManager:
    # При инициализации класса мы указываем где у нас что находится.
    def __init__(self,
                 data_dir = 'data',
                 image_dir = 'image',
                 sound_dir = 'sound',
                 music_dir = 'music'):
        # Это корневой каталог ресурсов
        self.data_dir = data_dir
        # Это каталог с изображениями
        self.image_dir = image_dir
        # Это каталог со звуками
        self.sound_dir = sound_dir
        # Это каталог с музыкой
        self.music_dir = music_dir

    # Этот метод загружает файл по имени.
    def get_image(self, name):
        # Получаем имя нужного нам файла вместе с путями к нему.
        fullname = os.path.join(self.data_dir,
                                os.path.join(self.image_dir, name))

        try:
            # Пробуем загрузить изображение
            image = pygame.image.load(fullname)
        except pygame.error, message:
            # Если это не удалось сообщаем об этом и кидаем исключение
            # на выход, так как отсутствие нужно изображения,
            # критичная ошибка.
            print('Cannot load image: {0}'.format(name))

            raise SystemExit, message
        else:
            # Мы используем изображения с поддержкой альфа канала,
            # потому и конвертируем изображение в формат удобный pygame c
            # учетом этого самого альфа канала.
            image = image.convert_alpha()

            return image
