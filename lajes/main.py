from Laje import Laje
#from lajes.Laje import TIPO_LAJE

#lx = float(input("lx (m):"))
#ly = float(input("ly (m):"))

#laje1 = Laje(2,2, 10,5,1,TIPO_LAJE.unidirecional_apoiada_apoiada)
laje1 = Laje(2,2, 10,5,1,1)
laje1.calcular_reacoes_apoio()

#laje2 = Laje(2,2, 10,5,1, TIPO_LAJE.unidirecional_apoiada_engastada)
laje2 = Laje(2,2, 10,5,1, 2)
laje2.calcular_reacoes_apoio()