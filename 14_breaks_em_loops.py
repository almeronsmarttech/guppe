


for i in range(15):
    if i == 10:
        print("Saindo do loop através do break.")
        break
    else:
        print(f"i = {i}")


while True:
    comando = input("Digite 'SAIR' para sair.")
    if comando == 'SAIR':
        "Saindo do programa..."
        break