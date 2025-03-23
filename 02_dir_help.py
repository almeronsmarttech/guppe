
nome_completo1 = 'mauricio monteiro almeron'

nome_completo2 = 'MAURICIO MONTEIRO ALMERON'

nome_completo3 = 'Mauricio Monteiro Almeron'

print(dir(nome_completo1))
print(nome_completo1.count('a')+nome_completo1.count('m'))
help(nome_completo1.count)

if nome_completo1 == nome_completo2:
    print("Os nomes são iguais.")
else:
    print("Os nomes são diferentes.")

print(nome_completo1.capitalize())
print(nome_completo1)
print(nome_completo1.title())

numero1 = 15
numero2 = 3.1415
print(numero1)
print(dir(numero1))
print(numero1.is_integer())
print(numero2.is_integer())
#print(nome_completo1.is_inte)
import sys
print(sys.getsizeof(numero1))
print(sys.getsizeof(numero2))