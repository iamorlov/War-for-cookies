#-*- coding: utf-8 -*-
import os
class Unit():
    def __init__(self,name):
        if os.path.exists(name):
            f=open(name)
            self.data=[]
            self.bonus=[]
            self.explain = {'id' : 0, 'name' : 1,'xp':2,
                        'move':3,'cost_cookie':4,'cost_milk':5,
                        'kick':6,'range':7,'bonus':8,'description':9}
            for line in f.xreadlines():
                self.data.append(line)
            self.bonus.extend(self.data[8].split(' '))
            for i in range(5):
                self.bonus[i]=float(self.bonus[i])
            for i in range(2,8):
                self.data[i]=int(self.data[i])
        else:
             print name
    def get_abil(self,n,m):
        if(self.explain.get(n)==8):
            return(self.bonus[m])
        else:
            return(self.data[self.explain[n]])
    def set_abil(self,n, data):
        self.data[self.explain[n]] = data
    #def set_units(self):
        #infantry=Unit('data\units\infantry.txt')
       # marines=Unit('data\units\marines.txt')
        #mob_infantry=Unit('data\units\mobinf.txt')
        #tank=Unit('data\units\tank.txt')
        #artillery=Unit('data\units\artillery.txt')
       # return [infantry,marines,mob_infantry,tank,artillery]
    
