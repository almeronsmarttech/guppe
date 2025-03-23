from Isostatica.Apoio import Apoio
from Isostatica.Carga import Carga


class Estrutura:

    def __init__(self, apoios: [Apoio], cargas_concentradas: [Carga], cargas_uniformemente_distribuidas: [Carga], cargas_desigualmente_distribuidas: [Carga]):
        self.__apoios = apoios
        self.__cargas_concentradas = cargas_concentradas
        self.__cargas_uniformemente_distribuidas = cargas_uniformemente_distribuidas
        self.__cargas_desigualmente_distribuidas = cargas_desigualmente_distribuidas

    def Calcular_Reacoes_Apoio(self):
        #for i in self.__cargas_uniformemente_distribuidas:
        self.SomatorioX()
        self.SomatorioY()

    def SomatorioX(self):
        print("Somatório em X.")
        for i in self.__apoios:
            print(i._Apoio__reacoes)
            print(dir(i))

    def SomatorioY(self):
        print("Somatório em Y.")
        for i in self.__apoios:
        #    print(i)
            print(dir(i))