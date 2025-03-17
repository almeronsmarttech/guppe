# for em c# ou java
"""
for(i = 0; i<100; i++){
    instruções
}
"""
# iteráveis
nome = "Mauricio Almeron"
lista = [1,2,3,4,5,6]
faixa_valores = range(10)

# iterando sobre uma string
for letra in nome:
    #print(letra)
    print(letra, end=' ')
print('')

# iterando sobre uma string com enumarate
for indice, nome in enumerate(nome):
    print(f"{indice} - {nome}")

print("*****************************************")

# iterando sobre uma lista
for elemento in lista:
    print(elemento)

# iterando sobre uma lista com enumarate
for indice, elemento in enumerate(lista)    :
    print(f"{indice} - {elemento}")

print("*****************************************")

# iterando sobre uma faixa
for valor in faixa_valores:
    print(valor)

# iterando sobre uma faixa com enumarate
for indice, valor in enumerate(faixa_valores):
    print(f"{indice} - {valor}")

print("*****************************************")

quantidade = int(input("Digite o número de vezes a serem repetidas:"))
soma = 0
for i in range(1, quantidade +1 ):
    print(f"Repetindo {quantidade} vezes!")
    num = int(input(f"Digite o valor {i} a ser somado:"))
    soma += num

print(f"O valor total da soma é = {soma}.")

# Emojis unicodes
# mudar o + por três zeros
# U+2764 -> U0002764

for i in range(1,11):
    print('\U0001F60D' * i)