class Concreto:
    def __init__(self, fck=20, alfa_b=1):
        self.__fck = fck
        self.__alfa_b = alfa_b
        self.__ni = 0.2
        self.__ecs = 1

    def calcular_modulo_elasticidade_secante(self):
        pass