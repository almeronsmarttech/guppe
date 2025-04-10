from ParametrosAraujo import *
from Concreto import Concreto
from Aco import Aco


class Laje:
    def __init__(self, lx: float, ly: float, h: int, g: float, q: float, tipo_laje: int, concreto: Concreto, psi2=0.4):
        self._lx = lx
        self._ly = ly
        self.__h = h
        self.__g = g
        self.__q = q
        self._p = self.__g + self.__q
        self._p_serv =self.__g + 0.3* self.__q
        self._tipo_laje = tipo_laje
        self.__concreto = concreto
        self._D = (self.__concreto.Ecs() *self.__h/10*self.__h/10*self.__h/10)/(12*(1-(self.__concreto.nu()*self.__concreto.nu()))) #  rigidez
        print(f"D: {int(self._D)}")
        self._w0 = 0 # flecha inicial




class LajeUnidirecional(Laje):
    def __init__(self, lx: float, ly: float, h: int, g: float, q: float, tipo_laje: int, concreto: Concreto, psi2=0.4):
        super().__init__(lx, ly, h, g, q, tipo_laje, concreto,psi2)
        self.__R = 0
        self.__Re = 0
        self.__M, self.__Me = 0, 0
        self.__k = 0


    def calcular_reacoes_apoio(self):
        print("Calculo de reacoes de apoio")
        if self._tipo_laje == 1:
             self.__R = self._p * self._lx / 2.0
             self.__M = self._p * self._lx * self._lx / 8.0
             self.__k = 5 # para o cálculo da flecha inicial
             print("Entrou no apoiada apoiada")
        elif self._tipo_laje == 2:
             self.__R = 3 * self._p * self._lx / 8.0
             self.__Re = 5 * self._p * self._lx / 8.0
             self.__M = self._p * self._lx * self._lx / 14.22
             self.__Me = - self._p * self._lx * self._lx / 8.0
             self.__k = 2 # para o cálculo da flecha inicial
        elif self._tipo_laje == 3:
             self.__Re = self._p * self._lx / 2.0
             self.__M = self._p * self._lx * self._lx / 24
             self.__Me = - self._p * self._lx * self._lx / 12
             self.__k = 1
        elif self._tipo_laje == 4:
             self.__Re = self._p * self._lx
             self.__Me = - self._p * self._lx * self._lx / 2
             self.__k = 48
        else:
            print("Tipo de laje não encontrada")

        print(f"Tipo de laje: {self._tipo_laje}")
        print(f"Rx : {self.__R:.2f} kN/m\tRxe : {self.__Re:.2f} kN/m\nMx : {self.__M:.2f} kN.m/m\tMxe : {self.__Me:.2f} kN.m/m")

    def calcular_flecha_inicial(self):
        self._w0 = self.__k * self._p_serv * self._lx ** 4 / (384 * self._D)
        print(f"Flecha inicial: {self._w0}")

