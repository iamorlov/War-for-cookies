# -*- coding: utf-8 -*-
import os
from core import get_datapath
class Unit():
    def __init__(self,name):
        if os.path.exists(name):
            f=open(name)
            self.data=[]
            self.bonus=[]
            self.explain = {'id' : 0, 'name' : 1,'xp':2,
                            'move':3,'cost_cookie':4,'cost_milk':5,
                            'attack':6,'range':7,'bonus':8,'description':9}
            for line in f.xreadlines():
                self.data.append(line)
            self.bonus.extend(self.data[8].split(' '))
        
    
    def get_print(self,n,m):#n-что надо, m-если надо бонусы, его номер
        if(n==8):
            return(self.bonus[self.explain[m]])
        else:
            return(self.data[self.explain[n]])
        # перенесено в core как востребованная ф-ция
    #def get_datapath(self):
     #   path=os.getcwd().split(os.sep)
     #   path.pop()
      #  path.append('data')
      #  print os.sep.join(path)
       # print path
if __name__ == '__main__':
    dir_path=get_datapath()
    infantry=Unit(dir_path+'units\infantry.txt')
    marines=Unit(dir_path+'units\marines.txt')
    mob_infantry=Unit(dir_path+'units\mobinf.txt')
    tank=Unit(dir_path+'units\tank.txt')
    artillery=Unit(dir_path+'units\artillery.txt')