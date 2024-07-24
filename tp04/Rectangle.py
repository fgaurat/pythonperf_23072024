class Rectangle:
    
    def __init__(self,longueur,largeur):
        print(f"def __init__(self,{longueur},{largeur})")
        assert longueur>0 and largeur>0  
        # if longueur<=0 or largeur<=0:
        #     raise Exception('mauvaises valeurs pour longueur ou largeur')
        
        self.__longueur = longueur # _Rectangle__longueur = longueur
        self.__largeur = largeur

    @property # get
    def longueur(self):
        """
        return the longueur
        """
        return self.__longueur
    
    @property # get
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self,l):
        assert l>0
        self.__longueur = l
    
    @largeur.setter
    def largeur(self,l):
        self.__largeur = l

    def get_surface(self):
        return self.__largeur*self.__longueur

    