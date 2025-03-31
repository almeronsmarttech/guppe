from Laje import Laje
from Concreto import Concreto

#from lajes.Laje import TIPO_LAJE

#lx = float(input("lx (m):"))
#ly = float(input("ly (m):"))

concreto = Concreto()

#laje1 = Laje(2,2, 10,5,1,TIPO_LAJE.unidirecional_apoiada_apoiada)
laje1 = Laje(4,4, 10,5,1,3, concreto)
#laje1.calcular_reacoes_apoio()
print(laje1.calcular_reacoes())

#laje2 = Laje(2,2, 10,5,1, TIPO_LAJE.unidirecional_apoiada_engastada)
laje2 = Laje(5.5,6, 10,5,1, 2, concreto)
#laje2.calcular_reacoes_apoio()
print(laje2.calcular_reacoes())

laje3 = Laje(3,5, 10,5,1, 1, concreto)
reacoes = laje3.calcular_reacoes()
print(reacoes)


reacoes = laje3.calcular_reacoes2()
print(reacoes)
