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
            map_file = open ('temp_battle', 'w')
            count_u_1 = 1
            count_y = 1
            count_u_2 = 6
            for i in range(11):
                for j in range(20):
                    if ((j == 0) and (i == count_y)):
                        map_file.writelines('('+str(j)+';'+str(i)+';0;'+str(count_u_1)+')\n')
                        count_u_1 +=1
                    elif (j == 19) and (i == count_y):
                        map_file.writelines('('+str(j)+';'+str(i)+';0;'+str(count_u_2)+')\n')
                        count_u_2 +=1
                        count_y +=2
                    else:
                        map_file.writelines('('+str(j)+';'+str(i)+';0;0)\n')
            map_file.close()
            self.file = 'temp_battle'
        elif self.map_type == 1:
            map_file = open ('temp_battle', 'w')
            count_u_1 = 1
            count_y = 1
            count_u_2 = 6
            for i in range(11):
                for j in range(20):
                    if ((j == 0) and (i == count_y)):
                        map_file.writelines('('+str(j)+';'+str(i)+';1;'+str(count_u_1)+')\n')
                        count_u_1 +=1
                    elif (j == 19) and (i == count_y):
                        map_file.writelines('('+str(j)+';'+str(i)+';1;'+str(count_u_2)+')\n')
                        count_u_2 +=1
                        count_y +=2
                    else:
                        map_file.writelines('('+str(j)+';'+str(i)+';1;0)\n')
            map_file.close()
            self.file = 'temp_battle'
        elif self.map_type == 2:
            map_file = open ('temp_battle', 'w')
            count_u_1 = 1
            count_y = 1
            count_u_2 = 6
            for i in range(11):
                for j in range(20):
                    if ((j == 0) and (i == count_y)):
                        map_file.writelines('('+str(j)+';'+str(i)+';3;'+str(count_u_1)+')\n')
                        count_u_1 +=1
                    elif (j == 19) and (i == count_y):
                        map_file.writelines('('+str(j)+';'+str(i)+';3;'+str(count_u_2)+')\n')
                        count_u_2 +=1
                        count_y +=2
                    else:
                        map_file.writelines('('+str(j)+';'+str(i)+';3;0)\n')
            map_file.close()
            self.file = 'temp_battle'
        
    def save_file(self,name):
        map_file =open('temp_battle','r')
        final_file = open(name,'w')
        temp = map_file.readlines()
        final_file.writelines(temp)
        final_file.close()
        map_file.close()
        self.file = name
    
    def load_file(self,name):
        self.file = name
        map_file = open(name,'r')
        buff = map_file.readlines()
        map_file.close()
        
        self.file = 'temp_battle'
        map_file = open(self.file,'w')
        map_file.writelines(buff)
        map_file.close()
            
    def change_cell(self,x,y,t,id):
        map_file = open(self.file,'r')
        lines = map_file.readlines()
        map_file.close()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        print str(x)+'[;]'+str(y)
        a = re.search('[(]'+str(x)+'[;]'+str(y)+'[;][0-7][;][0-1]{0,1}[0-9][)]',l)
        if a!=None:
            base_line = a.group(0)
        new_line = '('+str(x)+';'+str(y)+';'+str(t)+';'+str(id)+')' 
        file = open(self.file,'w')
        file.writelines(l.replace(base_line,new_line))
        file.close()
    
    def get_cell_information(self,line):
        #Ололо я індус
        result = []
        l = line.split(';')
        l[0] = l[0][1:]
        l[3] = l[3][:1]
        for i in range(len(l)):
            result.append(int(l[i]))
        return result
       # '[(][0-9]{1,2}[;][0-9]{1,2}[;][0-6][;][0-1]{0,1}[0-9][)]'
         


    #СВЯТА ДЖИГУРДА! Мені соромно за ті верхні два шматки коду :((((((( 
    
    def load_cells(self,x,y):
        map_file = open(self.file,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.seek(0)
        map_file.close()

        list_coords = []
   #     print str(self.x_coord_start)+' '+ str(self.x_coord_end)+ ' ' + str(self.y_coord_start)+ ' ' + str(self.y_coord_end)
        for j in range(11):
            for k in range(20):
                a = re.search('[(]'+str(k)+'[;]'+str(j)+'[;][0-7][;][0-9]+[)]',l)
                if a!= None:
                    list_coords.append(self.get_cell_information(a.group(0)))
        return list_coords

    def load_cells_for_transparent_textures(self,x,y):
        map_file = open(self.file,'r')
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
           
    def load_minimap_cells(self):
        map_file = open(self.file,'r')
        lines = map_file.readlines()
        l = ''
        for i in range(len(lines)):
            l+=lines[i]
        map_file.close()
        list_coords = []
        a = re.findall('[(][0-9]{1,2}[;][0-9]{1,2}[;][0-7][;][0-1]{0,1}[0-9][)]',l)
        for i in range(11*20):
            list_coords.append(self.get_cell_information(a[i]))
        return list_coords
         
#[(][0-9]{1,3}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,4}[;][0-9]{1,2}[)]