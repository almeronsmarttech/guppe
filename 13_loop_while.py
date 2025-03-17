
"""
c# ou java
while (expressao){
    comandos
}

do{
    comandos
}while (expressao)

python:
while expressao_booleana:
    execução do loop

*** Toda expressão que o resultado poder somente Verdadeiro ou Falso
"""
from http.client import responses

numero = 0

while numero < 100:
    print(numero)
    numero += 1
    # mostrar loop infinito

resposta = ''

while resposta != 'sim':
    resposta = input("Você vai estudar muito para ir bem nesta disciplina?")