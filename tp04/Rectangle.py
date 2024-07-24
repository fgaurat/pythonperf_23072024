class Rectangle:
    
    def __init__(self,longueur,largeur):
        print(f"def __init__(self,{longueur},{largeur})")
        assert longueur>0 and largeur>0  
        # if longueur<=0 or largeur<=0:
        #     raise Exception('mauvaises valeurs pour longueur ou largeur')
        
        self.__longueur = longueur # _Rectangle__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,l):
        self.__longueur = l

    def set_largeur(self,l):
        self.__largeur = l