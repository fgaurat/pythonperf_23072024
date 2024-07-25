from abc import ABCMeta,abstractmethod

class ICalcGeo(metaclass=ABCMeta):

    @abstractmethod
    def get_surface(self):
        pass
        # raise NotImplementedError("get_surface !!")