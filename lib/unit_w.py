#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, pygame, os

class unit():
        id_unit=''
        name=''
        hit_point
        cost_co
        cost_milk
        kick
        rang
        i=0
     def set_un(name):# тут индусятина ибо я говнокодер
         if os.path.exists(name):
            f=open(name)
            v=['','','','','','','']
            for line in f.xreadlines()
                i+=1
                v[i]=line
            id_unit=v[1]
            name=v[2]
            hit_point=v[3]
            cost_milk[5]
            kick=v[6]
            rang=v[7]
     def get_print(self)
             print(name)
                
if __name__ == '__main__':
       Unir=unit()
       Unir.set_un('data/units/artillery.txt')
       Unir.get_print()
