import enum

from Isostatica.Carga import CargaConcentrada


class TipoApoio(enum.Enum):
    simples = 1
    duplo = 2
    engaste = 3


class Apoio:
    def __init__(self, x: float, y: float, tipo_apoio: TipoApoio):
        self.__x = x
        self.__y = y
        self.__tipo_apoio = tipo_apoio
        self.__reacoes = CargaConcentrada(self.__x, self.__y, 0, 0, 0)
        print(self.__reacoes)
    #def __str__(self):
    #    return f"\tPosição: {self.__reacoes}"

class ApoioSimples(Apoio):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, TipoApoio.simples)

        self.__restricao_x = False
        self.__restricao_y = True
        self.__restricao_z = False
        #super().__reacoes.fx = 10
        #self.__reacoes = CargaConcentrada(x, y, 0,10,0)

    def __str__(self):
        pass


class ApoioDuplo(Apoio):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, TipoApoio.duplo)
        self.__restricao_x = True
        self.__restricao_y = True
        self.__restricao_z = False
        #self.__reacoes = CargaConcentrada(x, y, 10, 10, 0)


class Engaste(Apoio):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, TipoApoio.engaste)
        self.__restricao_x = True
        self.__restricao_y = True
        self.__restricao_z = True
        #self.__reacoes = CargaConcentrada(self.__x, self.__y, 10, 10, 10)