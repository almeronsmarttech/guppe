import enum
from Concreto import Concreto

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


class Laje:
    def __init__(self, lx: float, ly: float, h: int, g: float, q: float, tipo_laje: int, concreto: Concreto):
        self.__lx = lx
        self.__ly = ly
        self.__h = h
        self.__lambda = self.__lx / self.__ly
        self.__g = g
        self.__q = q
        self.__p = self.__g + self.__q
        self.__tipo_laje = tipo_laje
        #print(self.__tipo_laje)
        self.__Rx, self.__Rxe, self.__Ry, self.__Rye = 0, 0, 0, 0 # reações de apoio
        self.__Mx, self.__Mxe, self.__My, self.__Mye = 0, 0, 0, 0  # momentos
        self.__D = 0 #  rigidez
        self.__w0 = 0 # flecha inicial

    def calcular_reacoes2(self):
        lambda_val = self.__ly / self.__lx if self.__tipo_laje not in ['2b', '3b', '5b'] else self.__lx / self.__ly

        reacoes = {
            'Rxa': 0,
            'Rya': 0,
            'Rxe': 0,
            'Rye': 0,
            'Qxa': 0,
            'Qya': 0,
            'Qxe': 0,
            'Qye': 0
        }

        if self.__tipo_laje == 1:
            reacoes['Rxa'] = 0.25 / lambda_val
            reacoes['Rya'] = 0.5 - 0.25 / lambda_val

        elif self.__tipo_laje == '2a':
            if lambda_val <= 0.73:
                reacoes['Rye'] = 0.25 * lambda_val
                reacoes['Rya'] = 0.4325 * lambda_val
                reacoes['Rxa'] = 0.5 - 0.341 * lambda_val
            else:
                reacoes['Rya'] = 0.365 - 0.1335 / lambda_val
                reacoes['Rye'] = 0.635 - 0.2315 / lambda_val
                reacoes['Rxa'] = 0.1825 / lambda_val

        elif self.__tipo_laje == '2b':
            if lambda_val <= 0.73:
                reacoes['Rxa'] = 0.25 * lambda_val
                reacoes['Rxe'] = 0.4325 * lambda_val
                reacoes['Rya'] = 0.5 - 0.341 * lambda_val
            else:
                reacoes['Rxa'] = 0.365 - 0.1335 / lambda_val
                reacoes['Rxe'] = 0.635 - 0.2315 / lambda_val
                reacoes['Rya'] = 0.1825 / lambda_val

        elif self.__tipo_laje == '3a':
            if lambda_val <= 0.58:
                reacoes['Rye'] = 0.4325 * lambda_val
                reacoes['Rxa'] = 0.5 - 0.4325 * lambda_val
            else:
                reacoes['Rye'] = 0.5 - 0.145 / lambda_val
                reacoes['Rxa'] = 0.145 / lambda_val

        elif self.__tipo_laje == '3b':
            if lambda_val <= 0.58:
                reacoes['Rxe'] = 0.4325 * lambda_val
                reacoes['Rya'] = 0.5 - 0.4325 * lambda_val
            else:
                reacoes['Rxe'] = 0.5 - 0.145 / lambda_val
                reacoes['Rya'] = 0.145 / lambda_val

        elif self.__tipo_laje == 4:
            reacoes['Rya'] = 0.365 - 0.1825 / lambda_val
            reacoes['Rye'] = 0.635 - 0.3175 / lambda_val
            reacoes['Rxa'] = 0.1825 / lambda_val
            reacoes['Rxe'] = 0.3175 / lambda_val

        elif self.__tipo_laje == '5a':
            if lambda_val >= 0.79:
                reacoes['Rye'] = 0.5 - 0.1975 / lambda_val
                reacoes['Rxa'] = 0.145 / lambda_val
                reacoes['Rxe'] = 0.25 / lambda_val
            else:
                reacoes['Rye'] = 0.3175 * lambda_val
                reacoes['Rxa'] = 0.365 - 0.2315 * lambda_val
                reacoes['Rxe'] = 0.635 - 0.4035 * lambda_val

        elif self.__tipo_laje == '5b':
            if lambda_val >= 0.79:
                reacoes['Rxe'] = 0.5 - 0.1975 / lambda_val
                reacoes['Rya'] = 0.145 / lambda_val
                reacoes['Rye'] = 0.25 / lambda_val
            else:
                reacoes['Rxe'] = 0.3175 * lambda_val
                reacoes['Rya'] = 0.365 - 0.2315 * lambda_val
                reacoes['Rye'] = 0.635 - 0.4035 * lambda_val

        elif self.__tipo_laje == 6:
            reacoes['Rxe'] = 0.25 / lambda_val
            reacoes['Rye'] = 0.5 - 0.25 / lambda_val

        area = self.__lx * self.__ly

        for key in ['Rxa', 'Rya', 'Rxe', 'Rye']:
            if reacoes[key] != 0:
                reacoes['Q' + key[1:]] = reacoes[key] * area * self.__p / (self.__lx if 'x' in key else self.__ly)

        return reacoes

    def calcular_reacoes(self):
        """
        Calcula as reações de apoio para diferentes tipos de lajes retangulares.
        - lx: Comprimento na direção menor (horizontal)
        - ly: Comprimento na direção maior (vertical)
        - Q: Carga total aplicada na laje
        - tipo: Tipo da laje (1 a 9)

        Retorna um dicionário com os valores de R1, R2, R3 e R4.
        """
        lambda_laje = self.__lx / self.__ly
        if self.__tipo_laje == 1:
            print(f"p = {self.__p}")
            R1 = R2 = 0.25 * self.__p *self.__lx * (2 - lambda_laje)
            R3 = R4 = 0.25 * self.__p * self.__lx

        elif self.__tipo_laje == 2:
            R1 = R2 = 0.125 * self.__p * self.__lx * (4 - 2.732 * lambda_laje)
            R3 = 0.433 * self.__p * self.__lx
            R4 = 0.25 * self.__p * self.__lx

        elif self.__tipo_laje == 3:
            R1 = 0.2320724 * self.__p * self.__lx * (2.732 * lambda_laje)
            R2 = 0.577 * R1
            R3 = R4 = 0.183 * self.__p * self.__lx

        elif self.__tipo_laje == 4:
            R1 = self.__p * 0.366 * self.__lx * (1.155 - (self.__lx / self.__ly))
            R2 = self.__p * 1.732 * R1
            R3 = self.__p * 0.317 * self.__lx
            R4 = self.__p * 0.183 * self.__lx

        elif self.__tipo_laje == 5:
            R1 = R2 = R3 = R4 = self.__p * 0.144 * self.__lx

        elif self.__tipo_laje == 6:
            R1 = R2 = self.__p * 0.433 * self.__lx * (1.155 - (self.__lx / self.__ly))
            R3 = R4 = self.__p * 0.433 * self.__lx

        elif self.__tipo_laje == 7:
            R1 = self.__p * 0.232 * self.__lx * (1.578 - (self.__lx / self.__ly))
            R2 = self.__p * 1.732 * R1
            R3 = R4 = self.__p * 0.317 * self.__lx

        elif self.__tipo_laje == 8:
            R1 = R2 = self.__p * self.__lx * (2 - 0.789 * (self.__lx / self.__ly)) / 4
            R3 = self.__p * (self.__lx / 4)
            R4 = self.__p * 0.144 * self.__lx

        elif self.__tipo_laje == 9:
            R1 = R2 = self.__p * (self.__lx * (2 - self.__lx)) / (4 * self.__ly)
            R3 = R4 = self.__p * (self.__lx / 4)



        else:
            raise ValueError("Tipo de laje inválido. Escolha um número de 1 a 9.")

        return {
            'R1': R1,
            'R2': R2,
            'R3': R3,
            'R4': R4
        }

    def calcular_reacoes_apoio(self):
        # caso 7:
        print("Calculo de reacoes de apoio")
        #if self.__tipo_laje.unidirecional_apoiada_apoiada:
        M, Me = 0, 0
        if self.__tipo_laje == 1:
            R = self.__p * self.__lx / 2.0
            M = self.__p * self.__lx * self.__lx / 8.0
            k = 5 # para o cálculo da flecha inicial
            print("Entrou no apoiada apoiada")
        # caso 8:
        #elif self.__tipo_laje.unidirecional_apoiada_engastada:
        elif self.__tipo_laje == 2:
            R = 3 * self.__p * self.__lx / 8.0
            Re = 5 * self.__p * self.__lx / 8.0
            M = self.__p * self.__lx * self.__lx / 14.22
            Me = - self.__p * self.__lx * self.__lx / 8.0
            k = 2 # para o cálculo da flecha inicial
        # caso 9:
        elif self.__tipo_laje == 3:
        #elif self.__tipo_laje.unidirecional_engastada_engastada:
            Re = self.__p * self.__lx / 2.0
            M = self.__p * self.__lx * self.__lx / 24.0
            Me = - self.__p * self.__lx * self.__lx / 12.0
            k = 1
        elif self.__tipo_laje == 4:
            R = self.__p * self.__lx
            Me = - self.__p * self.__lx * self.__lx / 2.0
            k = 48
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

class Bidirecional(Laje):
    pass
