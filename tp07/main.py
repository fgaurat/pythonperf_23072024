from typing import Any
from Rectangle import Rectangle
from RectangleSingleton import RectangleSingleton
from RectangleMetaSingleton import RectangleMetaSingleton
from RectangleSingletonDeco import RectangleSingletonDeco

class TheClass:

    def __new__(cls):
        print("def __new__(cls)")
        self = super().__new__(cls)
        return self

    def __init__(self) -> None: # constructeur : init
        print("def __init__(self)")
        
    def __call__(self):
        print("def __call__(self)")


def main():
    t = TheClass()
    print(TheClass.mro())
    t()
    print(type(t))
    print(type(TheClass))

    print(50*"-")


    r1 = Rectangle(1,2)
    r2 = Rectangle(1,2)
    print(hex(id(r1)))
    print(hex(id(r2)))
    print(50*"-")

    r1 = RectangleSingleton(1,2)
    r2 = RectangleSingleton(1,2)
    print(hex(id(r1)))
    print(hex(id(r2)))
    r1.longueur = 12
    print(r2)
    print(50*"-")
    r1 = RectangleMetaSingleton(1,2)
    r2 = RectangleMetaSingleton(1,2)
    print(hex(id(r1)))
    print(hex(id(r2)))
    print(50*"-")
    r1 = RectangleSingletonDeco(1,2)
    r2 = RectangleSingletonDeco(1,2)
    print(hex(id(r1)))
    print(hex(id(r2)))




if __name__ == '__main__':
    main()