#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, pygame, lib
#from autor import autor
def get_center(surface, sprite):
    return (surface.w/2 - sprite.w/2,
            surface.h/2 - sprite.h/2)

# Эта сцена ожидания наследуется от нашей сцены из lib
class WaitScene(lib.Scene):
    def __init__(self, time = 1000, *argv):
        lib.Scene.__init__(self, *argv)
        self.run = 0
        self.time = time
        self.music_counter = 0

    def _event(self, event):
        # Здесь нам нужно обработать все события.
        # Если есть объекты которым нужны события их нужно
        # оповестить здесь, так как event.get() отчищает очередь событий,
        # а в объектах нужно брать из очереди только нужные события.
        # Здесь можно обработать все.
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                self.the_end()
                self.set_next_scene(MenuScene())
        if not self.run < self.time:
            self.the_end()

    def _update(self, dt):
        self.run += dt

# Эта сцена позволит показать наш логотип
class ShowScene(lib.Scene):
    # Как видите мы создаем при старте сцены наш логотип(загружая его из файла)
    # и анимацию.
    def _start(self):
        sprite = self.manager.get_image('logo.png')
        self.sprite = pygame.transform.scale(sprite, (sprite.get_rect().w ,
                                             sprite.get_rect().h))

        self.plambir = lib.Transparent(3000)
        self.plambir.start()

    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                self.the_end()
                self.set_next_scene(MenuScene())

        if not self.plambir.is_start():
            self.the_end()

    def _update(self, dt):
        self.plambir.update(dt)

    def _draw(self, dt):
        self.display.fill((255,255,255))
        # Как видите мы рисуем логотип, сначала пропустив его через анимацию
        # прозрачности.
        self.display.blit(self.plambir.get_sprite(self.sprite),
                          get_center(self.display.get_rect(),
                                     self.sprite.get_rect()))

# Эта сцена исчезновения логотипа, так как она не особо от сцены
# появления отличается, мы просто кое что изменим в инициализации
# класса ShowScene.
class HideScene(ShowScene):
    def _start(self):
        ShowScene._start(self)

        self.plambir.toggle()
        self.plambir.set_time(1000)

class Menu(lib.Game, lib.Scene):
    def __init__(self, position = (0,0), loop = True):
        self.index = 0
        self.x = position[0]
        self.y = position[1]
        self.menu = list()
    # Метод перемещающий нас циклично в низ по всем элементам.
    def down(self):
        self.index += 1
        if self.index >= len(self.menu):
            self.index = 0

    # Тоже самое но в вверх.
    def up(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.menu)-1
    def background(self):
       background = pygame.image.load('data/image/menu.png')#Фон!!!!!!!!!!!!!!!!!
       self.screen=pygame.display.set_mode((1280,720))
       self.screen.blit(background, (0,0))
       pygame.display.flip()
    # Добавляет новый элемент, нужно передать 2 изображения.
    # На 1 не выбранный вид элемента.
    # На 2 выбранный элемент
    def add_menu_item(self, no_select, select, func):
        self.menu.append({ 'no select' : no_select,
                           'select' : select,
                           'func' : func })

    def call(self):
        self.menu[self.index]['func']()

    def draw(self, display):
        index = 0
        x = self.x
        y = self.y
        for item in self.menu:
            if self.index == index:
                display.blit(item['select'], (x, y))
                y += item['select'].get_rect().h
            else:
                display.blit(item['no select'], (x, y))
                y += item['no select'].get_rect().h
            index += 1

