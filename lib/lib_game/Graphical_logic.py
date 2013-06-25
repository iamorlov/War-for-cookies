# -*- coding: utf-8 -*-
'''
Created on 16 черв. 2013

@author: antimoskal
'''
from pygame import *
from Core import Core


class Graphical_logic:
    
    def __init__(self):
        self.core = Core()
    
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
                
    def get_current_steps(self,id_army,filename): #повертаємо кількість кроків на даний момент в цій армії

        info_army = self.core.load_army(filename, id_army)
        info_ar = self.core.load_armies(filename)

        return info_army[7]
        
    def change_current_steps(self,id_army,filename,current_steps,steps):
        info_army = self.core.load_army(filename, id_army)
        res_steps = current_steps+steps
        if (res_steps<=0):
            res_steps =0
        self.core.change_army(filename, id_army, info_army[1], info_army[2], info_army[3], info_army[4], info_army[5], info_army[6], res_steps, info_army[8])

    def get_max_steps(self,id_army,filename):
        info_army = self.core.load_army(filename, id_army)
        return info_army[6]        
        
    def get_all_id_armies_for_current_fraction(self,fraction,filename):
        list_armies = self.core.load_armies(filename)
        list_id = []
        for i in range(len(list_armies)):
            if (list_armies[i][8]==fraction):
                list_id.append(list_armies[i][0])
        return list_id

    def change_all_armies_steps_for_fraction(self,fraction,filename):
        list_id = self.get_all_id_armies_for_current_fraction(fraction, filename)
        for i in range(len(list_id)):
            max_step = self.get_max_steps(list_id[i], filename)
            current_steps = self.get_current_steps(list_id[i], filename)
            steps = abs(max_step-current_steps)
            self.change_current_steps(list_id[i], filename, current_steps, steps)
#Fraction: id_fraction,base(0 - false, 1 - true),milk, cookies,farms,mines
    def add_resources_for_current_fraction(self,fraction,filename):
        fract = self.core.get_fraction_status(filename, fraction)
        print fract
        print 'FRACT'
        self.core.change_fraction_status(filename, fraction, fract[1], fract[2]+fract[4]*20, fract[3]+fract[5]*50, fract[4], fract[5])
        fract = self.core.get_fraction_status(filename, fraction)
        print fract                
        return fract

    def troops_generator(self,fraction,filename):
        fract = self.core.get_fraction_status(filename, fraction)
        costs = [[1,10],[2,25],[4,40],[9,80],[10,140]]
        current_resources  = [fract[2],fract[3]]
        used_resources  = [0,0]
        army = []
        for i in range(5):
            used_resources = [int(current_resources[0]*0.4),int(current_resources[1]*0.4)]
            temp_units1 = used_resources[0]//costs[i][0]
            temp_units2 = used_resources[1]//costs[i][1]
            if temp_units1 >=temp_units2:
                used_resources[0]=costs[i][0]*temp_units1
                used_resources[1]=costs[i][1]*temp_units1
                army.append(temp_units1)
            else:
                used_resources[0]=costs[i][0]*temp_units2
                used_resources[1]=costs[i][1]*temp_units2
                army.append(temp_units2)
            current_resources[0] = current_resources[0]-used_resources[0]
            current_resources[1] = current_resources[1]-used_resources[1]
        base = self.core.load_base(fraction, filename)
        bottom_coord = self.core.load_cell(base[0]+1, base[1]+1, filename)
        id_army = self.core.create_new_army(filename, army[0], army[1], army[2], army[3], army[4], 20, 20, fraction)
        self.core.change_cell(bottom_coord[0], bottom_coord[1], bottom_coord[2], fraction, id_army, filename)
        
        