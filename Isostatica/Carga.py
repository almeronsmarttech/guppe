class Carga:
    def __init__(self):
        #self.__x_cg = x_cg
        #self.__y_cg = y_cg
        #self.__Fx = Fx
        #self.__Fy = Fy
        #self.__Mz = Mz
        pass
    def MetodoClasseMae(self):
        print("Método da classe mãe ou super classe Carga.")


class CargaConcentrada(Carga):
    def __init__(self, x, y, fx, fy, mz):
        self.__x = x
        self.__y = y
        self.__Fx = fx
        self.__Fy = fy
        self.__Mz = mz

    def Altera_Cargas(self, Fx: float, Fy: float, Mz: float):
        self.__Fx = Fx
        self.__Fy = Fy
        self.__Mz = Mz

    def __str__(self):
        return f"Fx: {self.__Fx} kN\tFy: {self.__Fy} kN\tMz: {self.__Mz} kN.m"


class CargaUniformementeDistribuida(Carga):
    def __init__(self, x_ini: float, x_fim: float,  y_ini: float, y_fim: float, qx: float, qy: float):
        self.__x_ini = x_ini
        self.__x_fim = x_fim
        self.__lx = self.__x_fim - self.__x_ini
        self.__qx = qx
        self.__y_ini = y_ini
        self.__y_fim = y_fim
        self.__ly = self.__y_fim - self.__y_ini
        self.__qy = qy
        self.__x =self.__lx /2.0
        self.__y = self.__ly/2.0
        self.__F_equivalente = CargaConcentrada(self.__x, self.__y, (self.__qx * self.__lx), (self.__qy * self.__ly), 0)

    def __str__(self):
        return f"xi: {self.__y_ini} m\txf: {self.__y_fim} m\tq: {self.__qx} kN/m\nyi: {self.__y_ini} m\tyf: {self.__y_fim} m\tqy: {self.__qy} kN/m"

class CargaDiferentementeDistribuida(Carga):
    def __init__(self, x_ini: float, x_fim: float,  y_ini: float, y_fim: float,qx_ini: float, qx_fim: float, qy_ini: float, qy_fim: float,):
        self.__x_ini = x_ini
        self.__x_fim = x_fim
        self.__lx = self.__x_fim - self.__x_ini
        self.__qx_ini = qx_ini
        self.__qx_fim = qx_fim
        self.__y_ini = y_ini
        self.__y_fim = y_fim
        self.__ly = self.__y_fim - self.__y_ini
        self.__qy_ini = qy_ini
        self.__qy_fim = qy_fim
        self.__x = self.__lx / 2.0
        if self.__qx_ini < self.__qx_fim:
            self.__x_triangular = 1 * self.__lx /3.0
        else:
            self.__x_triangular = 2 * self.__lx /3.0
        self.__y = self.__ly/2.0
        if self.__qy_ini < self.__qy_fim:
            self.__y_triangular = 1 * self.__ly /3.0
        else:
            self.__y_triangular = 2 * self.__ly /3.0
        self.__F_equivalente = CargaConcentrada(self.__x, self.__y, (self.__qx_ini * self.__lx), (self.__qy_ini * self.__ly), 0)
        self.__F_triangular_equivalente = CargaConcentrada(self.__x_triangular, self.__y_triangular, ((max(self.__qx_ini, self.__qx_fim)-max(self.__qx_ini, self.__qx_fim)) * self.__lx) / 2.0, ((max(self.__qy_ini, self.__qy_fim)-max(self.__qy_ini, self.__qy_fim)) * self.__ly) / 2.0, 0)

    def __str__(self):
        return f"xi: {self.__y_ini} m\txf: {self.__y_fim} m\tqxi: {self.__qx_ini} kN/m\tqxf: {self.__qx_fim} kN/m\nyi: {self.__y_ini} m\tyf: {self.__y_fim} m\tqyi: {self.__qy_ini} kN/m\tqyf: {self.__qy_fim} kN/m"
