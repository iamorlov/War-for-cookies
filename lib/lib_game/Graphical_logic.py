# -*- coding: utf-8 -*-
'''
Created on 16 черв. 2013

@author: antimoskal
'''
from pygame import *

class Graphical_logic:
    
    def __init__(self):
        pass
    
    def get_type_background_textures(self,x,y,local_list):
        mass_cell_type = []
        for k in range(len(local_list)):
            type_cell = local_list[k][2]
            if (type_cell !=3) and (type_cell <6):
                mass_cell_type.append(type_cell)
        types = [0,0,0,0,0,0]
        for k in range(0,len(mass_cell_type)):
            if mass_cell_type[k] == 0:
                types[0]+=1;
            elif mass_cell_type[k] == 1:
                types[1]+=1;
            elif mass_cell_type[k] == 2:
                types[2]+=1;
            elif mass_cell_type[k] == 4:
                types[3]+=1;
            elif mass_cell_type[k] == 5:
                types[4]+=1;
            elif mass_cell_type[k] == 6:
                types[5]+=1;
        max_cells = max(types)
        for k in range(0,len(types)):
            if (max_cells == types[k]):
                if k <3:
                    return k
                else:
                    return  k+1