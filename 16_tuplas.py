# Tuplas são imutáveis
# Singifica que não terão os métodos de adição ou remoção de elementos


tupla1 = ()
print(type(tupla1))

tupla2 = (1,2,3,4)
print(type(tupla2))

tupla3 = 1,2,3,4
print(type(tupla3))
print(tupla3)

tupla4 = (4)
print(type(tupla4))
print(tupla4)
# inteiro!

tupla5 = (4,)
print(type(tupla5))
print(tupla5)
# tupla!

# Tuplas são definidas pela vírgula e não pelo parênteses

tupla6 = 4,
print(type(tupla6))
print(tupla6)
# tupla!

tupla7 = tuple(range(0,101,2))
print(type(tupla7))
print(tupla7)
# tupla!

nome_completo = ('Maurício', 'Almeron')
print(nome_completo)
primeiro_nome, sobrenome = nome_completo
print(primeiro_nome)
print(sobrenome)


tupla_numerica = (10,20,30,40,50)
print(type(tupla_numerica))
print(tupla_numerica)
print(sum(tupla_numerica))
print(max(tupla_numerica))
print(min(tupla_numerica))
print(len(tupla_numerica))

# concatenando tuplas
tupla_concat = tupla2 + tupla3
print(tupla_concat)

# Sobrescrevendo a tupla - tuplas só não podem ser editadas, mas podem ser sobrescritas! Não é constante!
print(tupla1)
tupla1 = tupla5 + tupla6
print(tupla1)

# buscando valor em tupla
print('Almeron' in nome_completo)

for elemento in tupla_numerica:
    print(elemento)

for indice, elemento in enumerate(tupla_numerica):
    print(indice, elemento)

# Contando elementos da tupla
nome = tuple(nome_completo[1])
print(nome)
print(nome.count('e'))
print(nome.count('a')) # case sensitive

# As tuplas devem ser utilizadas SEMPRE em que não devem ser alterados os dados da coleção

meses_tupla = ('janeiro', 'fevereiro', 'março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
print(len(meses_tupla))

meses_lista = list(meses_tupla)
meses_lista.append("Almeron") # Faz algum sentido isso?
print(meses_lista)

for i in meses_tupla:
    print(i)

n = 0
while n < len(meses_tupla):
    print(f"{n+1} - {meses_tupla[n]}")
    n += 1

print(meses_tupla.index('julho'))
#print(meses_tupla.index('Almeron'))

print(meses_tupla[2:6])

tupla = (1,2,3)
print(tupla)
nova_tupla = tupla
print(nova_tupla)
outra_tupla = (4,5,6)
nova_tupla = nova_tupla + outra_tupla
print(f"tupla original: {tupla}") # Aqui não tem shallow copy como nas listas
print(f"tupla nova: {nova_tupla}")

