# -*- coding: utf-8 -*-
from Window import *

if __name__ == '__main__':
    a = Window()
    a.Main_Window()
    a.Maps_grid()
    a.Type_of_grids()
    a.Mouse_events()
    for i in range(3000):
        a.Mouse_events()
        time.sleep(0.05)