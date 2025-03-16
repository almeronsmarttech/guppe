
# variáveis locais - escopo compreende todo o programa
# variáveis globais - escopo compreende apenas o bloco que foi declarada

# python é de tipagem dinâmica, ou seja, não é colocado o tipo de variável
# inclusive pode ser alterada no decorrer do programa

numero = 56
print(numero)
print(type(numero))

numero = 48.2
print(numero)
print(type(numero))

numero = 'Almeron'
print(numero)
print(type(numero))

num1 = 56

if num1 < 10:
    novo = num1 + 10
    print(novo)
# se tentar imprimir a variável local novo vai dar erro
# print(novo)


