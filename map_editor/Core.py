# -*- coding: utf-8 -*-
import os
import re
import time

class Core():

    def __init__(self):
        pass

    def empty_map(self,map_type):
        self.map_type = map_type
        if self.map_type == 0:
            x = 50
            y = 50
        elif self.map_type == 1:
            x = 100
            y = 100
        elif self.map_type == 2:
            x = 150
            y = 150
        ##
        map_file = open ('temp', 'w')
        map_file.writelines(str(x)+'\n'+str(y)+'\n2\n')
        for i in range(y):
            for j in range(x):
                map_file.writelines('('+str(j)+';'+str(i)+';3;0;0)\n')
        map_file.close()
        self.file = 'temp'
        
    def save_file(self,name):
        map_file =open('temp','r')
        final_file = open(name,'w')
        temp = map_file.readlines()
        final_file.writelines(temp)
        final_file.close()
        map_file.close()
        self.file = name
        os.remove('temp')
    
    def load_file(self,name):
        self.file = name
        map_file = open(name,'r')
        x_coords = map_file.readline()
        y_coords = map_file.readline()
        map_file.close()
        if x_coords[:-1] == y_coords[:-1] == '50':
            self.map_type = 0
        elif x_coords[:-1] == y_coords[:-1] == '100':
            self.map_type = 1
        elif x_coords[:-1] == y_coords[:-1] == '150':
            self.map_type = 2
            
    def change_cell(self,x,y,t,f,id_army):
        map_file = open(self.file,'r')
        lines = map_file.readlines()
        map_file.close()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        a = re.search('[(]'+str(x)+'[;]'+str(y)+'[;][0-9]{1,2}[;][0-2][;][0-9]+[)]',l)
        if a!=None:
            base_line = a.group(0)
        new_line = '('+str(x)+';'+str(y)+';'+str(t)+';'+str(f)+';'+str(id_army)+')' 
        file = open(self.file,'w')
        file.writelines(l.replace(base_line,new_line))
        file.close()
    
    def get_cell_information(self,line):
        #Ололо я індус
        result = []
        x = re.search('[(][0-9]{1,3}[;]', line)
        x = x.group(0)
        len_x = len(x)
        x = x[1:]
        x = x[:-1]
        
        result.append(int(x))
        y = re.search('[(][0-9]{1,3}[;][0-9]{1,3}[;]', line)
        y = y.group(0)
        len_y = len(y)
        y = y[len_x:]
        y = y[:-1]

        result.append(int(y))
        t = re.search('[(][0-9]{1,3}[;][0-9]{1,3}[;][0-9]{1,2}[;]', line)
        t = t.group(0)
        len_t = len(t)
        t = t[len_y:]
        t = t[:-1]

        result.append(int(t))
        f = re.search('[(][0-9]{1,3}[;][0-9]{1,3}[;][0-9]{1,2}[;][0-2][;]', line)
        f = f.group(0)
        temp_len = len(f)
        f = f[len_t:]
        f = f[:-1]

        result.append(int(f))
        id_army = re.search('[(][0-9]{1,3}[;][0-9]{1,3}[;][0-9]{1,2}[;][0-2][;][0-9]+', line)
        id_army = id_army.group(0)
        id_army = id_army[temp_len:]
        result.append(int(id_army))
        return result               
    
    def load_cells(self,x,y):
        map_file = open(self.file,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.seek(0)
        max1 = map_file.readline()
        max2 = map_file.readline()
        map_file.close()
        a = int(max1) - x
        b = int(max2) - y
        if (x < 25):
            self.x_coord_start = 0
            self.x_coord_end = 25
        elif(a<25):
            self.x_coord_start = int(max1)-25
            self.x_coord_end = int(max1)
        else:
            self.x_coord_start = x-13
            self.x_coord_end = x+12
        if (y < 25):
            self.y_coord_start = 0
            self.y_coord_end = 25
        elif(b<25):
            self.y_coord_start = int(max2)-25
            self.y_coord_end = int(max2)
        else:
            self.y_coord_start = y-13
            self.y_coord_end = y+12
        list_coords = []
        for j in range(self.x_coord_start,self.x_coord_end):
            for k in range(self.y_coord_start,self.y_coord_end):
                a = re.search('[(]'+str(k)+'[;]'+str(j)+'[;][0-9]{1,2}[;][0-2][;][0-9]+[)]',l)
                if a!= None:
                    list_coords.append(self.get_cell_information(a.group(0)))
        return list_coords
        
    def load_minimap_cells(self):
        map_file = open(self.file,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.seek(0)
        max1 = map_file.readline()
        max2 = map_file.readline()
        map_file.close()
        list_coords = []
        a = re.findall('[(][0-9]{1,3}[;][0-9]{1,3}[;][0-9]{1,2}[;][0-2][;][0-9]+[)]',l)
        for i in range(int(max1)*int(max2)):
           list_coords.append(self.get_cell_information(a[i]))
        return list_coords
            
