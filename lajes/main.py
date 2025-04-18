from Laje import LajeUnidirecional, LajeBidirecional
from Viga import Viga
from Pilar import Pilar
from Concreto import Concreto, TipoAgregado
from Aco import Aco, Barra
from Pavimento import Pavimento

C25 = Concreto(fck=25, tipo_agregado=TipoAgregado.CALCARIO)
aco_CA50 = Aco(fyk=500)
aco_CA60 = Aco(fyk=600)
bitolas =[]
barra_5mm = Barra(aco_CA60,diametro=5.0)
bitolas.append(barra_5mm)
barra_6_3mm = Barra(aco_CA50,diametro=6.3)
bitolas.append(barra_6_3mm)
barra_8mm = Barra(aco_CA50,diametro=8.0)
bitolas.append(barra_8mm)


print("****** Teste Laje Unidirecional ******")
laje_uni = LajeUnidirecional(1.4, 5, 10, 5, 2.5, 1, C25, aco_CA50, bitolas, psi2 = 0.3)
laje_uni.calcular_reacoes_apoio()
laje_uni.calcular_momentos_fletores()
laje_uni.calcular_flecha_inicial()
laje_uni.calcular_flecha_final(alfa_f=2.5)
laje_uni.calcular_armaduras()
laje_uni.detalhar_armaduras()

print("****** Teste Laje Bidirecional ******")
laje_bi = LajeBidirecional(2.7, 5.1, 10, 3.5, 1.5, 5, C25, aco_CA50, bitolas, psi2 = 0.3)
laje_bi.calcular_reacoes()
#laje_bi.imprimir_parametros()
laje_bi.calcular_reacoes_apoio()
laje_bi.calcular_momentos_fletores()
laje_bi.calcular_flecha_inicial()
laje_bi.calcular_flecha_final(alfa_f=2.5)
laje_bi.calcular_armaduras()
laje_bi.detalhar_armaduras()
# lx, ly = 4, 4
# if lx / ly < 0.5:
#     laje1 = LajeUnidirecional(lx,ly, 10,5,1,3, concreto)
# else:
#     laje1 = LajeBidirecional(lx,ly, 10,5,1,3, concreto)
# print(laje1.calcular_reacoes())

# laje1 = LajeBidirecional(4, 4, 10, 5, 1, 3, C25, aco_CA50)
#
# concreto1 = Concreto(fck=30,tipo_agregado=TipoAgregado.BASALTO_DIABASIO,gama_c=1.4)
# laje2 = LajeBidirecional(5.5,6, 10,5,1, 2, concreto1, aco_CA50)
# print(laje2.calcular_reacoes())
#
# laje3 = LajeBidirecional(3,5, 10,5,1, 1, concreto1, aco_CA50)
# reacoes = laje3.calcular_reacoes()
# print(reacoes)
#
# reacoes = laje3.calcular_reacoes2()
# print(reacoes)
#
# concreto2 = Concreto(fck=50,tipo_agregado=TipoAgregado.BASALTO_DIABASIO,gama_c=1.4)
# concreto3 = Concreto(fck=90,tipo_agregado=TipoAgregado.GRANITO_GNAISSE,gama_c=1.4)
#
# lajes = [laje1, laje2, laje3]
#
# vigas = []
# v1 = Viga(bw=20, h=45, concreto=C25)
# vigas.append(v1)
#
# pilares = []
# p1 = Pilar(lx=25,ly=50,le=300,concreto=concreto1)
# pilares.append(p1)
#
# pavimento = Pavimento(lajes,vigas, pilares)

#lx = float(input("lx (m):"))
#ly = float(input("ly (m):"))