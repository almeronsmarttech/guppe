
# inicia em zero, excludente e o passo igual a um por default
for i in range(10):
    print(i)

print("******")

# valor de início, excludente e o passo igual a um por default
for i in range(5, 10):
    print(i)

print("******")

# valor de início, excludente e o passo definido
for i in range(2, 10, 2):
    print(i)


print("******")

# valor de início, excludente e o passo definido
for i in range(0, 100, 20):
    print(i)

print("******")

# valor final exclusivo, valor de início e o passo definido decremento
for i in range(10, -1, -1): # contagem regressiva
    print(i)

print("******")

# valor final exclusivo, valor de início e o passo definido decremento
for i in range(500, 0, -100):
    print(i)