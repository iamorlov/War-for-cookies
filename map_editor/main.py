# -*- coding: utf-8 -*-
from Window import *

if __name__ == '__main__':
    a = Window()
    a.Main_Window()
    a.Entry_type()
    a.Maps_grid()
    a.Type_of_grids()
    a.Rewrite_cell()
    while True:
        a.Rewrite_cell()
        time.sleep(0.000001)