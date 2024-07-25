class Rectangle:
    # __slots__ = ("__longueur", "__largeur")
    __cpt = 0

    def __init__(self,longueur=1,largeur=1):
        print(f"def __init__(self,{longueur},{largeur})")
        assert longueur>0 and largeur>0  
        # if longueur<=0 or largeur<=0:
        #     raise Exception('mauvaises valeurs pour longueur ou largeur')
        Rectangle.__cpt+= 1
        self.__longueur = longueur # _Rectangle__longueur = longueur
        self.__largeur = largeur

    @classmethod
    def buildFromStr(cls,value):
        a,b = [int(v) for v in value.split(";")]

        return cls(a,b)


    @staticmethod
    def get_cpt():
        return Rectangle.__cpt

    @property # get
    def longueur(self):
        """
        return the longueur
        """
        return self.__longueur
    
    @property # get
    def largeur(self)->int:
        return self.__largeur
    
    @longueur.setter
    def longueur(self,l:int):
        assert l>0
        self.__longueur = l
    
    @largeur.setter
    def largeur(self,l):
        self.__largeur = l

    def get_surface(self):
        return self.__largeur*self.__longueur
    
    def __str__(self) -> str:
        return f"{__class__.__name__}({self.longueur=},{self.largeur=})"

    def __eq__(self, value: object) -> bool:
        r = False
        if self.longueur == value.longueur and self.largeur == value.largeur:
            r = True
        return r
