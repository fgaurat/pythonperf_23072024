#!/usr/bin/env python

import sys
# sys.path.append('')

from Rectangle import Rectangle
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