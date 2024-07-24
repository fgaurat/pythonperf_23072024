#!/usr/bin/env python

from Rectangle import Rectangle

def main():
    r = Rectangle(3,2)
    # print(r._Rectangle__longueur,r._Rectangle__largeur)
    # r._Rectangle__longueur = -12
    # print(r._Rectangle__longueur,r._Rectangle__largeur)

    print(r.get_longueur()) # 3
    print(r.get_largeur()) # 2

    r.set_longueur(12)
    print(r.get_longueur()) # 12

    r.set_largeur(24)
    print(r.get_largeur()) # 24


if __name__ == '__main__':
    main()