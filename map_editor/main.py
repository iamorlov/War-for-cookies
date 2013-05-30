# -*- coding: utf-8 -*-
from Window import *

if __name__ == '__main__':
    a = Window()
    a.Main_Window()
    a.Entry_type()
    a.load_cells_list()
    a.Maps_grid()
    a.Minimaps_grid()
    a.Minimap()
    a.Load_part_of_map()
    a.Type_of_grids()
    a.Rewrite_cell()
    while True:
        a.Rewrite_cell()
        time.sleep(0.000001)