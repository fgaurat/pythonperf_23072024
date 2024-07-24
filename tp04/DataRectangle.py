from dataclasses import dataclass

@dataclass
class DataRectangle:
    longueur:int=0
    largeur:int=0

    def get_surface(self):
        return self.largeur*self.longueur
