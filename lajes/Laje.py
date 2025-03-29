import enum

# class TIPO_LAJE(enum.Enum):
#     bidirecional_simples = 1
#     bidirecional_simplesa = 2
#     bidirecional_simplesb = 3
#     bidirecional_simplesc = 4
#     bidirecional_simplesd = 5
#     bidirecional_simplese = 6
#     unidirecional_apoiada_apoiada = 7
#     unidirecional_apoiada_engastada = 8
#     unidirecional_engastada_engastada = 9

class Concreto:
    def __init__(self, fck=20, alfa_b=1):
        self.__fck = fck
        self.__alfa_b = alfa_b

class Laje:
    def __init__(self, lx: float, ly: float, h: int, g: float, q: float, tipo_laje: int):
        self.__lx = lx
        self.__ly = ly
        self.__h = h
        self.__lambda = self.__lx / self.__ly
        self.__g = g
        self.__q = q
        self.__p = self.__g + self.__q
        self.__tipo_laje = tipo_laje
        #print(self.__tipo_laje)
        self.__Rx, self.__Rxe, self.__Ry, self.__Rye = 0,0,0,0 # reações de apoio
        self.__Mx, self.__Mxe, self.__My, self.__Mye = 0, 0, 0, 0  # momentos
        self.__D = 0 #  rigidez
        self.__w0 = 0


    def calcular_reacoes_apoio(self):
        # caso 7:
        print("Calculo de reacoes de apoio")
        #if self.__tipo_laje.unidirecional_apoiada_apoiada:
        if self.__tipo_laje == 1:
            self.__Rx = self.__p * self.__lx / 2.0
            self.__Mx = self.__p * self.__lx * self.__lx / 8.0
            k = 5 # para o cálculo da flecha inicial
            print("Entrou no apoiada apoiada")
        # caso 8:
        #elif self.__tipo_laje.unidirecional_apoiada_engastada:
        elif self.__tipo_laje == 2:
            self.__Rx = 3 * self.__p * self.__lx / 8.0
            self.__Rxe = 5 * self.__p * self.__lx / 8.0
            self.__Mx = self.__p * self.__lx * self.__lx / 14.22
            self.__Mxe = - self.__p * self.__lx * self.__lx / 8.0
            k = 2 # para o cálculo da flecha inicial
        # caso 9:
        elif self.__tipo_laje == 3:
        #elif self.__tipo_laje.unidirecional_engastada_engastada:
            self.__Rxe = self.__p * self.__lx / 2.0
        elif self.__tipo_laje == 4:
            self.__Rx = self.__p * self.__lx
        else:
            print("Tipo de laje não encontrada")

        print(self.__tipo_laje)
        print(f"Rx : {self.__Rx:.2f} kN/m\tRxe : {self.__Rxe:.2f} kN/m\nMx : {self.__Mx:.2f} kN.m\tMxe : {self.__Mxe:.2f} kN.m")

    def calcular_flecha_inicial(self, k):
        self.__w0 = k * self.__p * self.__lx ** 4 / (384 * self.__D)

class Unidirecional(Laje):
    def __init__(self, lx: float, ly: float, h: int, g: float, q: float, tipo_laje: int):
        super().__init__(lx, ly, h, g, q, tipo_laje)
        #self.__lambda = self.
        #self.__restricao_y = True
        #self.__restricao_z = False

    def calcular_reacoes_apoio(self):
        pass
        # # caso 7:
        # print("Calculo de reacoes de apoio")
        # if self.__tipo_laje.unidirecional_apoiada_apoiada:
        #     self.__Rx = self.__p * self.__lx / 2.0
        #     self.__Mx = self.__p * self.__lx * self.__lx / 8.0
        #     k = 5 # para o cálculo da flecha inicial
        #     print("Entrou no apoiada apoiada")
        # # caso 8:
        # elif self.__tipo_laje.unidirecional_apoiada_engastada:
        #     self.__Rx = 3 * self.__p * self.__lx / 8.0
        #     self.__Rxe = 5 * self.__p * self.__lx / 8.0
        #     self.__Mx = self.__p * self.__lx * self.__lx / 14.22
        #     self.__Mxe = - self.__p * self.__lx * self.__lx / 8.0
        #     k = 2 # para o cálculo da flecha inicial
        # # caso 9:
        # elif self.__tipo_laje.unidirecional_engastada_engastada:
        #     self.__Rxe = self.__p * self.__lx / 2.0
        #
        # else:
        #     print("Tipo de laje não encontrada")
        #
        # print(self.__tipo_laje)
        # print(f"Rx : {self.__Rx}\tRxe : {self.__Rxe}\tMx : {self.__Mx}\tMxe : {self.__Mxe}")
        #
