
lista1 = [99,1,5,9,8,3,7]
lista2 = ['A','l','m','e','r','o','n']
lista3 = []
lista4 = list(range(111))
lista5 = list('Almeron')

print(type(lista1))
print(lista1)

print(type(lista2))
print(lista2)

print(type(lista3))
print(lista3)

print(type(lista4))
print(lista4)

print(type(lista5))
print(lista5)

# procurar valor em uma lista
num_procurado = 18

if num_procurado in lista1:
    print(f"Foi encontrado o número {num_procurado}!")
else:
    print(f"Não foi encontrado o número {num_procurado}.")

# Ordenando listas
lista1_ordenada = lista1.copy()
lista1_ordenada.sort()
print(lista1_ordenada)
print(lista1)

lista2_ordenada = lista2.copy()
lista2_ordenada.sort()
print(lista2_ordenada)
print(lista2)

# Contando número de ocorrências de um elemento
print(lista2.count('A'))

# Adicionando elemento em lista (um elemento por vez!)
print(lista1)
lista1.append(100)
print(lista1)

# Adicionando um elmento do tipo lista
lista1.append([1,2,3])
print(lista1)
# Procurando a lista na lista
if [1,2,3] in lista1:
    print("Encontrei a lista.")
else:
    print("Não encontrei a lista.")

# Coloca valores como elementos adicionais
lista_nova = [4,5,6]
lista1.extend(lista_nova)
print(lista1)
# Mais um exemplo do mesmo
lista1.extend([7,8,9])
print(lista1)
# Mais um exemplo do mesmo
lista1.extend("Almeron")
print(lista1)

# Adicionando elemento em posição específica
lista1.insert(1,95)
print(lista1)

#podemos juntar duas listas

lista6 = lista2 + lista5
print(lista6)

lista7 = lista6.copy()
lista6.sort()
print(lista6)
lista6.reverse()
print(lista6)

# mesma coisa que
print(lista7[::-1])
