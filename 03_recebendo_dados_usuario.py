from datetime import datetime

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print(f"Seja muito bem-vindo(a) {nome}!")
print(f"Sua idade é {idade} anos.")

print(f"Olá {nome}, você tem {idade} anos de idade. Nasceu em {datetime.now().year-idade}")