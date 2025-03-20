
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