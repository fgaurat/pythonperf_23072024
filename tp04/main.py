#!/usr/bin/env python

import sys
# sys.path.append('')

from Rectangle import Rectangle
from DataRectangle import DataRectangle


# current directory
# PYTHONPATH
# python install directory
# sys.path.append
# venv


def main():
    r = Rectangle(3,2)
    # r._Rectangle__longueur = -12
    # r.longueur = -12
    a = r.longueur # get
    r.longueur =12 # set
    # print(r.longueur)
    # print(r.largeur)
    print(r.longueur)

    d = DataRectangle(2,3)
    print(d.longueur,d.largeur,d.get_surface())
    
    s = str(d)
    print(s)
    s = str(r)
    print(s)

    r.longueur =12
    print(r.__dict__)
    print(50*'-')    
    r = Rectangle(3,2)
    r1 = Rectangle(3,2)

    if r==r1: # r.__equal(r1)
        print("ok")
    else:
        print("ko")

    print(Rectangle.get_cpt())
    print(r.get_cpt())
    print(r1.get_cpt())
    print(50*'-')

    r = Rectangle()
    r1 = Rectangle(3,7)
    line = "3;7"
    
    a,b =[int(i) for i in line.split(";")] 
    r3 = Rectangle.buildFromStr(a,b)


    r2 = Rectangle.buildFromStr("3;7")
    print(r)
    print(r1)
    print(r2)
def main_01():
    r = Rectangle(3,2)
    # print(r._Rectangle__longueur,r._Rectangle__largeur)
    # r._Rectangle__longueur = -12
    # print(r._Rectangle__longueur,r._Rectangle__largeur)

    print(r.get_longueur()) # 3
    print(r.longueur)
    r.longueur = 4
    print(r.get_largeur()) # 2

    r.set_longueur(12)
    print(r.get_longueur()) # 12

    r.set_largeur(24)
    print(r.get_largeur()) # 24

    print(r.get_surface()) # 288
    
if __name__ == '__main__':
    main()