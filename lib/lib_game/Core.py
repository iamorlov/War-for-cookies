# -*- coding: utf-8 -*-
import os
import re
import time

class Core():

    def __init__(self):
        self.map_scale=14#магическое число епта

    def save_file(self,file_name_for_save,current_name):
        map_file =open(current_name,'r')
        final_file = open(file_name_for_save,'w')
        temp = map_file.readlines()
        final_file.writelines(temp)
        final_file.close()
        map_file.close()
    
    def load_file(self,file_name_for_loading,current_name):
        map_file = open(file_name_for_loading,'r')
        x_coords = map_file.readline()
        y_coords = map_file.readline()
        map_file.seek(0)
        buff = map_file.readlines()
        map_file.close()
        if x_coords[:-1] == y_coords[:-1] == '50':
            map_type = 0
        elif x_coords[:-1] == y_coords[:-1] == '100':
            map_type = 1
        elif x_coords[:-1] == y_coords[:-1] == '150':
            map_type = 2
        map_file = open(current_name,'w')
        map_file.writelines(buff)
        map_file.close()
        return map_type
            
    def change_cell(self,x,y,t,f,id_army,current_name):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        map_file.close()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        a = re.search('[(]'+str(x)+'[;]'+str(y)+'[;][0-9]{1,2}[;][0-2][;][0-9]+[)]',l)
        if a!=None:
            base_line = a.group(0)
        new_line = '('+str(x)+';'+str(y)+';'+str(t)+';'+str(f)+';'+str(id_army)+')' 
        file = open(current_name,'w')
        file.writelines(l.replace(base_line,new_line))
        file.close()
    
    def get_cell_information(self,line):
        line=line[1:]
        line=line[:-1]
        result=line.split(';')
        for i in range(len(result)):
            result[i]=int(result[i])
        return result

    def get_army_information(self,line):
        result = []
        l = line.split(';')
        l[0] = l[0][1:]
        l[8] = l[8][:1]
        for i in range(len(l)):
            result.append(int(l[i]))
        return result
    
    def load_cells(self,x,y,current_name):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.seek(0)
        max1 = int(map_file.readline())
        max2 = int(map_file.readline())
        map_file.close()
        a = max1 - x
        b = max2 - y
        if (x < 14):
            x_coord_start = 0
            x_coord_end = self.map_scale
        elif(a<14):
            x_coord_start = max1-self.map_scale
            x_coord_end = max1
        else:
            x_coord_start = x-self.map_scale//2
            x_coord_end = x+self.map_scale//2
        if (y < 14):
            y_coord_start = 0
            y_coord_end = self.map_scale
        elif(b<14):
            y_coord_start = int(max2)-self.map_scale
            y_coord_end = int(max2)
        else:
            y_coord_start = y-self.map_scale//2
            y_coord_end = y+self.map_scale//2
        list_coords = []
        for j in range(x_coord_start,x_coord_end):
            for k in range(y_coord_start,y_coord_end):
                a = re.search('[(]'+str(k)+'[;]'+str(j)+'[;][0-9]{1,2}[;][0-2][;][0-9]+[)]',l)
                if a!= None:
                    list_coords.append(self.get_cell_information(a.group(0)))
        print str(list_coords)+'\n'+str(x_coord_start)+'\n'+str(y_coord_start)
        return list_coords,x_coord_start,y_coord_start
    
    def load_battle_cells(self,current_name):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.seek(0)
        max1 = int(map_file.readline())
        max2 = int(map_file.readline())
        map_file.close()
        list_coords = []
        a = re.findall('[(][0-9]{1,2}[;][0-9]{1,2}[;][0-6][;][0-1]{0,1}[0-9][)]',l)
        for i in range(max1*max2):
            list_coords.append(self.get_cell_information(a[i]))
        return list_coords

    def load_cell(self,x,y,current_name):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]        
        map_file.close()
        cell = re.search('[(]'+str(x)+'[;]'+str(y)+'[;][0-9]{1,2}[;][0-2][;][0-9]+[)]',l)
        if cell!= None:#x,y,type,fraction,id_army
            return self.get_cell_information(cell.group(0))
        
    def load_cells_for_transparent_textures(self,x,y,current_name):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.seek(0)
        max1 = int(map_file.readline())
        max2 = int(map_file.readline())
        map_file.close()
        result = []
        
        for i in range(0,3):
            for j in range(3):
                #if (((x-1+i)>=0) or ((y-1+j)>=0) or ((x-1+i)<=max1) or ((y-1+j)<=max2)):
                if (((x-1+i)>=0) and ((y-1+j)>=0)) and (((x-1+i)<=max1) and ((y-1+j)<=max2)):
                    a = re.search('[(]'+str(x-1+i)+'[;]'+str(y-1+j)+'[;][0-9]{1,2}[;][0-2][;][0-9]+[)]',l)
                    result.append(self.get_cell_information(a.group(0)))
        return result
           
    def load_minimap_cells(self,current_name):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.seek(0)
        max1 = int(map_file.readline())
        max2 = int(map_file.readline())
        map_file.close()
        list_coords = []
        a = re.findall('[(][0-9]{1,3}[;][0-9]{1,3}[;][0-9]{1,2}[;][0-2][;][0-9]+[)]',l)
        for i in range(max1*max2):
           list_coords.append(self.get_cell_information(a[i]))
        return list_coords

    def load_armies(self,current_name):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.close()
        list_army = []
        a = re.findall('[(][0-9]{1,3}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,2}[;][0-9]{1,2}[;][0-9][)]',l)
        for i in range(len(a)):
            army = self.get_army_information(a[i])
            list_army.append(self.get_army_information(a[i]))
#            a_dict = dict([('id_army',army[0]),('infantry',army[1]),('marines',army[2]),('mob_inf',army[3]),('tank',army[4]),('arta',army[5]),('move',army[6]),('move_last',army[7]),('fraction', army[8])])
        return list_army
    
    def load_army(self,current_name,id_army):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]        
        map_file.close()
        a = re.search('[(]'+str(id_army)+'[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,2}[;][0-9]{1,2}[;][0-9][)]',l)
        print a.group(0)
        if a!= None:
            return self.get_army_information(a.group(0))        

    def change_army(self,current_name,id_army,unit_1,unit_2,unit_3,unit_4,unit_5,move_max,move_current,fraction):
        map_file = open(current_name,'r')
        lines = map_file.readlines()
        map_file.close()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        a = re.search('[(]'+str(id_army)+'[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,2}[;][0-9]{1,2}[;][0-9][)]',l)
        if a!=None:
            base_line = a.group(0)
        new_line = '('+str(id_army)+';'+str(unit_1)+';'+str(unit_2)+';'+str(unit_3)+';'+str(unit_4)+';'+str(unit_5)+';'+str(move_max)+';'+str(move_current)+';'+str(fraction)+')' 
        file = open(current_name,'w')
        file.writelines(l.replace(base_line,new_line))
        file.close()               
#[(][0-9]{1,3}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,2}[)]