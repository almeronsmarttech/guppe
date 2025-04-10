class Aco:

    def __init__(self, fyk=500, gama_s = 1.15):
        self.__gama_s = gama_s
        self.__fyk = fyk
        self.__fyd = self.__fyk/10/self.__gama_s # kN/cm2
        self.__es = 21000
        print(f"Aço\nfyk: {self.__fyk} MPa\t fyd: {int(self.__fyd)}\t Es: {int(self.__es)} MPa")

    # def calcular_Eci(self):
    #     if self.__fck <= 50:
    #         Eci = self.__alfa_e * 5600 * (self.__fck ** 0.5)
    #     else:
    #         Eci = 21500 * self.__alfa_e * ((self.__fck / 10 + 1.25) ** (1/3))
    #     return int(Eci)
    #
    # def Ecs(self):
    #     return self.__ecs
    #
    # def nu(self):
    #     return self.__nu