# -*- coding: utf-8 -*-
import os

class unit():
    def __init__(self):
        pass
        
    def set_un(self,name):# тут индусятина ибо я говнокодер
         if os.path.exists(name):
            f=open(name)
            v=[]
            i=0
            for line in f.xreadlines():
                v.append(line)
            self.id_unit=v[0]
            self.name=v[1]
            self.hit_point=v[2]
            self.cost_milk=v[4]
            self.kick=v[5]
            self.rang=v[6]
            
    def get_print(self):
             print(self.name)
                
if __name__ == '__main__':
       Unit_inf=unit()
       Unit_inf.set_un('data/units/infantry.txt')
     #  Unit_inf.get_print()
       Unit_art=unit()
       Unit_art.set_un('data/units/artillery.txt')
      # Unit_art.get_print()
       Unit_tank=unit()
       Unit_tank.set_un('data/units/tank.txt')
      # Unit_tank.get_print()
       Unit_marines=unit()
       Unit_marines.set_un('data/units/marines.txt')
       #Unit_marines.get_print()
       Unit_mobinf=unit()
       Unit_mobinf.set_un('data/units/mobinf.txt')
       #Unit_mobinf.get_print()
       
       
       
