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
       Unir=unit()
       Unir.set_un('infantry.txt')
       Unir.get_print()