class LajeBidirecional(Laje):
    def __init__(self, lx: float, ly: float, h: int, g: float, q: float, tipo_laje: int, concreto: Concreto, psi2=0.4):
        super().__init__(lx, ly, h, g, q, tipo_laje, concreto, psi2)

        self.__lambda, self.__wc, self.__mxe, self.__mye,self.__mx, self.__my, self.__mxy, self.__rxe, self.__rx, self.__rye, self.__ry, self.__beta_x, self.__beta_y = 0,0,0,0,0,0,0,0,0,0,0,0,0
        self.__mx,self.__mxe,self.__my,self.__mye = 0,0,0,0
        self.__Rx, self.__Rxe, self.__Ry, self.__Rye = 0, 0, 0, 0  # reações de apoio
        self.__Mx, self.__Mxe, self.__My, self.__Mye = 0, 0, 0, 0  # momentos

    # Usado no TCC de engenharia civil
    def calcular_reacoes2(self):
        lambda_val = self._ly / self._lx if self._tipo_laje not in ['2b', '3b', '5b'] else self._lx / self._ly

        reacoes = {'Rxa': 0,'Rya': 0,'Rxe': 0,'Rye': 0,'Qxa': 0,'Qya': 0,'Qxe': 0,'Qye': 0}

        if self._tipo_laje == 1:
            reacoes['Rxa'] = 0.25 / lambda_val
            reacoes['Rya'] = 0.5 - 0.25 / lambda_val

        elif self._tipo_laje == '2a':
            if lambda_val <= 0.73:
                reacoes['Rye'] = 0.25 * lambda_val
                reacoes['Rya'] = 0.4325 * lambda_val
                reacoes['Rxa'] = 0.5 - 0.341 * lambda_val
            else:
                reacoes['Rya'] = 0.365 - 0.1335 / lambda_val
                reacoes['Rye'] = 0.635 - 0.2315 / lambda_val
                reacoes['Rxa'] = 0.1825 / lambda_val

        elif self._tipo_laje == '2b':
            if lambda_val <= 0.73:
                reacoes['Rxa'] = 0.25 * lambda_val
                reacoes['Rxe'] = 0.4325 * lambda_val
                reacoes['Rya'] = 0.5 - 0.341 * lambda_val
            else:
                reacoes['Rxa'] = 0.365 - 0.1335 / lambda_val
                reacoes['Rxe'] = 0.635 - 0.2315 / lambda_val
                reacoes['Rya'] = 0.1825 / lambda_val

        elif self._tipo_laje == '3a':
            if lambda_val <= 0.58:
                reacoes['Rye'] = 0.4325 * lambda_val
                reacoes['Rxa'] = 0.5 - 0.4325 * lambda_val
            else:
                reacoes['Rye'] = 0.5 - 0.145 / lambda_val
                reacoes['Rxa'] = 0.145 / lambda_val

        elif self._tipo_laje == '3b':
            if lambda_val <= 0.58:
                reacoes['Rxe'] = 0.4325 * lambda_val
                reacoes['Rya'] = 0.5 - 0.4325 * lambda_val
            else:
                reacoes['Rxe'] = 0.5 - 0.145 / lambda_val
                reacoes['Rya'] = 0.145 / lambda_val

        elif self._tipo_laje == 4:
            reacoes['Rya'] = 0.365 - 0.1825 / lambda_val
            reacoes['Rye'] = 0.635 - 0.3175 / lambda_val
            reacoes['Rxa'] = 0.1825 / lambda_val
            reacoes['Rxe'] = 0.3175 / lambda_val

        elif self._tipo_laje == '5a':
            if lambda_val >= 0.79:
                reacoes['Rye'] = 0.5 - 0.1975 / lambda_val
                reacoes['Rxa'] = 0.145 / lambda_val
                reacoes['Rxe'] = 0.25 / lambda_val
            else:
                reacoes['Rye'] = 0.3175 * lambda_val
                reacoes['Rxa'] = 0.365 - 0.2315 * lambda_val
                reacoes['Rxe'] = 0.635 - 0.4035 * lambda_val

        elif self._tipo_laje == '5b':
            if lambda_val >= 0.79:
                reacoes['Rxe'] = 0.5 - 0.1975 / lambda_val
                reacoes['Rya'] = 0.145 / lambda_val
                reacoes['Rye'] = 0.25 / lambda_val
            else:
                reacoes['Rxe'] = 0.3175 * lambda_val
                reacoes['Rya'] = 0.365 - 0.2315 * lambda_val
                reacoes['Rye'] = 0.635 - 0.4035 * lambda_val

        elif self._tipo_laje == 6:
            reacoes['Rxe'] = 0.25 / lambda_val
            reacoes['Rye'] = 0.5 - 0.25 / lambda_val

        area = self._lx * self._ly

        for key in ['Rxa', 'Rya', 'Rxe', 'Rye']:
            if reacoes[key] != 0:
                reacoes['Q' + key[1:]] = reacoes[key] * area * self._p / (self._lx if 'x' in key else self._ly)

        return reacoes

    def calcular_reacoes(self):
        lx_ly = self._lx / self._ly
        ly_lx = self._ly / self._lx
        if self._tipo_laje == 1:
            teste = buscar_parametros_laje (self, lx_ly, tabela_tipo1_lxly)
            print(teste)
        elif self._tipo_laje == 2:
            teste = buscar_parametros_laje(self, lx_ly, tabela_tipo2_lxly)
            print(teste)
        elif self._tipo_laje == 3:
            teste = buscar_parametros_laje(self, lx_ly, tabela_tipo3_lxly)
            print(teste)
        elif self._tipo_laje == 4:
            teste = buscar_parametros_laje(self, lx_ly, tabela_tipo4_lxly)
            print(teste)
        elif self._tipo_laje == 5:
            teste = buscar_parametros_laje(self, lx_ly, tabela_tipo5_lxly)
            print(teste)
        elif self._tipo_laje == 6:
            teste = buscar_parametros_laje(self, lx_ly, tabela_tipo6_lxly)
            print(teste)
        else:
            raise ValueError("Tipo de laje inválido. Escolha um número de 1 a 6.")

        self.__lambda, self.__wc, self.__mxe, self.__mye, self.__mx, self.__my, self.__mxy, self.__rxe, self.__rx, self.__rye, self.__ry, self.__beta_x, self.__beta_y = teste.values()


    def calcular_reacoes_apoio(self):
        self.__Rx =0.001*self.__rx*self._p * self._lx
        self.__Rxe = 0.001 * self.__rxe * self._p * self._lx
        self.__Ry=0.001 * self.__ry * self._p * self._lx
        self.__Rye=0.001 * self.__rye * self._p * self._lx
        print(f"Reações de Apoio:\nRx: {self.__Rx:.2f}\tRxe: {self.__Rxe:.2f}\tRy: {self.__Ry:.2f}\tRye: {self.__Rye:.2f}")

    def calcular_momentos_fletores(self):
        self.__Mx =0.001 * self.__mx * self._p * self._lx * self._lx
        self.__Mxe = 0.001 * self.__mxe * self._p * self._lx * self._lx
        self.__My=0.001 * self.__my * self._p * self._lx * self._lx
        self.__Mye=0.001 * self.__mye * self._p * self._lx * self._lx
        print(f"Momentos Fletores:\nMx: {self.__Mx:.2f}\tMxe: {self.__Mxe:.2f}\tRy: {self.__My:.2f}\tRye: {self.__Mye:.2f}")

    def imprimir_parametros(self):
        print(f"{self.__lambda, self.__wc, self.__mxe, self.__mye,self.__mx, self.__my, self.__mxy, self.__rxe, self.__rx, self.__rye, self.__ry, self.__beta_x, self.__beta_y}")

    def calcular_flecha_inicial(self):
        self._w0 = 0.001 * self.__wc * self._p_serv * self._lx ** 4 / (self._D)
        print(f"Flecha inicial: {self._w0}")