class MenuScene(lib.Scene):
    def __init__(self):
        self.music_counter = 0
    def music(self,i): #для музона 0 стоп остальное играть
         pygame.mixer.music.load('data/music/menu.ogg')
         pygame.mixer.music.play()
         if(i==0):
          pygame.mixer.music.stop()
         if(i==1):
          pygame.mixer.pause()
         if(i==2):
          pygame.mixer.unpause()
    def clix(self):
         e=pygame.mixer.Sound('data/music/clix1.ogg')
         e.play()
    def video(self):
        overlay = pygame.display.set_mode((800,600))
        m=pygame.movie.Movie('data/video/preview234.mpg')
        m.set_display(overlay)
        m.play()
        pygame.display.flip()
        
    def empty_func(self):
        pass
    
    def item_call(self):
        self.menu = Menu((250,110))
        # Именно таким образом мы можем получить текст в pygame
        # В данном случае мы используем системный шрифт.        
        font_text = pygame.font.SysFont("Verdana", 30, bold=False, italic=False)
        font      = pygame.font.SysFont("Verdana", 50, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Verdana", 50, bold=True, italic=False)
        self.menu.background()
        # Загрузка музыки.
        #pygame.mixer.music.load('data/music/menu.ogg')
        # Проигрывание музыки.
        #pygame.mixer.music.play()
        if self.music_counter == 0:
            self.music(1)
            self.music_counter = 1
        item = u"Beta версия игры, элемент в разработке"
        self.menu.add_menu_item(font_text.render(item,True,(255,255,255)),
                                font_text.render(item,True,(255,255,255)),
                                self.empty_func)
        item = u"Назад"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self._start)
    def fun_exit(self):#кнопка закрыть
        exit(1)
    def autor_print(self):
        self.menu = Menu((250,110))
        # Именно таким образом мы можем получить текст в pygame
        # В данном случае мы используем системный шрифт.        
        font_text = pygame.font.SysFont("Verdana", 30, bold=False, italic=False)
        font      = pygame.font.SysFont("Verdana", 50, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Verdana", 50, bold=True, italic=False)
        self.menu.background()
        # Загрузка музыки.
        #pygame.mixer.music.load('data/music/menu.ogg')
        # Проигрывание музыки.
        #pygame.mixer.music.play()
        if self.music_counter == 0:
            self.music(1)
            self.music_counter = 1
        item = u"Evgen `Azon` Darnapuk"
        self.menu.add_menu_item(font_text.render(item,True,(255,255,255)),
                                font_text.render(item,True,(255,255,255)),
                                self.empty_func)
        item = u"Roman `Merorh` Lukov"
        self.menu.add_menu_item(font_text.render(item,True,(255,255,255)),
                                font_text.render(item,True,(255,255,255)),
                                self.empty_func)
        item = u"Vadim `Heiker` Orlov"
        self.menu.add_menu_item(font_text.render(item,True,(255,255,255)),
                                font_text.render(item,True,(255,255,255)),
                                self.empty_func)
        item = u"Igor `KIO` Kandyba"
        self.menu.add_menu_item(font_text.render(item,True,(255,255,255)),
                                font_text.render(item,True,(255,255,255)),
                                self.empty_func)
        item = u"Denis Goncharow"
        self.menu.add_menu_item(font_text.render(item,True,(255,255,255)),
                                font_text.render(item,True,(255,255,255)),
                                self.empty_func)
        item = u"Назад"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self._start)
    def game_window(self):
        self.music(0)
        a = lib.Window('first_map_for_test')
        a.Run()
    def map_editor_0(self):
        self.music(0)
        a = lib.lib_map_editor.Window(0,'')
        a.Run()
    
    def map_editor_1(self):
        self.music(0)
        a = lib.lib_map_editor.Window(1,'')
        a.Run()    
    
    def map_editor_2(self):
        self.music(0)
        a = lib.lib_map_editor.Window(2,'')
        a.Run()
        
    def map_editor_last(self):
        self.music(0)
        a = lib.lib_map_editor.Window(3,'temp')
        a.Run()

    def bmap_editor_0(self):
        self.music(0)
        a = lib.lib_map_editor_battle_map.Window(0,'')
        a.Run()
    
    def bmap_editor_1(self):
        self.music(0)
        a = lib.lib_map_editor_battle_map.Window(1,'')
        a.Run()    
    
    def bmap_editor_2(self):
        self.music(0)
        a = lib.lib_map_editor_battle_map.Window(2,'')
        a.Run()
        
    def bmap_editor_last(self):
        self.music(0)
        a = lib.lib_map_editor_battle_map.Window(3,'temp')
        a.Run()        

                
       # return pygame.mixer.music.stop()
    def _start(self):
        self.menu = Menu((250,110))
        # Именно таким образом мы можем получить текст в pygame
        # В данном случае мы используем системный шрифт.
        font      = pygame.font.SysFont("Verdana", 50, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Verdana", 50, bold=True, italic=False)
        self.menu.background()
        # Загрузка музыки.
        #pygame.mixer.music.load('data/music/menu.ogg')
        # Проигрывание музыки.
        #pygame.mixer.music.play()
        if self.music_counter == 0:
            self.music(1)
            self.music_counter = 1
        item = u"Новая игра"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.game_window)
        item = u"Загрузить игру"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.item_call)
        item = u"Редактор карт"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.map_editor_cubmenu)
        item = u"Настройки"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.item_call)
        item = u"Создатели"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.autor_print)
        item = u"Выход"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.fun_exit)

    def map_editor_cubmenu(self):
        self.menu = Menu((250,110))
        # Именно таким образом мы можем получить текст в pygame
        # В данном случае мы используем системный шрифт.
        font      = pygame.font.SysFont("Verdana", 50, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Verdana", 50, bold=True, italic=False)
        self.menu.background()
        # Загрузка музыки.
        #pygame.mixer.music.load('data/music/menu.ogg')
        # Проигрывание музыки.
        #pygame.mixer.music.play()
        #self.music(1)
        item = u"Карта 50х50"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.map_editor_0)
        item = u"Карта 100х100"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.map_editor_1)
        item = u"Карта 150х150"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.map_editor_2)
        item = u"Последняя несохраненная карта"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.map_editor_last)
        
        item = u"Карта боя"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.battlemap_editor_cubmenu)
        item = u"Назад"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self._start)

    def battlemap_editor_cubmenu(self):
        self.menu = Menu((250,110))
        # Именно таким образом мы можем получить текст в pygame
        # В данном случае мы используем системный шрифт.
        font      = pygame.font.SysFont("Verdana", 50, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Verdana", 50, bold=True, italic=False)
        self.menu.background()
        # Загрузка музыки.
        #pygame.mixer.music.load('data/music/menu.ogg')
        # Проигрывание музыки.
        #pygame.mixer.music.play()
        #self.music(1)
        item = u"Трава"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.bmap_editor_0)
        item = u"Песок"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.bmap_editor_1)
        item = u"Грунт"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.bmap_editor_2)
        item = u"Последняя несохраненная карта"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self.bmap_editor_last)

        item = u"Назад"
        self.menu.add_menu_item(font.render(item,True,(255,255,255)),
                                font_bold.render(item,True,(255,255,255)),
                                self._start)

    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.menu.down()
                    self.menu.background()
                    self.clix()
                elif e.key == pygame.K_UP:
                    self.menu.up()
                    self.menu.background()
                    self.clix()
                elif e.key == pygame.K_RETURN:
                    self.menu.call()

    def _draw(self, dt):
        #self.display.fill((255,255,255))
        self.menu.draw(self.display)


if __name__ == '__main__':
    # Вот так хитро все и закрутилось.
    # ждем, показываем, ждем, скрываем, ждем, меню.
    scene = WaitScene(1000, ShowScene(WaitScene(500, HideScene(WaitScene(1000,MenuScene())))))
    game = lib.Game(1280, 720, scene = scene)
    game.set_caption("War for Cookies", "icon.png")

    game.game_loop()

