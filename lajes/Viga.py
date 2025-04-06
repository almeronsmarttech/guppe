from lajes.Concreto import Concreto


class Viga:
    def __init__(self, bw=15, h=40, concreto = Concreto()):
        self.__bw = bw
        self.__h = h
        self.__area = self.__bw * self.__h
        self.__ro_min = self.calcular_area_aco_min
        self.__concreto = concreto

    def calcular_area_aco_min(self):
        pass



