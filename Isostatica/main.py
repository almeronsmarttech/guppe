from Apoio import ApoioSimples, ApoioDuplo
from Carga import CargaConcentrada, CargaUniformementeDistribuida
from Estrutura import Estrutura

apoios = []
cargas_concentradas = []
cargas_uniformemente_distribuidas = []
cargas_diferentemente_distribuidas = []

apoio1 = ApoioSimples(0,0)
apoio2 = ApoioDuplo(4,0)
print(type(apoio1))

apoios.append(apoio1)
apoios.append(apoio2)

carga_concentrada1 = CargaConcentrada(1.5,0,60,0,0)
cargas_concentradas.append(carga_concentrada1)
print(type(carga_concentrada1))

estrutura1 = Estrutura(apoios,cargas_concentradas, cargas_uniformemente_distribuidas, cargas_diferentemente_distribuidas)
estrutura1.Calcular_Reacoes_Apoio()
print(type(estrutura1))