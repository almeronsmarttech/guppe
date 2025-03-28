
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

# contado elementos
print(len(lista1))
print(len(lista7))

# removendo o último elemento
print(lista1)
elemento_excluido_lista1 = lista1.pop()
print(f"O elemento excluído foi {elemento_excluido_lista1}.")
print(lista1)
print(lista7)
elemento_excluido_lista7 = lista7.pop()
print(f"O elemento excluído foi {elemento_excluido_lista7}.")
print(lista7)

# removendo elemento com índice específico

elemento_excluido_lista7a = lista7.pop(6)
print(f"O elemento excluído foi {elemento_excluido_lista7a}.")
print(lista7)

# removendo toda a lista (limpando a lista)
print(lista6)
lista6.clear()
print(lista6)

# repetindo listas
lista6 = lista1 * 2
print(lista6)

# convertendo string para lista
nome_completo = "Maurício Monteiro Almeron"
print(nome_completo)
print(type(nome_completo))
lista_nome = list(nome_completo)
print(lista_nome)
print(type(lista_nome))

# separando palavras de uma frase
frase = "Este é um curso programação de linguagem python."
print(frase)
print(type(frase))
lista_palavras = frase.split() # por padrão o separador é espaço
print(lista_palavras)
print(type(lista_palavras))

frase1 = "Universidade;de;Caxias;do;Sul"
print(frase1)
print(type(frase1))
lista_palavras1 = frase1.split(';') # por padrão o separador é espaço
print(lista_palavras1)
print(type(lista_palavras1))

# transformando uma lista em uma string
frase2 = ' '.join(lista_palavras1)
print(frase2)

# outros exemplos de join
frase3 = '_'.join(lista_palavras1)
print(frase3)

frase4 = 'ALM'.join(lista_palavras1)
print(frase4)

lista8 = [1, 3.1415, True, 'Almeron', [1,2,3,4], 456_465_465]
print(lista8)
print(type(lista8))

# iterando sobre listas
# através do for
lista9 = list('Almeron')
print(lista9)
soma = ''
for elemento in lista9:
    print(elemento)
    soma += elemento

print(soma)

# através do while

carrinho_compras = []
produto = ''

while produto != 'sair':
    produto = input("Adicione um produto na lista ou digite 'sair' para sair:")
    if produto != "sair":
        carrinho_compras.append(produto)

print(carrinho_compras)



