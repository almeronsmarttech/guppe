
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

# while produto != 'sair':
#     produto = input("Adicione um produto na lista ou digite 'sair' para sair:")
#     if produto != "sair":
#         carrinho_compras.append(produto)

print(carrinho_compras)

        #  0        1       2       3       4       5
cores = ['bordo','azul','branco','azul','preto','branco']
        #  -6        -5       -4       -3       -2       -1

print(cores)
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
print(cores[4])
print(cores[5])

#print(cores[6])

print('***********')
print(cores[-1])
print(cores[-2])
#print(cores[-7])
print('***********')
for indice, cor in enumerate(cores):
    print(indice, cor)

# Criando um dicionário da lista

cores_dic = list(enumerate(cores))
print(cores_dic)

print(cores.index('branco'))
print(cores.index('branco',3))
print(cores.index('branco',0, len(cores)))

# A forma de buscar um elemento que se repete mais de uma vez é através do for, armazenando o índice em uma lista
elemento = 'branco'
indices = []
for i, x in enumerate(cores):
    if x == elemento:
        indices.append(i)
print(indices)

# Fazendo slice em listas

lista = [1,2,3,4,5,6]

print(lista[1:]) # do elemento de índice 1 até o final
print(lista[:3]) # do primeiro elemento até o elemento de índice 3 - 1 (excludente)
print(lista[1:3]) # do elemento de índice 1 até o elemento de índice 2
print(lista[1:-1]) # do elemento de índice 1 até o penúltimo
print(lista[::2]) # do primeiro elemento até o final, de 2 em 2
print(lista[1::2]) # do segundo elemento até o final, de 2 em 2
print(lista[::-1]) # do último elemento até o primeiro de 1 em 1
print(lista[::-2]) # do último elemento até o primeiro de 2 em 2



print(sum(lista)) # valor da soma dos elementos da lista
print(max(lista)) # valor máximo dos elementos da lista
print(min(lista)) # valor mínimo dos elementos da lista
print(len(lista)) # tamanho da lista

# transformando lista em tupla

print(lista)
print(type(lista))
print(tuple(lista))
print(type(tuple(lista)))

# desempacotando a lista

num1, num2, num3, num4, num5, num6 = lista

print(num1)
print(num5)

print("********************")

print(lista)

lista_copia = lista.copy()
print(lista_copia)
lista_copia.append(7)
print(lista_copia)

# Quando faz uma cópia, ela é uma lista nova com os dados copiados da original *** INDEPENDENTES *** Deep Copy
print("********************")

print(lista)

lista_copia2 = lista

print(lista_copia2)
lista_copia2.append(8)

print(lista_copia2)

print(lista)

# Quando uma lista é atribuída a outra lista elas apontam para o mesmo local da memória *** DEPENDENTES *** Shallow Copy