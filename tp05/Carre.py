from Rectangle import Rectangle

class Carre(Rectangle):
    
    
    def __init__(self, cote=1):
        super().__init__(cote, cote)
        print(f"def __init__(self, {cote})")
        self.__cote = cote

    @property
    def cote(self):
        return self.__cote
    
    @cote.setter
    def cote(self,c):
        self.__cote = c
        self.longueur = c
        self.largeur = c

    def __str__(self) -> str:
        return f"{__class__.__name__}({self.cote=})"
