from Laje import Laje
from Viga import Viga
from Pilar import Pilar


class Pavimento:
    def __init__(self, lajes: [Laje], vigas: [Viga], pilares: [Pilar]):
        self.__lajes = lajes
        self.__vigas = vigas
        self.__pilares = pilares
