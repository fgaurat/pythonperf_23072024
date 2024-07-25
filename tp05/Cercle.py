import math
from ICalcGeo import ICalcGeo
class Cercle(ICalcGeo):

    def __init__(self, rayon=1):
        print(f"def __init__(self, {rayon})")
        self.__rayon = rayon
    
    @property
    def rayon(self):
        return self.__rayon
    
    @rayon.setter
    def rayon(self,c):
        self.__rayon = c

    def __str__(self) -> str:
        return f"{__class__.__name__}({self.rayon=})"
    
    def get_surface(self):
        return math.pi*self.rayon**2
