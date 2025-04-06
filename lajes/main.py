from Laje import Laje
from Viga import Viga
from Pilar import Pilar
from Concreto import Concreto
from Pavimento import Pavimento

#from lajes.Laje import TIPO_LAJE

#lx = float(input("lx (m):"))
#ly = float(input("ly (m):"))

concreto = Concreto()

laje1 = Laje(4,4, 10,5,1,3, concreto)
print(laje1.calcular_reacoes())

laje2 = Laje(5.5,6, 10,5,1, 2, concreto)
print(laje2.calcular_reacoes())

laje3 = Laje(3,5, 10,5,1, 1, concreto)
reacoes = laje3.calcular_reacoes()
print(reacoes)

reacoes = laje3.calcular_reacoes2()
print(reacoes)

lajes = [laje1, laje2, laje3]

vigas = []
v1 = Viga(bw=20,h=45,concreto=concreto)
vigas.append(v1)

pilares = []
p1 = Pilar(lx=25,ly=50,le=300,concreto=concreto)
pilares.append(p1)

pavimento = Pavimento(lajes,vigas, pilares)
