from Concreto import Concreto

class Pilar:
    def __init__(self, lx: int, ly: int, le: float, concreto: Concreto):
        self.__lx = lx
        self.__ly = ly
        self.__Ac = self.__lx * self.__ly
        self.__le = le
        self.__concreto = concreto
