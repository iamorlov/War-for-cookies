#-*- coding: utf-8 -*-
import os, math, unit_w, unit_w
from lib_game import Core
class Base_core():
    def __init__(self, filename,nom,mapsize):
        self.core=Core()
        self.cells_list=self.core.load_battle_cells(filename)
        self.headquarter = [0,1,'Штаб','way_to_image',0]
        self.hire_infantry = [1,1,'Казарма пехоты','way_to_image',0]
        self.hire_marines = [2,0,'Казарма ракетчиков','way_to_image',50]
        self.hire_mob_inf = [3,0,'Автомобильный парк','way_to_image',100]
        self.hire_tank = [4,0,'Парк бронетехники','way_to_image',150]
        self.hire_artillery = [5,0,'Орудийный завод','way_to_image',200]
        self.find_base(nom)
        self.buildings=[self.headquarter,self.hire_infantry,self.hire_marines,self.hire_mob_inf,self.hire_tank,self.hire_artillery]
        self.base_army=load_army(filename,self.base_army_id)
        
    def find_base(self,nom):
        temp=get_cell_information(cells_list[nom])
        self.base_fract=temp[3]
        self.base_army_id=temp[4]                
        
    def build_building(self,milk,type):
        if (self.buildings[type][1]==1):
            return 'Здание уже построено!',milk
        elif(self.buildings[type][4]>milk):
            return 'Недостаточно молока рабочим!',milk
        else:
            self.buildings[type][1]=1
            return 'Здание построено!',milk-self.buildings[type][4]
        
    def sell_building(self,type):
        if (self.buildings[type][1]==0):
            return 'Здание не найдено!',0
        else:
            self.buildings[type][1]=1
            return 'Здание снесено!',self.buildings[type][4]/2
        
    def use_building(self,type,count,cookies,milk):
        if(type==0):
            
        else:
            if()
            self.base_army[type]
    