#-*- coding: utf-8 -*-
import os, math, unit_w,copy
from lib_game import Core
from random import randint
class Battle():
    def __init__(self, filename):
        infantry=unit_w.Unit('data\\units\\infantry.txt')
        marines=unit_w.Unit('data\\units\\marines.txt')
        mob_infantry=unit_w.Unit('data\\units\\mobinf.txt')
        tank=unit_w.Unit('data\\units\\tank.txt')
        artillery=unit_w.Unit('data\\units\\artillery.txt')
        filename=('data\\battle_maps\\'+str(filename))
        self.core=Core()
        self.units_list=[infantry,marines,mob_infantry,tank,artillery]
        self.hp_last1=[infantry.get_abil('xp',0),marines.get_abil('xp',0),mob_infantry.get_abil('xp',0),tank.get_abil('xp',0),artillery.get_abil('xp',0)]
        self.hp_last2=copy.copy(self.hp_last1)
        self.move_last1=[infantry.get_abil('move',0),marines.get_abil('move',0),mob_infantry.get_abil('move',0),tank.get_abil('move',0),artillery.get_abil('move',0)]
        self.move_last2=copy.copy(self.move_last1)
        self.cells_list=self.core.load_battle_cells(filename)
        self.coord_army1=self.get_army_coords(0)
        self.coord_army2=self.get_army_coords(1)
        #остаток здоровья и остаток хода
    def find_strength(self, army):
        strength=0
        for i in range(5):
            strength+=army[i+1]*(self.units_list[i].get_abil('xp',0)+self.units_list[i].get_abil('kick',0)+self.units_list[i].get_abil('move',0))
        return strength
        
    def chanse(self,army_str1, army_str2):
        chans=army_str1/float(army_str2)
        if (chans<0.2):
            str='Однозначное поражение'
        elif(chans<0.4):
            str='Тяжелое поражение'
        elif(chans<0.6):
            str='Поражение'
        elif(chans<0.8):
            str='Незначительное поражение'
        elif(chans<1):
            str='Паритет'
        elif(chans<1.2):
            str='Пиррова победа'
        elif(chans<1.4):
            str='Тяжелая победа'
        elif(chans<1.6):
            str='Победа'
        elif(chans<1.8):
            str='Блестящая победа'
        else:
            str='Легкая разминка'
        return str
        
    def kick(self,army1,army2,type1,type2,fraction):
        if (fraction==0):
            self.move_last1[type1-1]=0#no more moving
            damag=math.ceil((army1[type1]*randint(3,5)*self.units_list[type1-1].get_abil('kick',0)*self.units_list[type1-1].get_abil('bonus',type2))/4.0)#количество*тычка*бонус
            last_health=math.modf(((army2[type2+1]*self.units_list[type2].get_abil('xp',0))+self.hp_last2[type2]-damag)/self.units_list[type2].get_abil('xp',0))
            if(last_health[1]<0):#если убили
                self.hp_last2[type2]=0
                army2[type2+1]=0
            else:
                self.hp_last2[type2]=last_health[0]*self.units_list[type2].get_abil('xp',0)
                army2[type2+1]= last_health[1]
        if (fraction==1):
            self.move_last2[type1-1]=0#no more moving
            damag=math.ceil((army1[type1]*randint(3,5)*self.units_list[type1-1].get_abil('kick',0)*self.units_list[type1-1].get_abil('bonus',type2))/4.0)#количество*тычка*бонус
            last_health=math.modf(((army2[type2+1]*self.units_list[type2].get_abil('xp',0))+self.hp_last1[type2]-damag)/self.units_list[type2].get_abil('xp',0))
            if(last_health[1]<0):#если убили
                self.hp_last1[type2]=0
                army2[type2+1]=0
            else:
                self.hp_last1[type2]=last_health[0]*self.units_list[type2].get_abil('xp',0)
                army2[type2+1]= last_health[1]
        return army2
    
    def is_in_range(self,coord_army1,coord_army2,attacker,victim):
        distance_x=coord_army1[attacker][0]-coord_army2[victim][0]-self.units_list[attacker].get_abil('range',0)
        distance_y=coord_army1[attacker][1]-coord_army2[victim][1]-self.units_list[attacker].get_abil('range',0)
        in_range_by_x=distance_x<=0
        in_range_by_y=distance_y<=0
        if (in_range_by_x and in_range_by_y):
            return True
        return False
        
    def get_alive(self,army):
        alive_list=[]
        for i in range(1,6):
            if (army[i]>0):
                alive_list.append(i-1)
        return alive_list
    
    def get_vunerable(self,atacker,army2):
        victim=-1
        temp=-1
        alive_list=self.get_alive(army2)
        for i in range(len(alive_list)):
            if (victim<self.units_list[atacker].get_abil('bonus',alive_list[i])):
                temp=alive_list[i]
                victim=self.units_list[atacker].get_abil('bonus',alive_list[i])
        return temp
    
    def bot_moving(self,unit_number, dir_x, dir_y,fraction):
        if (fraction==0):
            temp=self.cells_list[self.coord_army1[unit_number][1]*20+self.coord_army1[unit_number][0]]
            self.cells_list[self.coord_army1[unit_number][1]*20+self.coord_army1[unit_number][0]][3]=0
            self.cells_list[(self.coord_army1[unit_number][1]+dir_y)*20+(self.coord_army1[unit_number][0]-dir_x)][3]=temp[3]
            self.coord_army1[unit_number][0]+=dir_x
            self.coord_army1[unit_number][1]+=dir_y
            return self.coord_army1
        elif (fraction==1):
            temp=self.cells_list[self.coord_army2[unit_number][1]*20+self.coord_army2[unit_number][0]]
            self.cells_list[self.coord_army2[unit_number][1]*20+self.coord_army2[unit_number][0]][3]=0
            self.cells_list[(self.coord_army2[unit_number][1]+dir_y)*20+(self.coord_army2[unit_number][0]-dir_x)][3]=temp[3]
            self.coord_army2[unit_number][0]+=dir_x
            self.coord_army2[unit_number][1]+=dir_y
            return self.coord_army2
    def get_army_coords(self,fraction):
        coord_army=[[0,0],[0,0],[0,0],[0,0],[0,0]]
        for i in range(len(self.cells_list)):
            if ((self.cells_list[i][3]>(0+fraction*5))and(self.cells_list[i][3]<(6+fraction*5))):
                coord_army[self.cells_list[i][3]-fraction*5-1][0]=int(self.cells_list[i][0])
                coord_army[self.cells_list[i][3]-fraction*5-1][1]=int(self.cells_list[i][1])
        return coord_army
                 
    def bot_1step(self, army1, army2,army1_coord, army2_coord, fraction,attacker):
        alive_list=self.get_alive(army2)
        false_army=[-1,0,0,0,0,0]
        no_in_range=0#если ни одного в пределах досягаемости за ход, это - просто чтобы топал
        victim=self.get_vunerable(attacker,army2)
        victim_chosen=False
        while(victim_chosen == False):
            distance_x=army1_coord[attacker][0]-army2_coord[victim][0]
            distance_y=army1_coord[attacker][1]-army2_coord[victim][1]
            if (abs(distance_x)+abs(distance_y)-(2*self.units_list[attacker].get_abil('range',0))<self.units_list[attacker].get_abil('move',0)):#если дотопает за ход
                victim_chosen=True
                break
            if(sum(false_army)==-1):
                false_army=copy.copy(army2)
            false_army[victim+1]=0
            if(sum(false_army)>false_army[0]):
                victim=self.get_vunerable(attacker,false_army)
                
            else:
                victim_chosen=True
                victim=self.get_vunerable(attacker,army2)
        for i in range(self.units_list[attacker].get_abil('move',0)):
            distance_x=army1_coord[attacker][0]-army2_coord[victim][0]#-self.units_list[attacker].get_abil('range',0)
            distance_y=army1_coord[attacker][1]-army2_coord[victim][1]#-self.units_list[attacker].get_abil('range',0)
            in_range_by_x=abs(distance_x)-self.units_list[attacker].get_abil('range',0)<=0
            in_range_by_y=abs(distance_y)-self.units_list[attacker].get_abil('range',0)<=0    
            if (in_range_by_x and in_range_by_y):#если кто-то уже в радиусе атаки
                army2=self.kick(army1,army2,attacker+1,victim,fraction)#то это его проблемы
                break
            list_plase=army1_coord[attacker][1]*20+army1_coord[attacker][0]
            if (abs(distance_x)>self.units_list[attacker].get_abil('range',0)):
                if (distance_x<0 and (self.cells_list[list_plase-11][3]==0)):
                    army1_coord=self.bot_moving(attacker, 1, 0,fraction)  #move left           
                elif( self.cells_list[list_plase-11][3]==0):
                    army1_coord=self.bot_moving(attacker, -1, 0,fraction)  #move right
            else:
                if (abs(distance_y)>self.units_list[attacker].get_abil('range',0)):
                    if (distance_y<0 and (self.cells_list[list_plase-1][3]==0)):
                        army1_coord=self.bot_moving(attacker, 0, -1,fraction)      #move up
                    elif((self.cells_list[list_plase+1][3]==0)):
                        army1_coord=self.bot_moving(attacker, 0, 1,fraction)      #move down
                        
    def who_wins(self,army1,army2):
        countwarrs1=0
        countwarrs2=0
        for i in range(5):
            countwarrs1+=army1[i+1]
            countwarrs2+=army2[i+1]#считаем кол-во войск
        if(countwarrs1>0 and countwarrs2>0):
            return 0
        elif(countwarrs2==0):
            return 1
        else:
            return 2   
    
    def auto_battle(self,army1,army2):
        #coord_army1 = [[1,0],[3,0],[5,0],[7,0],[9,0]]
        #coord_army2 = [[1,20],[3,20],[5,20],[7,20],[9,20]]
        alive_list=self.get_alive(army1)    
        while(self.who_wins(army1,army2)==0):
            for i in range(5):
                if (army1[i+1]>0):
                    self.bot_1step(army1, army2, self.coord_army1, self.coord_army2,0,i)
                    if(self.who_wins(army1,army2)>0):
                        break
                if (army2[i+1]>0):
                    self.bot_1step(army2, army1,self.coord_army2, self.coord_army1,1,i)
                    if(self.who_wins(army1,army2)>0):
                        break
        #print (self.who_wins(army1,army2))
        if(self.who_wins(army1,army2)==1):
            return army1,army2
        return army2,army1
#bat=Battle(1)
#bat.find_strength([0,10,0,0,0,0])
#bat.auto_battle([0,100,20,0,0,8],[1,50,20,0,0,4])