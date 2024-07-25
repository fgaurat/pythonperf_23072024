from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(2)
    print(c.get_surface())
    print(c)
    c.cote = 12
    print(c)
    print(c.get_surface())
    ce = Cercle(3)
    print(c.get_surface())
    
    print(ce.get_surface())


if __name__ == '__main__':
    main()